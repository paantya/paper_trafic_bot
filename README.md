# Paper Traffic Bot / Бот "Трафик Paper"

---
## Описание проекта / Project Description

**Paper Traffic Bot** is a tool for monitoring the monthly VPN traffic limit usage by "Paper" system users. The bot automatically notifies the user in Telegram about the current state of their VPN traffic.

**Paper Traffic Bot** — это инструмент для мониторинга использования месячного лимита VPN-трафика пользователями системы "Бумага". Бот автоматически уведомляет пользователя в Telegram о текущем состоянии его VPN-трафика.

---
## Установка и запуск / Installation and Launch

### Предварительные требования / Prerequisites:

- Find out your `user_id` in the "Paper" system through the developer tools in your browser.
- Узнайте свой `user_id` в системе "Бумага" через инструменты разработчика в вашем браузере.
<br/>
<br/>

- Create a chat in Telegram and get its `chat_id`.
- Создайте чат в Telegram и получите его `chat_id`.
<br/>
<br/>
 
- Create a Telegram bot through @BotFather and get the `telegram_bot_token`.
- Создайте Telegram-бота через @BotFather и получите `telegram_bot_token`.
<br/>
<br/>

- Add the bot to the created Telegram chat and assign it as an administrator.
- Добавьте бота в созданный чат Telegram и назначьте его администратором.

### Настройка переменных окружения / Setting Environment Variables:

Set the following environment variables on your server or local machine:

На вашем сервере или локальной машине задайте следующие переменные окружения:

```bash
export PAPERPAPER__USERNAME="<login_paper>"
export PAPERPAPER__PASSWORD="<pass_paper>"
export PAPERPAPER__USER_ID="<user_id_paper>"
export PAPERPAPER__CHAT_ID="<telegram_chat_id>"
export PAPERPAPER__TELEGRAM_TOKEN="<telegram_bot_token>"
```

### Запуск Docker контейнера / Running the Docker Container:

```bash
docker run --restart always -v $(pwd):/app --name paper_traffic_bot \
-e PAPERPAPER__USERNAME="$PAPERPAPER__USERNAME" \
-e PAPERPAPER__PASSWORD="$PAPERPAPER__PASSWORD" \
-e PAPERPAPER__USER_ID="$PAPERPAPER__USER_ID" \
-e PAPERPAPER__CHAT_ID="$PAPERPAPER__CHAT_ID" \
-e PAPERPAPER__TELEGRAM_TOKEN="$PAPERPAPER__TELEGRAM_TOKEN" \
python:3.6-slim /bin/sh -c "pip install -r /app/requirements.txt && python /app/run.py"
```

### Настройка автоматического перезапуска / Setting Up Automatic Restart:

Configure a task scheduler (e.g., cron) for regular VPN traffic status checks (recommended every hour).

Настройте планировщик задач (например, cron) для регулярной проверки состояния VPN-трафика (рекомендуется каждый час).


---
## Примеры использования / Usage Examples

The bot will automatically send messages to the specified Telegram chat with up-to-date information about the user's monthly VPN traffic limit.

Бот будет автоматически отправлять сообщения в указанный Telegram-чат с актуальной информацией о месячном лимите VPN-трафика пользователя.


---
## Лицензия / License

This project is distributed under the MIT License. Use, modification, and distribution of the code are allowed provided that authorship is credited.

Проект распространяется под лицензией MIT. Использование, модификация и распространение кода разрешены при условии указания авторства. 

<br/>

Additionally, if you plan to use this code in your projects, please keep the author informed about such use. This is not a mandatory condition, but it will be highly appreciated and will allow the author to learn about interesting applications of the project.

Дополнительно, если вы планируете использовать данный код в своих проектах, пожалуйста, держите автора в курсе о таком использовании. Это не является обязательным условием, но будет высоко цениться и позволит автору узнать о интересных применениях проекта.

---
