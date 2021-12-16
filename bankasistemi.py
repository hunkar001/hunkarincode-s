#BANKA ATM ÖRNEĞİ
#KARTIN BİR ŞİFRESİ VARDIR.
#KARTIN BAŞLANGIÇTA BAKİYESİ 500 TL DİR.
#3 DEFA YANLIŞ GİRİLİNCE KART BLOKE OLACAKTIR.
#ATM NİN İŞLEM MENÜSÜNDE para çekme, para yatırma, bakiye sorgulama ve kart iade işlemleri yapılacaktır.

kart_sifre=1768
bakıye=500
giris_sayac=3
login= False

while True:

    if login == False :
        şifre=int(input("Lütfen Şifrenizi giriniz: "))
    if şifre == kart_sifre:
            login = True
            print("""
1.Para çekme           
2.Para yatırma           
3.Bakiye sorgulama          
4.Kart İade
            """)

            seçim=int(input("Lütfen bir seçim yapınız: "))
            if seçim == 1 :
                miktar=int(input("Kaç TL çekmek istiyorsunuz: "))
                if bakıye < miktar :
                    print("Yeterli Bakiyeniz bulunmamaktadır")
                    continue
                bakıye -= miktar
            
            elif seçim == 2 :
                yatır=int(input("Hesabınıza kaç TL yatırmak istersiniz?: "))
                bakıye += yatır

            elif seçim == 3 :
                print("BAKİYENİZ {} TL".format(bakıye))
                
            elif seçim == 4 :
                print("Yine bekleriz")
                break
            
            else:
                print("Lütfen 1-4 arasında seçim yapınız.")


    else:
        giris_sayac -= 1
        if giris_sayac <= 0 :
            print("Kartınız Bloke olmuştur.")


                



            
    
