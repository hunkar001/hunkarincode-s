import random       

class Dusman():

    def __init__(self,isim,kalan_can,saldırı_gucu,mermi_sayısı):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldırı_gucu = saldırı_gucu
        self.mermi_sayısı = mermi_sayısı
    
    def saldır(self):
        print(self.isim + " saldırıyor..")
        harcanan_mermi = random.randrange(0,15)
        print(str(harcanan_mermi) + " kadar harcandı" )
        self.mermi_sayısı -= harcanan_mermi

        return(harcanan_mermi,self.mermi_sayısı)

    def saldırıyaugra(self,harcanan_mermi,saldırı_gucu):
        print(self.isim," vuruldummm")
        self.kalan_can -= (harcanan_mermi*saldırı_gucu)

    def mermi_bitti_mi(self):
        if self.mermi_sayısı <= 0 :
            print(self.isim + " konuşuyor: Mermim bitti. ")
            return True
        return False

    def hayata_mı(self):
        if self.kalan_can <= 0 :
            print(self.isim + " ölüyorr")

    def print(self):
        print("isim: ",self.isim,"Kalan Can: ",self.kalan_can,"Saldırı Gücü: ",self.saldırı_gucu,"Mermi Sayısı: ",self.mermi_sayısı)

dusmanlar = []

i=0
while i<10 :
    rastegelecan=random.randrange(200,400)
    rastgelesaldırıgücü=random.randrange(40,60)
    rastgelemermisayısı=random.randrange(90,120)
    neweneym=Dusman("DÜŞMAN"+ str(i+1),rastegelecan,rastgelesaldırıgücü,rastgelemermisayısı)
    dusmanlar.append(neweneym)
    i += 1
for dusman in dusmanlar:
    dusman.print()

i=0
while i<3 :
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)

    donendeger = dusmanlar[randomdusman1].saldır()

    dusmanlar[randomdusman2].saldırıyaugra(donendeger[0],donendeger[1])

    print("round bitti")
    i += 1




        

    
