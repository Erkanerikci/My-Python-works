#-Burada ise range methodunu gördük range'in mantığı ise girilen değerde durmasını sağlıyor.
# for sayi in range(5,15):
#     print(sayi)

# for sayi in range(5,100,15):#5 ten başlayıp 15 er 15 er 100 e kadar artırır.
#     print(sayi)


#-Enumerate ise kaç karakter olduğunu numaralandırmak için yapılır.
# x = 'Merhaba'

# for karakter,sayi in enumerate(x):
#     print(f'karakter: {karakter}  sayi : {sayi}' )
#-Zip ise listeleri birleştiren bir methottur.
# list1 = [52,65,89,45,59,14]
# list2 = ['Ahmet','Mehmet','Ali','Erkan','Hüseyin','Kazım']
# list3 = ['Kaya','Erden','Veli','Erikci','Kağıt','Kazım']
# print(list(zip(list1,list2,list3)))