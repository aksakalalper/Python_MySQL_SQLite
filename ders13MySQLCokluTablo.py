import mysql.connector
import pandas as pd

#baglanti saglanir
conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="373737",  
            database="node-app"  
            )
#fonksiyon tanimlanir
def deleteItem():
    cursor=conn.cursor()
    # update metodu cagirilir %s verileri disaridan alinir.
    query="SELECT * FROM  categories"
    # disaridan alinan veriler tuple liste haline getirilir.
    try:
        # query uygulanir
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"hata var {err}")
    finally:
        print("blok calisti")
        cursor.close()
        conn.close()

a=deleteItem()