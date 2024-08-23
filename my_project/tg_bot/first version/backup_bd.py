import shutil
import os
from datetime import datetime

# Путь к базе данных
db_path = '/market/instance/mydatabase.db'
# Папка для хранения резервных копий
backup_folder = '/market/backups'

# Убедитесь, что папка для резервных копий существует
os.makedirs(backup_folder, exist_ok=True)

# Форматирование текущей даты для добавления к имени файла
current_date = datetime.now().strftime('%Y-%m-%d')
backup_path = os.path.join(backup_folder, f'mydatabase_backup_{current_date}.db')

# Копирование базы данных
shutil.copy2(db_path, backup_path)
print(f'Backup created at {backup_path}')
