

dict = [".com", ".ru", ".net"]

def check_email(email):


    for k in range(len(dict)):
        if email.endswith(dict[k]) and "@" in email:
            return True

    return False





def send_email(message, recipient, sender="university.help@gmail.com"):

    check_recipient = check_email(recipient)
    check_sender = check_email(sender)

    if not check_sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com" and check_sender:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

