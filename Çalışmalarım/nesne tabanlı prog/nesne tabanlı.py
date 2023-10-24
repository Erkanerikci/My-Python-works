# liste = [1,5,3,6]

# sonuç = type(liste)#Type hangi class'a ait olduğunu hangi sınıfa ait olduğunu gösterir.

# print(sonuç)

class Insan:
       #Pass ile yer tutucu olarak kullanabiliriz.

    def __init__(self,ad,yas):#init methodu ise bir değer girdiğimiz zaman çalışan methottur.
        self.ad = ad
        self.yas = yas
        print('init methodu çalıştı.')

    def yashesabı(self):
        return 2023 - self.yas

    
a1 = Insan('Erkan',2004)
print(f'ad:  {a1.ad}  year:  {a1.yas}  yaşı: {a1.yashesabı()}')
print(type(a1))

#---init özelliği ile matematiksel hesaplamalar.
class Mat:
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesaplama(self):
        return 2*self.pi + self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    
a1 = Mat(5)
print(f'a1 : alan = {a1.alan_hesapla()} çevre = {a1.cevre_hesaplama()}')