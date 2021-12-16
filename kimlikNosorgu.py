def kimlikNosorgu(veri):
    veri = str(veri)  # veriyi stringe döndürüp for döngüsü ile içinde gezinip değerleri çıkardık.
    tümtoplam=0
    kosultüm=0
    tektoplam=0
    cıfttoplam=0
    kosultekcift=0
    kosultsayı=0

    if veri[0] == '0' :
        return False
    
    if not len(veri) == 11 :  # if len(veri) != 11 :  # return false                                               
        return False
    
    if len(veri) == 11 :

        for i in range(0,10):
            a=veri[i]     #veriyi string değerden inte çevirip toplamı elde ettik.
            a=int(a)
            tümtoplam += a
        kosultüm=tümtoplam%10

        for i in range(0,9,2):
            a=veri[i]
            a=int(a)
            tektoplam += a

        for i in range(1,9,2):
            a=veri[i]
            a=int(a)
            cıfttoplam += a

        kosultekcift=(tektoplam*7 + cıfttoplam*9)%10
        kosultsayı=(tektoplam*8)%10

        if kosultüm == int(veri[10]) and kosultekcift == int(veri[9]) and kosultsayı == int(veri[10]) : #indisleri inte çevirip doğru olup olmadığını döndürdük.
            return True 
        return False

veri=int(input("lütfen TC kimlik no giriniz: "))

a=kimlikNosorgu(veri)
print(a)

        


        

        
            
            