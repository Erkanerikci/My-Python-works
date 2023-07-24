import random
while True:
    kullanıcı1 = int(input("kırmızı ise 0 siyah ise 1 yazın: "))
    if kullanıcı1 == 0:
        kullanıcı1 = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    elif kullanıcı1 == 1:
        kullanıcı1 = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    else:
        print("Yanlış değer girdiniz.")

    masa = random.randint(0, 37)
    print("Rulet numarası:", masa)

    if masa in kullanıcı1:
        print("Kazandınız.")
    else:
        print("Kaybettiniz.")

    