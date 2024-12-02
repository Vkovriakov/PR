def send_email(message, recipient = 'petya8438.ru', *,sender = "university.help@gmail.com"):
    print(message, sender, recipient)
send_email(message = 'Письмо успешно отправлено с адреса',
           recipient =  ' на адрес petya8438.ru')
send_email(message= 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса',
           recipient= 'на адрес urban.fan@mail.ru')
send_email(message= 'Невозможно отправить письмо с адреса',
           sender = 'urban.teacher@mail.uk',
           recipient='на адрес urban.student@mail.ru')
send_email(message= 'Нельзя отправить письмо самому себе!', sender='', recipient= '')