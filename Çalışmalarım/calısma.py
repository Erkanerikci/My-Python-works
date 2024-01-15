class Insan:
    def __init__(self,ad,soyad,sınıf,okul):
        self.ad = ad
        self.soyad = soyad
        self.sınıf = sınıf
        self.okul = okul
insan1 = Insan("Erkan","Erikci","Bilgisayar","KÜ")
print(f'Ad = {insan1.ad} Soyad = {insan1.soyad} Sınıf = {insan1.sınıf} Okul = {insan1.okul}')