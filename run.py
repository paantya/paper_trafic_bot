import os

from bot.message_utils import upd_message
from vpn.vpn_data import get_paper_vpn_data, save_vpn_data

chat_id = os.getenv('PAPERPAPER__CHAT_ID')


def main():
    """
    Основная функция для получения данных о VPN трафике и обновления сообщений.
    """
    is_get_ok, profile_data_message, profile_data_data = get_paper_vpn_data()

    print(f"chat_id: {chat_id}")
    if is_get_ok:
        save_vpn_data(chat_id, profile_data_message, profile_data_data)
        upd_message(chat_id, profile_data_message, profile_data_data, base_traffic=1000)
    else:
        print("ERROR!!!")


if __name__ == '__main__':
    main()
