import mysql.connector
import pandas as pd

#baglanti saglanir
conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="373737",  
            database="phonedata"  
            )
#fonksiyon tanimlanir
def getUpdate(User_ID,Device_Model):
    cursor=conn.cursor()
    # update metodu cagirilir %s verileri disaridan alinir.
    query="UPDATE users SET Device_Model=%s WHERE User_ID=%s"
    # disaridan alinan veriler tuple liste haline getirilir.
    values=(Device_Model,User_ID)
    try:
        # query uygulanir
        cursor.execute(query,values)
        # degistirilen satir ekrana basilir.
        cursor.execute(f"SELECT * FROM users WHERE User_ID = {User_ID}")
        result2=cursor.fetchone()
        conn.commit()
        print(result2)
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

a=getUpdate(1,'Google Pixel 5')