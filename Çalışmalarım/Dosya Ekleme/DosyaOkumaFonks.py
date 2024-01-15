# Reading Fonksiyonu

# try:
#     sonuc = open("Yeni Dosya.py","r",encoding='utf-8')  
#     print(sonuc)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı")
#     sonuc.close()

#---------

# sonuc = open("Yeni Dosya.py","r",encoding='utf-8')

# for a in sonuc:
#     print(a,end="") # end'i kullanmamızdaki amaç ise aradaki boşlukları göstermemesi için

# sonuc.close()


#-----------
# sonuc = open("Yeni Dosya 1.py","x",encoding='utf-8') 
# oku = sonuc.read()
# print(oku)
# sonuc.close()

#-----------

# sonuc = open("Yeni Dosya.py","r",encoding='utf-8')
# oku = sonuc.read(5)
# oku = sonuc.read(6)
# print(oku)


#-----------
# sonuc = open("Yeni Dosya.py","r",encoding='utf-8')
# print(sonuc.readline(),end="")
# print(sonuc.readline(),end="") # Readline ise 1 satırı kullanıcıya gösteriyor.
# print(sonuc.readline(),end="")

# sonuc = open("Yeni Dosya.py","r",encoding='utf-8')
# print(sonuc.readlines()) # Readlines ise herbir satırı 1 liste elemanı gibi gösteriyor.


with open("Yeni Dosya.py","r",encoding='utf-8') as sonuc:
    oku = sonuc.read()
    sonuc.seek(10) #Seek kaçıncı karaktere kadar okumasını istiyorsak kullanıyoruz
    print(oku) #With kullandığımızda ise fonksiyonu kapatmaya artık gerek kalmıyor 
    print(sonuc.tell()) # tell fonksiyonu kaç tane karakter olduğunu gösteriyor.
    