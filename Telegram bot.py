import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Функция, которая будет вызываться при команде /start
def start(update, context):
    update.message.reply_text("Привет! Я бот поиска вакансий. Пожалуйста, введите желаемую специальность.")

# Функция, которая будет вызываться при получении сообщения от пользователя
def search_jobs(update, context):
    job_title = update.message.text
    url = f"https://api.example.com/jobs?title={job_title}"  # Подставьте ваш API URL для поиска вакансий
    response = requests.get(url)
    if response.status_code == 200:
        jobs = response.json()
        if jobs:
            update.message.reply_text("Вот некоторые вакансии по вашему запросу:")
            for job in jobs:
                update.message.reply_text(f"- {job['title']}: {job['description']}")
        else:
            update.message.reply_text("По вашему запросу вакансий не найдено.")
    else:
        update.message.reply_text("Произошла ошибка при обращении к серверу.")

# Основная функция, запускающая бота
def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)  # Замените YOUR_BOT_TOKEN на токен вашего бота
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_jobs))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
