from app.internal import whatsapp


def test_whatsapp_send():
    # Redirects you directly to the specified contact and the message will
    #  already be there (or to whatsapp web if the call is from the web)
    phone_number = "972536106106"
    message = 'Event or a joke or the schedule of one day'
    assert whatsapp.make_link(phone_number, message) == 'https%3A%2F%2F'\
        'api.whatsapp.com%2Fsend%3Fphone=972536106106&text=Event+or+a+'\
        'joke+or+the+schedule+of+one+day'


def test_wrong_phone_number():
    # Redirects you to a popup: The phone number shared via a link is incorrect
    phone_number = "999999"
    message = 'Wrong phone number?'
    assert whatsapp.make_link(phone_number, message) == 'https%3A%2F%2F'\
        'api.whatsapp.com%2Fsend%3Fphone=999999&text=Wrong+phone+number%3F'


def test_no_message():
    # Redirects to whatsapp of the specified number. Write your own message.
    phone_number = "972536106106"
    message = ''
    assert whatsapp.make_link(phone_number, message) == 'https%3A%2F%2F'\
        'api.whatsapp.com%2Fsend%3Fphone=972536106106&text='


def test_no_number():
    # Redirects to whatsapp window. Choose someone from your own contact list.
    phone_number = ""
    message = 'Which phone number?'
    assert whatsapp.make_link(phone_number, message) == 'https%3A%2F%2F'\
        'api.whatsapp.com%2Fsend%3Fphone=&text=Which+phone+number%3F'
