def karesi(sayi) :   
    return sayi **2
# sonuç = karesi(input("Karesini almak istediğiniz sayıyı giriniz:  ")) #Kullanıcıya karesini aldırmak için kullanılır.

sayilar = [1,5,6,8]

sonuç = list(map(karesi,sayilar))

for mat in map(karesi,sayilar):
    print(mat)

print(sonuç)#Burada ise map methodu ile her sayı için döndürmesini sağlıyor.

#-------------------------------------------------------------------------------------------------------
#Burada ise lambda methodu ile daha kolay bir şekilde karesini almasını sağladık.


sayilar = [1,5,6,8]

sonuç = list(map(lambda sayi: sayi**2,sayilar))


print(sonuç)