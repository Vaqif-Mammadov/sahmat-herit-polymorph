class Oyun():
    def __init__(self):
        print("Oyun yaradildi")

class Sahmat(Oyun):
    def __init__(self):
        super().__init__()
        self.ad="Şahmat"
        print("Sahmat oyunu yaradildi ve fiqurlar oz yerlerine duzuldu")
        print("Fiqurlarin gedisleri bu curdur")
        
    def nov(self):
        self.nov="Stolustu"
        return self.nov
        
    def oyuncu_sayi(self):
        self.oyuncu_sayi=2
        return self.oyuncu_sayi

    def hereket_diaqonal(self,fiqur):
        self.hereket="diaqonal gedis"
        self.fiqur=fiqur
        if self.fiqur== "Fil" or self.fiqur== "Vezir" or self.fiqur== "Sah":
            return True
        else:
            False

    def hereket_perpendikulyar(self,fiqur):
        self.hereket="perpendikulyar gedis"
        self.fiqur=fiqur
        if self.fiqur=="Top" or self.fiqur=="Vezir" or self.fiqur=="Sah":
            return True
        else:
            False

    def hereket_L_sekilde(self,fiqur):
        self.hereket="L seklinde gedis"
        self.fiqur=fiqur
        if self.fiqur=="At":
            return True
        else:
            False
        
    def vezire_cixmaq(self, fiqur):
        self.hereket="Vezire cixma gedisini"
        self.fiqur=fiqur
        if self.fiqur=="Piyada":
            return True
        else:
            False
    
    def qala_qurmaq(self,fiqur):
        self.hereket="Qala qurma gedisini"
        self.fiqur=fiqur
        if self.fiqur=="Sah":
            return True
        else:
            False
        
    def uzerinden_tullanmaq(self, fiqur):
        self.hereket="Fiqur uzerinden tullanma gedisini"
        self.fiqur=fiqur
        if self.fiqur=="At" or self.fiqur=="Top":
            return True
        else:
            False
        
    def yoxla(self,fiqur):
        self.fiqur=fiqur
        self.result=False

        if self.hereket_diaqonal(self.fiqur):
            self.result=True
        self.last_func(self.result)
        self.result=False
      
        if self.hereket_perpendikulyar(self.fiqur):
            self.result=True
        self.last_func(self.result)
        self.result=False

        if self.hereket_L_sekilde(self.fiqur):
            self.result=True
        self.last_func(self.result)
        self.result=False

        if self.vezire_cixmaq(self.fiqur):
            self.result=True
        self.last_func(self.result)
        self.result=False 

        if self.qala_qurmaq(self.fiqur):
            self.result=True
        self.last_func(self.result)
        self.result=False 

        if self.uzerinden_tullanmaq(self.fiqur):
            self.result=True
        self.last_func(self.result)
        self.result=False 

    def last_func(self,result):
        self.result=result
        if self.result:
            print(f"{self.fiqur} {self.hereket} ede bilir")
        else:
            print(f"{self.fiqur} {self.hereket} ede bilmir")

class Dama(Oyun):
    def __init__(self):
        super().__init__()
        self.ad="Dama"
    
    def nov(self):
        self.nov="Stolustu"
        return self.nov
        
    def oyuncu_sayi(self):
        self.oyuncu_sayi=2
        return self.oyuncu_sayi
        
dama=Dama()
oyun = Sahmat()
#oyun.yoxla("Sah")     #Hansi fiqurun nece hereket etdiyini bilmek ucun metodun icine bir fiqur adi daxil edin :)

def oyuncu(obj1,obj2):
    print("{} oyununun novu {} , oyuncu sayi {}".format(obj1.ad,obj1.nov(),obj1.oyuncu_sayi()))
    print("{} oyununun novu {} , oyuncu sayi {}".format(obj2.ad,obj2.nov(),obj2.oyuncu_sayi()))
    
oyuncu(dama,oyun)