import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="373737",  
            database="phonedata"  
            )

# Tüm kayitlari aliniz.
def getAllData():
    cursor=conn.cursor()
    query="SELECT * FROM users"
    cursor.execute(query)
    try:
        result=cursor.fetchall()
        for row in result:
            print(row,"\n")
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

# tüm kullanicilarin sadece device model, operating system ve gender bilgilerini aliniz.
def getDeviceOSGenderData():
    cursor=conn.cursor()
    query="SELECT Device_Model, Operating_System, Gender FROM users"
    cursor.execute(query)
    try:
        result=cursor.fetchall()
        for row in result:
            print(f"Device_Model {row[0]}, Operating_System {row[1]}, Gender {row[2]} \n")
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

# sadece kadin cinsiyetin device model ve operating system bilgilerini getirinziz.
def getFemaleData():
    cursor=conn.cursor()
    query="SELECT Device_Model, Operating_System, Gender FROM users WHERE Gender LIKE '%Female%'"
    cursor.execute(query)
    try:
        result=cursor.fetchall()
        for row in result:
            print(f"Device_Model {row[0]}, Operating_System {row[1]}, Gender {row[2]} \n")
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

# yasi 21 olan kullanicilari getiriniz.
def getAge21Data():
    cursor=conn.cursor()
    query="SELECT * FROM users WHERE Age=21"
    cursor.execute(query)
    try:
        result=cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

# yasi 25 olup iOS kullanan kullanicilari getiriniz.
def getAge25iOSData():
    cursor=conn.cursor()
    query="SELECT * FROM users WHERE Age=25 AND Operating_System LIKE '%iOS%'"
    cursor.execute(query)
    try:
        result=cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

# telefon modeli icinde 'sa' ve 'le' gecen kayitlari aliniz.
def getCharData():
    cursor=conn.cursor()
    query="SELECT * FROM users WHERE Device_Model LIKE '%sa%' OR Device_Model LIKE '%le%' "
    cursor.execute(query)
    try:
        result=cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

# kac adet kadin kullanici vardir.
def getFemaleCountData():
    cursor=conn.cursor()
    query="SELECT * FROM users WHERE Gender LIKE '%Female%' "
    cursor.execute(query)
    try:
        result=cursor.fetchall()
        print(len(result))
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

# kadin kullanicilari telefon kullanma suresine gore siralayiniz.
def sortFemaleData():
    cursor=conn.cursor()
    query="SELECT * FROM users WHERE Gender LIKE '%Female%' ORDER BY App_Usage_Time DESC "
    cursor.execute(query)
    try:
        result=cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

a=sortFemaleData()





