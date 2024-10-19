import mysql.connector
from datetime import datetime

# Veritabanı bağlantısı oluştur
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="373737",
    database="schooldb"
)

# Bir cursor oluştur
cursor = conn.cursor()

class Student:
    def __init__(self,studentNumber,studentName,studentSurname,studentBirtdate,studentGender):
        self.studentNumber=studentNumber
        self.studentName=studentName
        self.studentSurname=studentSurname
        self.studentBirtdate=studentBirtdate
        self.studentGender=studentGender
        self.studentBirtdateTime=datetime.strptime(self.studentBirtdate, '%m/%d/%Y')


    def insertStudent(self):
        sql = "INSERT INTO student (studentNumber, studentName, studentSurname, studentBirthdate, studentGender) VALUES (%s, %s, %s, %s, %s)"
        # Veri ekleme
        values = [
        self.studentNumber, self.studentName, self.studentSurname,self.studentBirtdateTime, self.studentGender
        ]       
        cursor.execute(sql, values)

# Veritabanına değişiklikleri kaydetme
while True:
    userChoice=input("eklemek icin e/h\n")
    number=input("ogrenci no: \n")
    name=input("ogrenci adi: \n")
    surname=input("ogrenci soyadi: \n")
    birthdate=input("ogrenci dogum tarihi(ay/gun/yil): \n")
    gender=input("ogrenci cinsiyeti(e/k): \n")
    student=Student(studentNumber=number,studentName=name,studentSurname=surname,studentBirtdate=birthdate,studentGender=gender)
    
    try:
        if(userChoice=="e"):
            student.insertStudent()
            conn.commit()
            print(f"eklenen kayif sayisi: {cursor.rowcount}")
            continue
    
    except mysql.ConnectionError as err:
        print("hata var!")
        break
        
    except (userChoice=="h"):
        break
    
    finally:
        print("islem gerceklesti.")
        # Bağlantıyı kapatma
        cursor.close()
        conn.close()




