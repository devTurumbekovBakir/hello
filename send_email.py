def send_mail(text, address, title):
    message = text.format()
    return message + address + title


def get_address(filepath):
    with open(filepath, 'r') as f:
        return f.read()
