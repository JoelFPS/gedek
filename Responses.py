from datetime import datetime
import telegram
import cv2
import Constants as keys
import randomizer as Geo
import dbConnector as db

# ---- authorization pending
def auth_photo(update):
    keys.status = 1
    update.message.reply_text("Najpierw podaj magiczne hasło")

# ---- take photo
def take_photo(id,path):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("panel")
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Camera",frame)

        img_name = "opencv_frame_{}.png".format(0)
        cv2.imwrite(img_name, frame)
        break

    cam.release()
    cv2.destroyAllWindows()

    sendPhoto(id,path)

# ---- send photo
def sendPhoto(id,path):
    TELEGRAM_BOT_TOKEN = keys.API_KEY
    TELEGRAM_CHAT_ID = id
    PHOTO_PATH = path

    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))

# ---- new game Geo
def newGeo(update,nope):
    if nope==0:
        update.message.reply_text("nie")
    id = update.message.chat.id

    name = Geo.selectRectangles()
    result = db.chooseCoordinates(name)
    
    maxlat = result[0]
    maxlong = result[1]
    minlat = result[2]
    minlong = result[3]
    
    loc_random = Geo.randomizeCoordinates(maxlat,maxlong,minlat,minlong)
    loc_name = Geo.downPhoto(loc_random)
    if loc_name == "error":
        newGeo(update,0)
    else:
        loc_photo = Geo.searchCity(loc_name[0],loc_name[1])
        if loc_photo == "error":
            newGeo(update,0)
        else:
            keys.loc_photo = loc_photo
            sendPhoto(id,'GeoImage.jpg')
            update.message.reply_text("Zgadujemy wg wzoru: państwo, miasto")

# ---- operations durning the Geo
def TemporaryGeo(name, country, city):
    keys.user_nr += 1
    nr = keys.user_nr
    if city=="x":
        loc_user = Geo.searchCountry(country)
        if loc_user == "error":
            keys.user_nr -= 1
            return "error"
    else: 
        loc_user = Geo.searchCity(country,city)
        if loc_user == "error":
            keys.user_nr -= 1
            return "error"
    db.saveTemporaryGeo(nr, name, loc_user)

# ---- end Geo
def endGeo(update):
    guesses = db.chooseTemporaryGeo(keys.user_nr)
    results = []
    emoticons = ['🥇','🥈','🥉','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
    scoreboard = "Zdjęcie zostało zrobione w: "+keys.photo_name[0]+", "+keys.photo_name[1]+"\n"
    for i in range(0,keys.user_nr):
        distance = Geo.measureDistance(keys.loc_photo,guesses[i][2])
        name = guesses[i][1]
        results.append([distance, name])
    results.sort()
    for i in range(0,keys.user_nr):
        a = str(results[i][1])
        b = str(results[i][0])
        c = str(i+1)
        if i < 10:
            scoreboard += emoticons[i]+" "+a+" | "+b+"km\n"
        else:
            scoreboard += c+" "+a+" | "+b+"km\n"
    update.message.reply_text("Oto wyniki:\n"+scoreboard)

    keys.user_nr = 0
    keys.loc_photo = ''

# ---- interaction with user
def sample_responses(input_text, update):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi","siemka","elo","hej","cześć"):
        return "Hej! Co tam?"

    if user_message in ("jak leci"):
        return "Hej! Co tam?"

    if user_message in ("co?","co"):
        return "Nie wiem... Jak leci?"

    if user_message in ("dobrze","fajnie","spoko","świetnie","wybornie","bardzo dobrze"):
        return "To elegancko 👍"

    if user_message in ("who are you", "who are you?", "kto ty jesteś", "kto ty jesteś?", "kim jesteś?"):
        return "Jestem botem praktykanta! :D"

    if user_message in ("lubisz mnie?"):
        return "Jeszcze się pytasz!? :D"

    if user_message in ("ziomuś","gedek"):
        return "Tak?"

    if user_message in ("date","data"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("time","clock","czas","godzina","godz","która godzina?","jaki czas?"):
        now = datetime.now()
        date_time = now.strftime("%H:%M:%S")
        return str(date_time)

    if user_message in ("cyknij fotke","kto jest w moim pokoju?"):
        return auth_photo(update)

    if user_message in ("losuj"):
        keys.status = 3
        return newGeo(update,1)

    return "no_instructions"
