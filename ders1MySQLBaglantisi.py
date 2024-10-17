import mysql.connector #sql connector kutuphanesi import edilir.

#database baglanmak icin gerekli parametreler gonderilir.
myDB=mysql.connector.connect(
    host="localhost", #bu yerel veri tabanıdır. eğer server olursa 192.154.... şeklinde bir adrese bağlanılır.
    user="root",
    password="373737",
    database="mydatabase" #secili database icinde olusturuldu.
)

myCursor=myDB.cursor() #isaretci olusturuldu.
myCursor.execute("CREATE DATABASE mydatabase") #database olusturur.
myCursor.execute("SHOW DATABASES") #olusturulan databaseleri goruntuler.
for x in myCursor:
    print(x)

myCursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") #
