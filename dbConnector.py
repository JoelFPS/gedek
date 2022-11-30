import sqlite3
import opt as F

path = 'D:/Joel/web-projects/telegrambot/db.sqlite' #paste your path

# ---- delete rekord from secrets table (manually)
def dbDeleteSecret(id):
    user_id = str(id)
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    sql = "DELETE FROM secrets WHERE user_id=?"
    c.execute(sql, (user_id,))
    conn.commit()
    conn.close()

# ---- delete rekord from area table (manually)
def dbDeleteArea(name):
    area = str(name)
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    sql = "DELETE FROM temp WHERE name=?"
    c.execute(sql, (area,))
    conn.commit()
    conn.close()

# ---- create table (manually)
def dbCreateTable():
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE temp (nr INTEGER, name TEXT, loc TEXT)''')
    conn.commit()
    conn.close()

# ---- add area (manually)
def dbCommitRectangle():
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT INTO areas VALUES ('zakopane','49.72049','20.10782','49.23704','19.83053','pl')")
    c.execute("INSERT INTO areas VALUES ('szczecin','53.92222','15.01951','52.52084','14.47688','pl')")
    c.execute("INSERT INTO areas VALUES ('gdansk','54.71292','18.60021','54.0931','17.0345','pl')")
    c.execute("INSERT INTO areas VALUES ('katowice','50.46885','22.84608','49.71353','18.62568','pl')")
    c.execute("INSERT INTO areas VALUES ('czestochowa','51.01876','23.57213','50.4492','16.45037','pl')")
    c.execute("INSERT INTO areas VALUES ('centrum','54.02958','23.17675','51.01885','15.07484','pl')")
    c.execute("INSERT INTO areas VALUES ('europa1','53.88064','35.9417','46.16049','3.99083','eu')")
    c.execute("INSERT INTO areas VALUES ('europa2','46.69372','28.79369','43.36392','16.00809','eu')")
    c.execute("INSERT INTO areas VALUES ('europa3','43.4586','22.9542','38.60158','20.55337','eu')")
    c.execute("INSERT INTO areas VALUES ('europa4','43.28337','-1.78958','37.02567','-9.41243','eu')")
    c.execute("INSERT INTO areas VALUES ('europa5','49.59724','6.8511','43.35658','-1.37142','eu')")
    c.execute("INSERT INTO areas VALUES ('europa6','62.25643','45.78218','54.78907','21.10023','eu')")
    c.execute("INSERT INTO areas VALUES ('europa7','54.90935','0.81583','50.52735','-3.58079','eu')")
    c.execute("INSERT INTO areas VALUES ('europa8','47.04281','16.0665','16.0665','7.109','eu')")
    c.execute("INSERT INTO areas VALUES ('europa9','43.61851','14.74458','41.77467','10.63583','eu')")
    c.execute("INSERT INTO areas VALUES ('europa10','60.5416','18.48313','58.34824','6.34318','eu')")
    c.execute("INSERT INTO areas VALUES ('europa11','57.00176','13.46039','55.29331','8.75728','eu')")
    c.execute("INSERT INTO areas VALUES ('europa12','54.24897','-6.18339','52.24222','-9.75638','eu')")
    c.execute("INSERT INTO areas VALUES ('amerykaN1','48.79341','-69.07406','42.15773','-124.15535','an')")
    c.execute("INSERT INTO areas VALUES ('amerykaN2','44.77892','-73.14029','36.64543','-122.17622','an')")
    c.execute("INSERT INTO areas VALUES ('amerykaN3','40.53826','-75.46144','31.77491','-118.53299','an')")
    c.execute("INSERT INTO areas VALUES ('amerykaN4','35.58819','-81.20351','26.55981','-109.76957','an')")
    c.execute("INSERT INTO areas VALUES ('amerykaN5','29.29542','-97.11122','17.10379','-103.45138','an')")
    c.execute("INSERT INTO areas VALUES ('amerykaS1','4.93098','-52.9559','-15.72089','-75.00721','as')")
    c.execute("INSERT INTO areas VALUES ('amerykaS2','-17.91902','-61.90757','-50.99074','-73.86381','as')")
    c.execute("INSERT INTO areas VALUES ('amerykaS3','-2.60601','-40.97949','-24.05578','-49.29299','as')")
    c.execute("INSERT INTO areas VALUES ('amerykaS4','-17.51179','-53.98959','-35.20673','-63.02725','as')")
    c.execute("INSERT INTO areas VALUES ('afryka1','7.77058','28.03626','-34.33144','18.44612','af')")
    c.execute("INSERT INTO areas VALUES ('afryka2','7.56379','34.95763','-26.44875','28.54844','af')")
    c.execute("INSERT INTO areas VALUES ('afryka3','31.05727','33.62416','22.68157','29.7933','af')")
    c.execute("INSERT INTO areas VALUES ('afryka4','14.35087','17.66477','5.02175','-12.05295','af')")
    c.execute("INSERT INTO areas VALUES ('afryka5','26.37319','59.70861','21.2448','39.31386','af')")
    c.execute("INSERT INTO areas VALUES ('azja1','52.06996','117.95519','27.07763','54.76615','aj')")
    c.execute("INSERT INTO areas VALUES ('azja2','26.65776','109.42633','21.03664','72.79456','aj')")
    c.execute("INSERT INTO areas VALUES ('azja3','37.12523','140.72051','34.9869','136.52296','aj')")
    c.execute("INSERT INTO areas VALUES ('azja4','42.27005','48.26542','36.6715','27.01616','aj')")
    c.execute("INSERT INTO areas VALUES ('azja5','26.21583','53.69188','28.03731','33.70256','aj')")
    c.execute("INSERT INTO areas VALUES ('azja6','41.3715','129.69612','34.66892','125.58999','aj')")
    c.execute("INSERT INTO areas VALUES ('oceania1','-26.2456','151.34397','-35.65764','138.46871','oc')")
    c.execute("INSERT INTO areas VALUES ('oceania2','-41.86569','173.09705','-43.87483','169.08854','oc')")
    conn.commit()
    conn.close()

# ---- add record
def dbCommitSecret(user_id, secret):
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    data = [user_id, secret]
    c.execute("INSERT INTO secrets VALUES (?,?)",data)
    conn.commit()
    conn.close()

# ---- code validation (2fa)
def checkPassword(text,user_id):
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    sql = "SELECT secret FROM secrets WHERE user_id=?;"
    result = c.execute(sql, (user_id,))
    row = result.fetchone()
    key = str(row[0])
    correct = F.check2fa(key, text)
    conn.close()
    return correct

# ---- get the range of coordinates of area
def chooseCoordinates(name):
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    sql1 = 'SELECT maxlat FROM areas WHERE name=?;'
    sql2 = 'SELECT maxlong FROM areas WHERE name=?;'
    sql3 = 'SELECT minlat FROM areas WHERE name=?;'
    sql4 = 'SELECT minlong FROM areas WHERE name=?;'
    resultTuple = c.execute(sql1, (name,)).fetchone(),c.execute(sql2, (name,)).fetchone(),c.execute(sql3, (name,)).fetchone(),c.execute(sql4, (name,)).fetchone()
    resultList = [list(resultTuple[0]),list(resultTuple[1]),list(resultTuple[2]),list(resultTuple[3])]
    resultStr = [resultList[0][0],resultList[1][0],resultList[2][0],resultList[3][0]]
    result = [float(resultStr[0]),float(resultStr[1]),float(resultStr[2]),float(resultStr[3])]
    return result

# ---- writing to a temporary table
def saveTemporaryGeo(nr, name, loc_user):
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    sql = "INSERT INTO temp VALUES (?,?,?);"
    c.execute(sql, (nr,name,loc_user,))
    conn.commit()
    conn.close()

# ---- get locations provided by users
def chooseTemporaryGeo(nr):
    nr = nr+1
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    result = []
    for i in range(1,nr):
        sql1 = 'SELECT name FROM temp WHERE nr=?;'
        sql2 = 'SELECT loc FROM temp WHERE nr=?;'
        resultTuple = c.execute(sql1, (i,)).fetchone(),c.execute(sql2, (i,)).fetchone()
        resultList = [list(resultTuple[0]),list(resultTuple[1])]
        result.append([i,resultList[0][0],resultList[1][0]])
    c.execute("DELETE FROM temp")
    conn.commit()
    conn.close()
    return result

# ---- clear table (manually)
def dbClearTable():
    conn = sqlite3.connect(path,check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM areas")
    conn.commit()
    conn.close()