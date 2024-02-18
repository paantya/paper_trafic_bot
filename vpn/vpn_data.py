import os
from datetime import datetime
import requests

from data_utils.file_utils import save_file

# Получение данных окружения
username = os.getenv('PAPERPAPER__USERNAME')
password = os.getenv('PAPERPAPER__PASSWORD')
user_id = os.getenv('PAPERPAPER__USER_ID')
print(f"username: {username}")
print(f"password: {password}")
print(f"user_id: {user_id}")


def get_paper_vpn_data():
    """
    Аутентифицирует пользователя и получает данные о VPN трафике.

    Возвращает кортеж, содержащий статус операции, сообщение от сервера и данные о трафике.
    """
    login_url = 'https://paperpaper.io/wp-login.php'
    login_data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Войти',
        'redirect_to': 'https://paperpaper.io/profile/',
    }

    session = requests.Session()
    response = session.post(login_url, data=login_data)

    if response.status_code == 200 and '/profile/' in response.url:
        print("Успешный вход")
        profile_response = session.get(f'https://paperpaper.io/api/vpn/traffic/remaining/{user_id}')
        profile_data = profile_response.json()

        return True, profile_data.get('message'), profile_data.get('data')
    else:
        print("Ошибка входа")
        return False, None, None


def save_vpn_data(chat_id, profile_data_message, profile_data_data):
    """
    Сохраняет данные о VPN трафике в файл.

    Args:
        chat_id (str): Идентификатор чата для пути сохранения.
        profile_data_message (str): Сообщение от сервера.
        profile_data_data (dict): Данные о трафике.
    """
    now = datetime.now()
    file_path = f"./data/{chat_id}/{now.strftime('%Y/%m/%d/%H.txt')}"
    data_to_save = {
        'profile_data_message': profile_data_message,
        'profile_data_data': profile_data_data,
    }
    save_file(data=data_to_save, file_path=file_path)
