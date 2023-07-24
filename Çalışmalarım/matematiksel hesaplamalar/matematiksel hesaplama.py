import math

hesap =int(input("faktöriyel hesaplamak için 0'ı girin veya Bir sayının karesini almak için 1 sayısını girin."))
if hesap==1:
    sayi1 =int(input("karesi alınacak sayiyi girin."))
    sayi1= sayi1*sayi1
    print(sayi1)
elif hesap==0:
    sayi2 =int(input("faktöriyel alınacak sayiyi girin."))
    sayi2 =math.factorial(sayi2)
    print(sayi2)
else:
    print("Bir şeyler ters gitti")

