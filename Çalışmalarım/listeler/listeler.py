adlar = ['Ali' , 'Yağmur' , 'Hakan' , 'Deniz']
Yıllar = [1998 , 2000 , 1998 , 1987]
# 1-"Cenk" ismini listenin sonuna ekleyiniz.
adlar.append('Cenk')

# 2-"Sena" degerini listenin basina ekleyiniz.
adlar.insert(0,'Sena')

# 3-"Deniz" ismini listeden siliniz.
del adlar[-2]

# 4-"Ali" isminin indeksi nedir ?
index = adlar.index('Ali')
print(index)
# 5-"Ali" listenin bir elemanı midir
adlar in ['Ali']

# 6- Liste elemanlarini ters cevirin.
adlar.reverse()

#7- Liste elemanlarin1 alfabetik olarak siralayiniz.
adlar.sort()

# 8-Yıllar listesini rakamsal büyüklüge göre siralayiniz.
Yıllar.sort()

# 10- Yıllar dizisinin en büyük ve en küçük elemani nedir?
küçük = min(Yıllar)
Büyük = max(Yıllar)
print(küçük)
print(Büyük)

# 11- Yıllar dizisinde kaç tane 1998 degeri vardir
sonuç = Yıllar.count(1998)
print(sonuç)
# 12- Yıllar dizisinin tum elemanlarini siliniz.
del Yıllar[:]

print(adlar)
print(Yıllar)

