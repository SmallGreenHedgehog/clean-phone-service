from typing import Type

from os import getcwd
from os.path import abspath

from flask import Flask
from flask import request

from file_managers import FileManager
from preparers_for_phone_number import PhoneNumberPreparer, PhoneNumberPlusSevenNinePreparer

app = Flask(__name__)

tmp_req_file_path = abspath(getcwd() + '/data/tmp_req.txt')


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
    """Возвращает подготовленный номер телефона на базе переданного"""
    return prepare_russian_phone(phone)


@app.route('/api/v1/echo-request/', methods=['POST'])
def echo_request_page():
    """Возвращает данные запроса, отладочная страница"""
    request_data = request.data
    file_manager = FileManager(tmp_req_file_path)
    file_manager.erase_file()
    file_manager.write_text_to_file(str(request_data.decode("utf-8")))
    return request_data


@app.route('/api/v1/last-request/', methods=['GET'])
def last_request_page():
    """Возвращает данные последнего запроса"""
    # TODO добавить проверку токена, переделать работу с файлом на работу с redis
    return FileManager(tmp_req_file_path).file_text


if __name__ == '__main__':
    app.run(debug=False)
