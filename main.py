import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот для заказа услуг. Чтобы узнать прайс, напишите /price. Чтобы оформить заказ, напишите /order.")

@bot.message_handler(commands=["price"])
def price_message(message):
    bot.send_message(message.chat.id, "Прайс наших услуг:\n1. Уборка квартиры - 1000 руб.\n2. Уборка офиса - 1500 руб.\n3. Генеральная уборка - 2000 руб.")

@bot.message_handler(commands=["order"])
def order_message(message):
    bot.send_message(message.chat.id, "Отлично, оформим заказ. Выберите номер услуги из прайса и укажите желаемое время связи с нами в формате 'час:минута'.")

@bot.message_handler(content_types=["text"])
def order_confirm(message):
    service = message.text
    if service not in ["1", "2", "3"]:
        bot.send_message(message.chat.id, "Извините, такой услуги нет в нашем прайсе. Пожалуйста, выберите номер услуги из прайса.")
    else:
        bot.send_message(message.chat.id, "Спасибо за заказ! Мы свяжемся с вами в указанное время.")

bot.polling()