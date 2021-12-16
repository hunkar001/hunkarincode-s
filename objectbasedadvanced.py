class Dusman():

    def __init__(self,isim,kalan_can,saldırı_gucu,mermi_sayısı):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldırı_gucu = saldırı_gucu
        self.mermi_sayısı = mermi_sayısı

        
    def print(self):
        print("basılıyorrr..")
        print("isim:",self.isim,"kalan can: ",self.kalan_can,"saldırı gücü: ",self.saldırı_gucu,"mermi sayısı: ",self.mermi_sayısı)
    
dusman1 = Dusman("hünkar",1500,100,200)
dusman2 = Dusman("eylül",2000,200,300)

print("düsman1-------------")
dusman1.print()

print("düsman2-------------")
dusman2.print()