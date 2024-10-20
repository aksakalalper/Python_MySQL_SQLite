import pandas as pd
import mysql.connector

# CSV dosyasını okuyun
file = "studentData.csv"  # Dosya adını uygun şekilde değiştirin
df = pd.read_csv(file)

# Veritabanına bağlanma
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="373737",
    database="studentData"
)

cursor = conn.cursor()

# DataFrame'deki her satırı tuple olarak listeye çevirme
values_list = [tuple(x) for x in df.to_numpy()]

# SQL sorgusu
sql = """INSERT INTO students (Hours_Studied, Attendance, Parental_Involvement, 
         Access_to_Resources, Extracurricular_Activities, Sleep_Hours, Previous_Scores, 
         Motivation_Level, Internet_Access, Tutoring_Sessions, Family_Income, 
         Teacher_Quality, School_Type, Peer_Influence, Physical_Activity, 
         Learning_Disabilities, Parental_Education_Level, Distance_from_Home, 
         Gender, Exam_Score) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# DataFrame'deki verileri MySQL'e ekleme
try:
    cursor.executemany(sql, values_list)
    conn.commit()
    print("DataFrame başarıyla MySQL veritabanına aktarıldı!")
except mysql.connector.Error as err:
    print(f"Hata: {err}")

# Bağlantıyı kapatma
cursor.close()
conn.close()
