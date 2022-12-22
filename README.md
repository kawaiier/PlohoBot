# PlohoBot
Бот для канала *⚡️Подслушано Ploho bar*

# Как запустить у себя
## venv
[Настройте и активируйте](https://docs.python.org/3/library/venv.html) venv в папке проекта

## Зависимости
Установите зависимости

`python3 -m pip install -r requirements.txt`

## .env
Создайте в папке проекта файл `.env` с переменными
- TOKEN — токен бота
- DESTINATION_CHANNEL — **id канала**, в который нужно публиковать посты из бота
- GATEWAY_ACCOUNT_TAG — **тег канала**, в который будут публиковаться посты из бота

## Запускайте бота и наслаждайтесь
`python3 ploho_bot.py`
