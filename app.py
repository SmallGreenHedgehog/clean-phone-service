from typing import Type
from flask import Flask
from preparers_for_phone_number import PhoneNumberPreparer, PhoneNumberPlusSevenNinePreparer

app = Flask(__name__)


def prepare_phone(phone_preparer_class: Type[PhoneNumberPreparer], phone: str):
    """Возвращет подготовленный номер переданным подготовщиком"""
    phone_preparer = phone_preparer_class(phone)
    return phone_preparer.prepared_phone_number


def prepare_russian_phone(phone: str):
    """Возвращет подготовленный номер телефона вида +79998887766"""
    return prepare_phone(phone_preparer_class=PhoneNumberPlusSevenNinePreparer, phone=phone)


@app.route('/api/v1/single-phone/', methods=['GET'])
@app.route('/api/v1/single-phone/<string:phone>', methods=['GET'])
def single_phone_page(phone=''):
    return prepare_russian_phone(phone)


if __name__ == '__main__':
    app.run(debug=False)
