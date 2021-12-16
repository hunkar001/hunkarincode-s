import sqlite3
import random
import time
import datetime

con = sqlite3.connect("dersler.db")
cursor = con.cursor()

def  tablooluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1(zaman REAL, tarih TEXT, anahtarkelime TEXT, deger REAL)")


def rastgeledegerekle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%y-%m-%d %H:%M:%S'))
    anahtarkelime="python sqlite3"
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger) VALUES (?,?,?,?)",(zaman,tarih,anahtarkelime,deger))

    con.commit()

tablooluştur()

i=0
while i<10 :
    rastgeledegerekle()
    time.sleep(1)
    i += 1

con.close
