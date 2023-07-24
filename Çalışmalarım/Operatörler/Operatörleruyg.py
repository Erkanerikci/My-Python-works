
# 1- Girilen bir sayinin 0-100 arasinda olup olmadigina kontrol ediniz.
sayi = int(input("Herhangi bir sayi giriniz."))
if sayi <= 100:
    print("Girilen sayi 0-100 arasındadır.")
else:
    print("Girilen sayi 0-100 arasında değidir.")

# 2- Girilen bir sayinin pozitif cift say olup olmadigani kontrol ediniz.
sayi = float(input("Herhangi bir sayi giriniz."))
if sayi %2 == 0 and sayi >0 :
    print("Girilen sayi pozitif cift sayidir")    
else:
    print("Girilen sayi pozitif cift sayi değildiir")  
# 3- Email ve parola bilgileri ile giris kontrolü yapiniz.
email = 'erkanerikci5489@gmail.com'
sifre = 'asd123123'

girilenemail = input("E-maili giriniz.")
girilensifre = input("Şifrenizi giriniz.")

if email == girilenemail and sifre == girilensifre:
    print("Başarıyla giriş yaptınız.")
else:
    print("E-mailiniz veya şifrenizi yanlış girdiniz,lütfen tekrar deneyiniz.")

# 4- Girilen 3 sayiya büyüklük olarak karsilastiraniz.
sayi1 = int(input("Sayı Giriniz: "))
sayi2 = int(input("Sayı Giriniz: "))
sayi3 = int(input("Sayı Giriniz: "))

if sayi1>sayi2>sayi3:
    print("Büyükten küçüğe doğru sıralaması: ",sayi1,sayi2,sayi3)
elif sayi1>sayi3>sayi2:
    print("Büyükten küçüğe doğru sıralaması: ",sayi1,sayi3,sayi2)
elif sayi2>sayi1>sayi3:
    print("Büyükten küçüğe doğru sıralaması: ",sayi2,sayi1,sayi3)
elif sayi2>sayi3>sayi1:
    print("Büyükten küçüğe doğru sıralaması: ",sayi2,sayi3,sayi1)
elif sayi3>sayi1>sayi2:
    print("Büyükten küçüğe doğru sıralaması: ",sayi3,sayi1,sayi2)
else:
    print("Büyükten küçüğe doğru sıralaması: ",sayi3>sayi2>sayi1)
   

# 5- Kullanacidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayinaz
vize1 = float(input("1.Vize notunuzu giriniz: "))
vize2 = float(input("2.Vize notunuzu giriniz: "))
final = float(input("final notunuzu giriniz: "))

ortalama = ((vize1 + vize2)/2) * 0.6 + final * 0.4
print("Ortalamanız: ",ortalama)


#  6- Eger ortalama 50 ve üstündeyse geçti degilse kaldı yazdirin.
if ortalama >= 50:
    print("Geçti")
else:
    print("Kaldı")

#   7- ortamalama 50 olsa bile final not en az 50 olmalidir
if ortalama >= 50 and final >=50:
    print("Geçti")
else:
    print("Kaldı")


# 8- Kisinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayin1z.
#   Formül: (Kilo / boy uzunlugunun karesi)
#   Asagidaki tabloya göre kisi hangi gruba girmektedir.
#   0-18.4=> Zayif
#   18.5-24.9 => Normal
#   25.0-29.9 => Fazla Kilolu
#   30.0-34.9 => Sisman (Obez)

ad = input("Adınızı Giriniz: ")
boy = float(input("Boyunuzu Giriniz metre cinsinden(m): "))
kilo = float(input("Kilonuzu Giriniz kilogram cinsinden (kg): "))
boy = boy*boy
indeks = (kilo / boy)
print(indeks)
if 18.4 >= indeks >=0:
    print("Zayıfsınız.")
elif 24.9 >= indeks >= 18.5:
    print("Normal kilolusunuz.")
elif 29.9 >= indeks >=25.0 :
    print("Fazla kilolusunuz.")
elif 34.9 >= indeks >= 30.0:
    print("Şişman(Obezsiniz)")
else:
    print("Yanlış değer girdiniz.")