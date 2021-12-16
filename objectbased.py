
class Dusman():
    kalan_can = 3
    def saldır(self):
        print("hucümmmm")
        self.kalan_can -= 1

    def hayatta_mi(self):
        if self.kalan_can <= 0 :
            print("öldü.")
        else:
            print(str(self.kalan_can) + " canım kaldı")

dusman1 = Dusman()

dusman1.saldır()
dusman1.saldır()
dusman1.hayatta_mi()
        

