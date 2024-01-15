def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    print(liste[0])
    print(liste[1])


def Notları_oku():
    with open("SinavNotları.txt","r",encoding="utf-8") as sonuc:
        for satir in sonuc:
            print(not_hesapla(satir))



def Not_gir():
    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    vize = input("Öğrenci vizesi: ")
    final = input("Öğrenci finali: ")
    butunleme = input("Öğrenci bütünlemesi: ")

    with open("SinavNotları.txt","a",encoding="utf-8") as ogrenci:
        ogrenci.write(ad+ "  "+ soyad + " : "+vize+","+final+","+butunleme+"\n")


def notları_kayitet():
    pass



while True:
    islem = input("1-Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4-Çıkış\n ")
    
    if islem == '1':
        Notları_oku()
    elif islem == '2':
        Not_gir()
    elif islem == '3':
        notları_kayitet()
    elif islem == '4':
        break
    else:
        print("Yanlış değer girdiniz.")