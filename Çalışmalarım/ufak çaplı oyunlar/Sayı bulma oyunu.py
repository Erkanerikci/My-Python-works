import random

sayi = random.randint(1, 100)
hak = 5

while hak > 0:
    hak -= 1
    girilen = int(input('1-100 arasında sayı giriniz: '))

    if sayi == girilen:
        print(f'Kazandınız,Puanınız: {hak*20+20}')
        break
    elif sayi > girilen:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f'Hakkınız bitti, Tutulan sayı {sayi}')
        break
