import mysql.connector
# MySQL veritabanına bağlanma

# Veri ekleme
def insertProduct(name,price,imageURL,description):
    conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='373737' ,
    database='node-app'
    )

    # Bir cursor oluşturma 
    cursor = conn.cursor() 
    sql="INSERT INTO products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values=(name,price,imageURL,description)
    cursor.execute(sql,values)

    try:
        conn.commit()
        print(f"ekleme basarili! son eklenen kayit {cursor.lastrowid}")
    except mysql.connector.error as err:
        print("hatali!")
    finally:
        conn.close()
        print("kapatiliyor")

list=[] 
while True:
    name=input("ürün adı: \n")
    price=input("ürün fiyatı: \n")
    imageURL=input("ürün görseli: \n")
    description=input("ürün tanımı: \n")
    userChoice=input("eklemeye devam mı? e/h ")
    if (userChoice=="h"):
        insertProduct(name=name,price=price,imageURL=imageURL,description=description)
        break
    else:
        insertProduct(name=name,price=price,imageURL=imageURL,description=description)
        continue


