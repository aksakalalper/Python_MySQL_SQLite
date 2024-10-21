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
def deleteItem(User_ID):
    cursor=conn.cursor()
    # update metodu cagirilir %s verileri disaridan alinir.
    query="DELETE FROM  users WHERE User_ID=%s"
    # disaridan alinan veriler tuple liste haline getirilir.
    values=(User_ID,)
    try:
        # query uygulanir
        cursor.execute(query,values)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

a=deleteItem(1)