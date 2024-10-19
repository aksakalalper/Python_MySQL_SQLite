import mysql.connector

def getProducts():
    # Veritabanı bağlantısı oluştur
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="373737",
    database="node-app")

    # Bir cursor oluştur
    cursor = conn.cursor()

    # SQL sorgusunu tanımla
    query = "SELECT * FROM product"

    # Sorguyu çalıştır
    cursor.execute(query)

    # Sonuçları al
    result = cursor.fetchall()

    # Sonuçları yazdır
    for product in result:
        print(f"id: {product[0]}, name: {product[1]},price: {product[2]},note: {product[3]},description: {product[4]}")

getProducts()