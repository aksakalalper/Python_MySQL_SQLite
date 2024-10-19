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

    # SQL sorgusunu tanımla ve çalıştır (yaşa göre azalan sırayla ve notu 'A' olan öğrenciler)
    query = "SELECT * FROM students WHERE grade = 'A' ORDER BY age DESC"
    
    cursor.execute(query)

    # Sonuçları al
    result = cursor.fetchall()

    # Sonuçları yazdır
    for student in result:
        print(student)

    # Bağlantıyı kapatma
    cursor.close()
    conn.close()

# Fonksiyonu çağır
get_students()
