import cv2
#kameramızı açıyoruz
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#casdade dosyaımız yüklüyoruz
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    #kameradan gelen kareleri okuyoruz(iki değişken döndürür.)
    ret , frame = cap.read()

    #kameradan gelen her kareyi y ekseninde çeviriyoruz
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #gri

    #detectmultiscale() fonksiyonuyla her karedeki yüzün koordinatlarını tespit ediyoruz.

    faces = face_cascade.detectMultiScale(gray, 1.3,5)

    for (x,y,w,h) in faces :
        #karemizi çizdiriyoruz
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),thickness= 1)

        text = "yuz algilandi"
        koordinat=(x+w-20,y-20)
        yazı_tipi = cv2.FONT_HERSHEY_DUPLEX
        olcek = 1
        renk = (0,0,255)
        kalınlık = 1

        cv2.putText(frame,text,koordinat,yazı_tipi,olcek,renk,kalınlık)

    cv2.imshow("yüz algılama",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

