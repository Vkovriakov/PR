def send_email(message, recipient, sender="university.help@gmail.com"):
    if '@' not in recipient or not recipient.endswith(
            ('.com', '.ru', 'net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
     print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
     print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
     print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
     print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('message', 'razor@gmail.com')
send_email('message', 'boook0909@mail.net', 'kniwers6567@gmail.com')
send_email('message', 'ctuytcf788@mail.net', 'iubbyi8098@mail.vb')
send_email('message', 'university.help@gmail.com', 'university.help@gmail.com')