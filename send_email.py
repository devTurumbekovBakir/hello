def send_mail(text, address, title):
    message = text.format()
    return message + address + title
