import Constants as keys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Responses as R
import dbConnector as db
import opt as F
import time

print("Bot started...")

def start_command(update, context):
    update.message.reply_text("Napisz coś do mnie! Użyj /register, żeby dokonać autoryzacji")

def help_command(update, context):
    update.message.reply_text("Jeśli potrzebujesz pomocy wyszukaj to w Google")

def register_command(update, context):
    id = update.message.chat.id
    key = F.createKey()
    db.dbCommitSecret(id, key)
    R.sendPhoto(id,"qr.png")
    update.message.reply_text("Podaj 6-cyfrowy kod")
    keys.status = 2

def stop_command(update, context):
    keys.status = 0
    keys.user_nr = 0
    keys.loc_photo = ''
    keys.photo_name = []
    db.dbClearTable()
    update.message.reply_text("Akcja zatrzymana")
    

def geo_command(update, context):
    keys.status = 0
    update.message.reply_text("Werble 🥁")
    time.sleep(3)
    R.endGeo(update)

def handle_message(update, context):
    text = str(update.message.text).lower()
    id = update.message.chat.id
    if update.message.chat.type == 'group':
        name = update.message.from_user.first_name
    else:
        name = update.message.chat.first_name

    if keys.status==0:
        response = R.sample_responses(text, update)
        if response != "no_instructions":
            update.message.reply_text(response)
    elif keys.status==1: #taking photo
        correct = db.checkPassword(text, id)
        if correct == "True":
            update.message.reply_text("Uśmiech!")
            response = "Pięknie wyszejdłeś!"
            R.take_photo(id,"opencv_frame_0.png")
            keys.status = 0
        else:
            response = "Kod niepoprawny. Spróbuj ponownie lub użyj /stop"
        update.message.reply_text(response)
    elif keys.status==2: #password
        correct = db.checkPassword(text, id)
        if correct == "True":
            response = "Kod poprawny. Autoryzacja przebiegła pomyślnie"
            keys.status = 0
        else: 
            db.dbDeleteSecret(id)
            response = "Kod niepoprawny. Spróbuj ponownie /register"
        update.message.reply_text(response)
    elif keys.status==3: #Geo
        count = text.count(",")
        if count==0:
            output = R.TemporaryGeo(name, text, 'x')
            if output == "error":
                response = "Nie znalazłem takiego miejsca 🫢\nSpróbuj jeszcze raz 😉"
                update.message.reply_text(response)
        else:
            i = text.index(",")
            j = i+1
            country = text[0:i]
            city = text[j:]
            output = R.TemporaryGeo(name, country, city)
            if output == "error":
                response = "Nie znalazłem takiego miejsca 🫢\nSpróbuj jeszcze raz 😉"
                update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("register", register_command))
    dp.add_handler(CommandHandler("stop", stop_command))
    dp.add_handler(CommandHandler("geo", geo_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
