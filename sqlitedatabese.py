import sqlite3

con = sqlite3.connect("notlar.db")
cursor=con.cursor()

def tablooluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT, soyad TEXT, numara INT, ogrencınotu INT)")
    


def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('Emre','demir',211118031,95)")
    con.commit()
    con.close()

def degeral():
    cursor.execute("SELECT * FROM ogrenciler")
    data=cursor.fetchall()
    for i in data:
        print(i)


degeral()
