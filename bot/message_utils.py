import os
import time
from datetime import datetime
from typing import Optional, Union
from pathlib import Path
import telebot
import pytz

from data_utils.file_utils import save_file, load_file

TOKEN = os.getenv('PAPERPAPER__TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode='MARKDOWN')


def bot_send_message(
    chat_id: Union[int, str],
    text: str,
    parse_mode: Optional[str] = None,
    reply_markup=None,
    entities=None,
    disable_web_page_preview: Optional[bool] = None,
    disable_notification: Optional[bool] = True,
    time_sleep: Union[bool, int] = False,
    pin=False,
):
    """
    Отправляет сообщение в Telegram чат.

    Args:
        chat_id: ID чата.
        text: Текст сообщения.
        parse_mode: Режим форматирования текста.
        reply_markup: Разметка клавиатуры.
        entities: Сущности сообщения.
        disable_web_page_preview: Отключить предпросмотр веб-страниц.
        disable_notification: Отключить уведомления.
        time_sleep: Задержка перед отправкой сообщения.
        pin: Закрепить сообщение после отправки.
    """
    try:
        if time_sleep:
            time.sleep(time_sleep if isinstance(time_sleep, int) else 5)
        message = bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
            entities=entities,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
        )
        if pin:
            time.sleep(1)
            bot.pin_chat_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Exception in bot_send_message: {e}")
        message = None
    return message


def upd_message(chat_id, profile_data_message, profile_data_data, base_traffic=1000, path=None):
    """
    Обновляет сообщение с информацией о VPN трафике.

    Args:
        chat_id: ID чата.
        profile_data_message: Сообщение от сервера.
        profile_data_data: Данные о трафике.
        base_traffic: Базовое значение трафика для расчета.
        path: Путь к файлу для сохранения данных сообщения.
    """
    path = path or f'./data/{chat_id}/messages.json'
    if not Path('urls.json').is_file():
        message_json = bot_send_message(chat_id=chat_id, text='Сообщение для статистики', disable_notification=True,
                                        pin=True).json
        save_file(data=message_json, file_path=path)
    msg_json = load_file(file_path=path)
    upd_info(msg_json, profile_data_message, profile_data_data, base_traffic)


def upd_info(msg_json, profile_data_message, profile_data_data, base_traffic=1000):
    """
    Обновляет информацию в сообщении.

    Args:
        msg_json: JSON данные текущего сообщения.
        profile_data_message: Сообщение от сервера.
        profile_data_data: Данные о трафике.
        base_traffic: Базовое значение трафика для расчета.
    """
    datetime_now = datetime.now().astimezone(pytz.timezone('Europe/Moscow'))
    text = (f"Осталось месячного трафика VPN, по состоянию на `{datetime_now.strftime('%H:%M:%S %Y-%m-%d')}` по Москве:"
            f" {profile_data_message}\n{profile_data_data}")

    if 'amount' in profile_data_data and profile_data_data['amount']:
        text_markup = f"{(int(profile_data_data['amount']) / base_traffic * 1000)/10} [%]"
    else:
        text_markup = f"? [%]"
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text=text_markup, url='https://t.me/ProSkidkuru'))

    try:
        bot.edit_message_text(text=text, chat_id=msg_json['chat']['id'], message_id=msg_json['message_id'],
                              reply_markup=markup)
    except Exception as e:
        print(f"Exception in upd_info: {e}")
