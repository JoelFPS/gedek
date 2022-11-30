import random
from geopy.geocoders import Nominatim
import haversine as hs
import googlemaps
import Constants as keys

# ---- randomize area of world
def selectRectangles():
    number = random.randrange(1,11)
    if number==1:
        selectPolandRectangles()
    else:
        number = random.randrange(1,35)
        match number:
            case 1:
                return 'europa1'
            case 2:
                return 'europa2'
            case 3:
                return 'europa3'
            case 4:
                return 'europa4'
            case 5:
                return 'europa5'
            case 6:
                return 'europa6'
            case 7:
                return 'europa7'
            case 8:
                return 'europa8'
            case 9:
                return 'europa9'
            case 10:
                return 'europa10'
            case 11:
                return 'europa11'
            case 12:
                return 'europa12'
            case 13:
                return 'oceania2' #heh
            case 14:
                return 'amerykaN2'
            case 15:
                return 'amerykaN3'
            case 16:
                return 'amerykaN3'
            case 17:
                return 'amerykaN4'
            case 18:
                return 'amerykaN5'
            case 19:
                return 'amerykaS1'
            case 20:
                return 'amerykaS2'
            case 21:
                return 'amerykaS3'
            case 22:
                return 'amerykaS4'
            case 23:
                return 'azja1'
            case 24:
                return 'azja2'
            case 25:
                return 'azja3'
            case 26:
                return 'azja4'
            case 27:
                return 'azja5'
            case 28:
                return 'azja6'
            case 29:
                return 'afryka1'
            case 30:
                return 'afryka2'
            case 31:
                return 'afryka3'
            case 32:
                return 'afryka4'
            case 33:
                return 'afryka5'
            case 34:
                return 'oceania1'

# ---- randomize area of PL
def selectPolandRectangles():
    number = random.randrange(1,233)
    tab = [[1], [2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232]]

    if number in (tab[0]):
        return 'zakopane'
    if number in (tab[1]):
        return 'szczecin'
    if number in (tab[2]):
        return 'gdansk'
    if number in (tab[3]):
        return 'katowice'
    if number in (tab[4]):
        return 'czestochowa'
    if number in (tab[5]):
        return 'centrum'

# ---- randomize location
def randomizeCoordinates(maxlat,maxlong,minlat,minlong):
    lat = str(round(random.uniform(maxlat,minlat),7))
    long = str(round(random.uniform(maxlong,minlong),7))
    location = lat+", "+long
    return location

# ---- search location of country
def searchCountry(country):
    geolocator = Nominatim(user_agent="GetLoc")
    location = geolocator.geocode(country)
    try:
        lat = str(location.latitude)
    except:
        return "error"
    else:
        long = str(location.longitude)
        loc_user = lat+", "+long
        return loc_user

# ---- wsearch location of city
def searchCity(country,city):
    geolocator = Nominatim(user_agent="GetLoc")
    location = geolocator.geocode(city+','+country)
    try:
        lat = str(location.latitude)
        if lat == None:
            return "error"
    except:
        return "error"
    else:
        long = str(location.longitude)
        loc_user = lat+", "+long
        return loc_user

# ---- distance calculation
def measureDistance(loc_photo,loc_user):
    loc_photo = str(loc_photo)
    loc_user = str(loc_user)
    photo_lat = float(loc_photo[0:loc_photo.index(',')])
    photo_long = float(loc_photo[loc_photo.index(',')+1:])
    user_lat = float(loc_user[0:loc_user.index(',')])
    user_long = float(loc_user[loc_user.index(',')+1:])
    photo = (photo_lat, photo_long)
    user = (user_lat, user_long)
    distance = round(hs.haversine(photo,user),1)
    return distance

# ---- get nearby photo
def downPhoto(loc_random):
    gmaps = googlemaps.Client(key=keys.API_MAPS)
    places_result = gmaps.places_nearby(location=loc_random, radius=40000, open_now = False)
    my_place_id = places_result['results'][0]['place_id']
    my_fields = ['photo']
    places_details = gmaps.place(place_id=my_place_id, fields=my_fields)

    try:
        photo_id = places_details['result']['photos'][0]['photo_reference']
    except:
        return "error"
    else:
        photo_width = 1200
        photo_height = 1200

    raw_image_data = gmaps.places_photo(photo_reference=photo_id, max_width=photo_width,max_height=photo_height)
    f = open('GeoImage.jpg', 'wb')
    for chunk in raw_image_data:
        if chunk:
            f.write(chunk)
    f.close()

    city = places_result['results'][0]['name']
    try:
        compound = str(places_result['results'][1]['plus_code']['compound_code'])
        print("Informacja o kraju:",compound)
    except:
        print("Błąd country")
        return "error"
    else:
        count = compound.count(",")
        try:
            compound.index(",")
        except:
            return "error"
        tab = compound.split(", ")
        country = tab[count]
        loc_name = [country,city]
        keys.photo_name = [country,city]
        return loc_name
