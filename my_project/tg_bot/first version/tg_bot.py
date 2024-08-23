import time

from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
import requests
#from flask_sqlalchemy import Pagination
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///G://prejecet/epishura_market/instance/mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    epicoin = db.Column(db.Integer)
    full_name = db.Column(db.String(100))
    birthday = db.Column(db.String(100))
    company = db.Column(db.String(100))
    status = db.Column(db.String(100), default='Inactive')
    selected_products = db.Column(db.String(1000), default='')
    total_amount = db.Column(db.Integer, default=0)
    product_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.id}>'

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_type = db.Column(db.String(100))
    user_id = db.Column(db.Integer)
    full_name = db.Column(db.String(100))
    amount = db.Column(db.Float)
    product = db.Column(db.String(100))
    is_completed = db.Column(db.Boolean, default=False)
    delivery_address = db.Column(db.String(200))

    def __repr__(self):
        return f'<Request {self.id}>'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<Product {self.id} - {self.name}>'

# Создаем все таблицы, если их еще нет
with app.app_context():
    db.create_all()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid input"}), 400

    user_id = data.get('ID')
    full_name = data.get('Full_name')
    user_company = data.get('User_Company')
    epicoin = data.get('EpiCoin', 0)
    status = data.get('Status', 'Inactive')
    birthday = data.get('birthday')

    if not user_id or not full_name or not user_company:
        return jsonify({"error": "Missing required fields"}), 400

    existing_user = User.query.filter_by(user_id=user_id).first()
    if existing_user:
        existing_user.full_name = full_name
        existing_user.company = user_company
        existing_user.epicoin = epicoin
        existing_user.status = status
        existing_user.birthday = birthday
    else:
        user = User(user_id=user_id, full_name=full_name, company=user_company, epicoin=epicoin, status=status, birthday=birthday)
        db.session.add(user)

    db.session.commit()
    return jsonify({"message": "Data received"}), 200

@app.route('/request', methods=['POST'])
def handle_request():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid input"}), 400

    request_type = data.get('request_type')
    user_id = data.get('user_id')
    full_name = data.get('full_name')
    amount = data.get('amount')
    product = data.get('product')
    delivery_address = data.get('delivery_address')

    if not request_type or not user_id or not full_name or not amount or not product or not delivery_address:
        return jsonify({"error": "Missing required fields"}), 400

    new_request = Request(request_type=request_type, user_id=user_id, full_name=full_name, amount=amount,
                          product=product, delivery_address=delivery_address)
    db.session.add(new_request)
    db.session.commit()

    return jsonify({"message": "Request received"}), 200

@app.route('/requests/<int:request_id>/toggle', methods=['POST', 'PUT'])
def toggle_request_completion(request_id):
    req = db.session.get(Request, request_id)
    if req:
        req.is_completed = not req.is_completed
        db.session.commit()
        flash('Request status updated successfully', 'success')
    else:
        flash('Request not found', 'error')
    return redirect(url_for('list_requests'))

@app.route('/users', methods=['GET'])
def get_users():
    sort_by = request.args.get('sort_by', 'user_id')
    search_query = request.args.get('search', '')

    users = User.query.filter(
        User.user_id.like(f'%{search_query}%') |
        User.full_name.like(f'%{search_query}%') |
        User.company.like(f'%{search_query}%') |
        User.epicoin.like(f'%{search_query}%') |
        User.status.like(f'%{search_query}%')
    ).order_by(getattr(User, sort_by)).all()

    return render_template('users.html', users=users, search_query=search_query)

from flask import render_template

# Функция для отображения списка существующих запросов
@app.route('/requests', methods=['GET'])
def list_requests():
    sort_by = request.args.get('sort_by', 'request_type')
    search_query = request.args.get('search', '')

    requests = Request.query.filter(
        Request.request_type.like(f'%{search_query}%') |
        Request.user_id.like(f'%{search_query}%') |
        Request.full_name.like(f'%{search_query}%') |
        Request.amount.like(f'%{search_query}%') |
        Request.product.like(f'%{search_query}%')
    ).order_by(getattr(Request, sort_by)).all()

    return render_template('requests.html', requests=requests, search_query=search_query)


@app.route('/create_request', methods=['POST'])
def create_request():
    try:
        # Получение данных из JSON тела запроса
        request_data = request.get_json()

        request_type = request_data['request_type']
        user_id = request_data['user_id']
        full_name = request_data['full_name']
        amount = request_data['amount']
        product = request_data['product']
        delivery_address = request_data['delivery_address']

        # Создание нового объекта запроса
        new_request = Request(
            request_type=request_type,
            user_id=user_id,
            full_name=full_name,
            amount=amount,
            product=product,
            delivery_address=delivery_address
        )

        # Добавление в базу данных
        db.session.add(new_request)
        db.session.commit()

        flash('Request submitted successfully', 'success')

        return jsonify({'message': 'Request created successfully'}), 201  # Возвращаем JSON с сообщением об успешном создании запроса
    except KeyError as e:
        # Обработка ошибки, если какой-то ключ отсутствует в request_data
        return jsonify({'error': 'Missing required field in the request'}), 400
    except Exception as e:
        # Обработка других исключений, если что-то пошло не так
        return jsonify({'error': str(e)}), 500


@app.route('/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Количество продуктов на странице
    products = Product.query.paginate(page=page, per_page=per_page)
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        product_price = request.form['product_price']

        # Проверяем, существует ли продукт с заданным ID
        existing_product = Product.query.filter_by(id=product_id).first()
        if existing_product:
            flash(f'Product ID {product_id} is already taken. Please choose a different ID.', 'error')
            return redirect(url_for('add_product'))

        # Создаем новый объект продукта
        new_product = Product(id=product_id, name=product_name, price=product_price)

        # Добавляем в базу данных и сохраняем изменения
        db.session.add(new_product)
        db.session.commit()

        flash('Product added successfully', 'success')

        # Ждем 2 секунды перед редиректом, чтобы пользователь увидел сообщение
        time.sleep(2)

        return redirect(url_for('get_products'))

    return render_template('add_product.html')


@app.route('/products/<int:product_id>/delete', methods=['POST', 'DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash(f'Product {product.name} deleted successfully', 'success')
    return redirect(url_for('get_products'))


@app.route('/products/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        # Обработка данных из формы редактирования
        new_product_id = request.form['product_id']
        product_name = request.form['product_name']
        product_price = request.form['product_price']

        # Проверка, изменился ли ID продукта
        if new_product_id != product.id:
            existing_product = Product.query.filter_by(id=new_product_id).first()
            if existing_product and existing_product.id != product.id:
                flash(f'Product ID {new_product_id} is already taken. Please choose a different ID.', 'error')
                return redirect(url_for('edit_product', product_id=product.id))

        # Обновление данных продукта
        product.id = new_product_id
        product.name = product_name
        product.price = product_price
        db.session.commit()
        flash(f'Product {product.name} updated successfully', 'success')
        return redirect(url_for('get_products'))

    return render_template('edit_product.html', product=product)



@app.route('/process_choice', methods=['POST'])
def process_choice():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid input"}), 400

        print("Received data:", data)

        choice_item = data.get('Choice_item')
        user_id = data.get('user_id')

        if not choice_item or not user_id:
            return jsonify({"error": "Missing required fields"}), 400

        choice_item = int(choice_item)
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        bot_token = ''

        if choice_item == 0:
            user.selected_products = ''
            user.total_amount = 0
            user.product_count = 0
            db.session.commit()
            return jsonify({"message": "Selection reset successfully"}), 200

        product = Product.query.get(choice_item)
        if not product:
            return jsonify({"error": "Invalid choice item"}), 400

        product_name = product.name
        price = float(product.price)

        if user.selected_products:
            selected_products = user.selected_products.split(', ')
        else:
            selected_products = []

        selected_products.append(product_name)
        user.selected_products = ', '.join(selected_products)

        user.total_amount += price
        user.product_count += 1
        db.session.commit()

        # Обновляем значение переменной amount
        amount_expression = str(user.total_amount)
        amount_update_url = f"https://api.puzzlebot.top/?token={bot_token}&method=variableChange&user_id={user_id}&variable=amount&expression={amount_expression}"
        response_amount = requests.get(amount_update_url)
        print("Update amount response:", response_amount.json())

        # Обновляем значение переменной Choice_accept
        choice_expression = ''.join(user.selected_products)  # Объединяем в одно слово без запятых
        choice_expression_encoded = urllib.parse.quote(f'"{choice_expression}"')  # Экранируем кавычки и кодируем строку целиком
        choice_update_url = f"https://api.puzzlebot.top/?token={bot_token}&method=variableChange&user_id={user_id}&variable=Choice_accept&expression={choice_expression_encoded}"
        response_choice = requests.get(choice_update_url)
        print("Update Choice_accept response:", response_choice.json())

        if all(response.json().get('code') == 0 for response in [response_amount, response_choice]):
            return jsonify({"message": "Choice processed successfully"}), 200
        else:
            return jsonify({"error": "Failed to update bot variables"}), 500

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/')
def index():
    return redirect('/users')

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        result = subprocess.run(['python', '/market/backup_db.py'], capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500
        return jsonify({"message": "Script executed successfully", "output": result.stdout}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

scheduler = BackgroundScheduler()

@scheduler.scheduled_job('cron', hour=0, minute=0)
def backup_database():
    try:
        result = subprocess.run(['python', '/market/backup_db.py'], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Backup script error: {result.stderr}")
        else:
            print(f"Backup script output: {result.stdout}")
    except Exception as e:
        print(f"Exception occurred: {str(e)}")

scheduler.start()

@app.teardown_appcontext
def shutdown_session(exception=None):
    if scheduler.running:
        scheduler.shutdown()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
