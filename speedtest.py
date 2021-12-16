import speedtest
speed = speedtest.speedtest()


def test():
    
    while True:
        print('\a')
        seçim=int(input("""
    internet bağlantınızı kontrol ediniz...
    1)indirme hızı
    2)yükleme hızı
    3)çıkış
    seçim >>> """))

        print('\a')
     
    

        if seçim == 1 :
            print("test ediliyor...")
            print(f"İndirme hızı : {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s")

        elif seçim == 2 :
            print("Test ediliyor")
            print(f"Yükleme hızı : {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")

        elif seçim == 3 :
            print("Programdan çıkış yapıldı")
            break
        

        else:
            print("Hatalı seçim lütfen tekrar deneyiniz.")
    
test()

     