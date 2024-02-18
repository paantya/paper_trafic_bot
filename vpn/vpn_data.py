import os
import requests

from datetime import datetime

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


    print(username)
    # Указываем URL для входа
    login_url = 'https://paperpaper.io/wp-login.php'

    # Данные для входа
    login_data = {
        'log': username,  # Имя пользователя или email
        'pwd': password,  # Пароль
        'wp-submit': 'Войти',
        'redirect_to': 'https://paperpaper.io/profile/',  # URL, куда перейти после успешного входа
        'testcookie': '1'
    }

    # Создаем сессию, чтобы сохранять cookies
    session = requests.Session()

    # Отправляем POST-запрос для входа
    response = session.post(login_url, data=login_data)

    # Проверяем успешность входа по URL перенаправления или содержимому страницы
    if response.status_code == 200 and '/profile/' in response.url:
        print("Успешный вход")
        # Получаем содержимое страницы профиля
        profile_response = session.get(f'https://paperpaper.io/api/vpn/traffic/remaining/{user_id}')

        # Декодируем JSON-ответ в словарь Python
        profile_data = profile_response.json()

        profile_data__message = profile_data['message']
        profile_data__data = profile_data['data']
        profile_data__amount = profile_data__data['amount']

        # Печатаем полученные данные
        print("Сообщение:", profile_data__message)
        print("Количество:", profile_data__amount)

        return True, profile_data__message, profile_data__data
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
