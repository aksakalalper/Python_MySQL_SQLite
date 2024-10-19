import mysql.connector

def get_students():
    # Veritabanı bağlantısı oluştur
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="373737",
        database="node-app"
    )
    # Bir cursor oluştur
    cursor = conn.cursor()

    # Sütundaki öğe sayısını bulur
    query = "SELECT COUNT(*) from product"
    cursor.execute(query)

    # Sonuçları al
    result = cursor.fetchone()

    for product in result:
        print(product)

    # Belirli bir sütundaki öğelerin ortalamasını bulur
    #query = "SELECT AVG(productPrice) from product"
    #query = "SELECT SUM(productPrice) from product"
    #query = "SELECT MIN(productPrice) from product"
    #query = "SELECT MAX(productPrice) from product"
    query="SELECT productName, productPrice from product WHERE productPrice=(SELECT MAX(productPrice) from product)"
    cursor.execute(query)

    # Sonuçları al
    result = cursor.fetchone()

    print(f"{result[0]} {result[1]}")

    # Bağlantıyı kapatma
    cursor.close()
    conn.close()

# Fonksiyonu çağır
get_students()
