import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

'''
Key Features:

User ID: Unique identifier for each user.
Device Model: Model of the user's smartphone.
Operating System: The OS of the device (iOS or Android).
App Usage Time: Daily time spent on mobile applications, measured in minutes.
Screen On Time: Average hours per day the screen is active.
Battery Drain: Daily battery consumption in mAh.
Number of Apps Installed: Total apps available on the device.
Data Usage: Daily mobile data consumption in megabytes.
Age: Age of the user.
Gender: Gender of the user (Male or Female).
User Behavior Class: Classification of user behavior based on usage patterns (1 to 5).'''

class Phone:
    def __init__(self):
        try:
            # database bağlantısı sağlanır
            self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="373737",  
            database="phonedata"  
            )
            print("Veritabanına başarıyla bağlanıldı.")
            self.cursor=self.conn.cursor()
        except mysql.connector.Error as err:
            # bağlantı hatası olursa çıkar.
            print(f"Veritabanı bağlantı hatası: {err}")
            exit()
            
    def readValues(self):
            # SQL sorgusunu tanımla
            query = "SELECT * FROM users"
            # Sorguyu çalıştır
            self.cursor.execute(query)
            # Sonuçları al
            results = self.cursor.fetchall()
            # Sonuçları yazdır
            for row in results:
                print(f"User_ID {row[0]}, Device_Model {row[1]}, Operating_System {row[2]}, App_Usage_Time {row[3]}, Screen_On_Time {row[4]}, Battery_Drain {row[5]}, Number_of_Apps_Installed {row[6]}, Data_Usage {row[7]}, Age {row[8]}, Gender {row[9]}, User_Behavior_Class {row[10]} \n")              
            
            # mysql tablosu dataframe olarak çıktı alınır.
            dataframe=pd.read_sql(query,self.conn)    
            print(dataframe)

    def addValues(self,user_id, device_model, operating_system, app_usage_time,
              screen_on_time, battery_drain, number_of_apps_installed,
              data_usage, age, gender, user_behavior_class):
        # girişte alınan değerler liste içine alınır.
        valuesList=(user_id, device_model, operating_system, app_usage_time,
              screen_on_time, battery_drain, number_of_apps_installed,
              data_usage, age, gender, user_behavior_class)
        # sql sorgusu oluşturulur.
        sql = """INSERT INTO users (User_ID, Device_Model, Operating_System, 
         App_Usage_Time, Screen_On_Time, Battery_Drain, 
         Number_of_Apps_Installed, Data_Usage, Age, 
         Gender, User_Behavior_Class) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # DataFrame'deki verileri MySQL'e ekleme
        self.cursor.execute(sql, valuesList)
        self.conn.commit()
        #işlem sonunda çıkış yapılır.
        self.cursor.close()
        self.conn.close()
        
    def deleteValues(self):
        # veri silme için sorgu oluşturulur.
        sql = "DELETE FROM users"
        # Verileri silme
        self.cursor.execute(sql)
        self.conn.commit()  # Değişiklikleri kaydet
        self.cursor.close()
        self.conn.close()
        print("Tüm veriler başarıyla silindi!")

    def writeValues(self):
        #veri tabanı okunur.
        file="phonedata.csv"
        df=pd.read_csv(file)
        #DataFrame'deki her satırı tuple olarak listeye çevirme
        values_list = [tuple(x) for x in df.to_numpy()]
        # SQL sorgusu
        sql = """INSERT INTO users (User_ID, Device_Model, Operating_System, 
         App_Usage_Time, Screen_On_Time, Battery_Drain, 
         Number_of_Apps_Installed, Data_Usage, Age, 
         Gender, User_Behavior_Class) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # DataFrame'deki verileri MySQL'e ekleme
        self.cursor.executemany(sql, values_list)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    
    def averageValues(self):
        sql="SELECT AVG(App_Usage_Time),AVG(Screen_On_time),AVG(Battery_Drain),AVG(Number_of_Apps_Installed),AVG(Data_Usage), AVG(Age),AVG(User_Behavior_Class) from users"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(f"App_Usage_Time {result[0]}, screen_on_time {result[1]},Battery_Drain {result[2]}, Number_of_Apps_Installed {result[3]}, Data_Usage {result[4]}, Age {result[5]},User_Behavior_Class {result[6]}")
        self.cursor.close()
        self.conn.close()
    
    def dataAnalysis(self):
        sql = "SELECT * FROM users WHERE Operating_System LIKE '%Android%' "
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        androidCount=len(result)
        sql = "SELECT * FROM users WHERE Operating_System LIKE '%iOs%' "
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        iOSCount=len(result)
        print(androidCount,iOSCount)
        dataTypes="android","iOS"
        counts=[androidCount,iOSCount]
        colors=["blue","red"]
        plt.subplot(1, 2, 1)
        plt.pie(counts,labels=dataTypes,colors=colors,autopct='%1.0f%%')
        plt.title('Kullanıcı Dağılımı')
        # Bar grafiği
        sql_android = "SELECT AVG(Screen_On_Time) FROM users WHERE Operating_System LIKE '%Android%'"
        self.cursor.execute(sql_android)
        avg_android = self.cursor.fetchone()[0]
        # iOS kullanıcılarının ortalama ekran süresini almak için SQL sorgusu
        sql_ios = "SELECT AVG(Screen_On_Time) FROM users WHERE Operating_System LIKE '%iOs%'"
        self.cursor.execute(sql_ios)
        avg_ios = self.cursor.fetchone()[0]
        # Verileri grafik için hazırlama
        operating_systems = ['Android', 'iOS']
        average_screen_times = [avg_android, avg_ios]
        # Çubuk grafiği oluşturma
        plt.subplot(1, 2, 2)
        plt.bar(operating_systems, average_screen_times, color=['blue', 'red'], alpha=0.7)
        # Başlık ve etiketler
        plt.title('Ortalama Ekran Süreleri')
        plt.xlabel('İşletim Sistemi')
        plt.ylabel('Ortalama Ekran Süresi (Saat)')
    # Değerleri grafik üzerinde gösterme
        for i, v in enumerate(average_screen_times):
            plt.text(i, v + 0.05, f"{v:.2f}", ha='center', va='bottom')  # Değerleri yazdır
    # Grafiği göster
        plt.tight_layout()
        plt.show()
    # Bağlantıyı kapatma
        self.cursor.close()
        self.conn.close()

    def closeConnection(self):
        # Bağlantıyı kapatma
        self.cursor.close()
        self.conn.close()
        print("Veritabanı bağlantısı kapatıldı.")
        exit()

while True:
    # Kullanıcıdan veri girişi
    userChoice=input("islem seciniz:\n1-Verileri ekle\n2-Verileri oku\n3-Verileri yaz\n4-Verileri sil\n5-Baglantiyi kopart\n6-Ortalama getir\n7-Analiz yap\n")
    if(userChoice=="1"):
        try:
            user_id = int(input("User ID (int): "))
            device_model = input("Device Model: ")
            operating_system = input("Operating System: ")
            app_usage_time = int(input("App Usage Time (min/day): "))
            screen_on_time = float(input("Screen On Time (hours/day): "))
            battery_drain = int(input("Battery Drain (mAh/day): "))
            number_of_apps_installed = int(input("Number of Apps Installed: "))
            data_usage = int(input("Data Usage (MB/day): "))
            age = int(input("Age: "))
            gender = input("Gender (Male/Female/Other): ")
            user_behavior_class = int(input("User Behavior Class (int): "))
            values = (user_id, device_model, operating_system, app_usage_time,
              screen_on_time, battery_drain, number_of_apps_installed,
              data_usage, age, gender, user_behavior_class)
            result=Phone()
            result.addValues(user_id, device_model, operating_system, app_usage_time,
              screen_on_time, battery_drain, number_of_apps_installed,
              data_usage, age, gender, user_behavior_class)
            another_entry = input("Başka bir islem yapmak ister misiniz? (E/H): ")
            if (another_entry.lower() != 'e'):
                break
            continue
        except mysql.connector.Error as err:
            print(f"{err}")
            break
        finally:
            print("blok calisti")
    elif(userChoice=="2"):
        result=Phone()
        result.readValues()
    elif(userChoice=="3"):
        result=Phone()
        result.writeValues()
    elif(userChoice=="4"):
        result=Phone()
        result.deleteValues()
    elif(userChoice=="5"):
        result=Phone()
        result.closeConnection()
    elif(userChoice=="6"):
        result=Phone()
        result.averageValues()    
    elif(userChoice=="7"):
        result=Phone()
        result.dataAnalysis()   
    else:
        print("hatali giris")
    
