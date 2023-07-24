Öğrenciler = {}

numarası = input("öğrenci numarası: ")
adi = input("öğrenci adi: ")
soyadi = input("öğrenci soyadı: ")
telefon = input("telefon numarası: ")

Öğrenciler[numarası] = { 
    'ad': adi,
    'soyad': soyadi,
    'telefon' : telefon 
}

print(Öğrenciler)  # Burada ise mesela okula bir öğrenci eklersek kullanacağımız liste mantığı...
