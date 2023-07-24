# Burda 2 farklı liste yapmak yerine tek liste yapıp karşılığını kolay şekilde vermek için kullanılır.

# Şehirler = {'Karabük' : 78, 'Kastamonu' : 57}

# print(Şehirler['Karabük']) #Burda Karabüğün direk plaka numarasını veriyor yani burda mesela 81 il'den birini yazıp istediği ilin plakasına ulaşabiliriz.

Kullanıcı = {
    'Erkan Erikci':{
        'yasi': 19,
        'e-mail': 'erkanerikci576@gmail.com',
        'Şehri':  'Karabük',
        'Telefon': '053546218574',
        'İnstagram': '__erkanerikci0'
    }
}
# print(Kullanıcı['Erkan Erikci'])
print(Kullanıcı['Erkan Erikci']['yasi'])
print(Kullanıcı['Erkan Erikci']['e-mail'])
print(Kullanıcı['Erkan Erikci']['Şehri'])
print(Kullanıcı['Erkan Erikci']['Telefon'])
print(Kullanıcı['Erkan Erikci']['İnstagram']) #Burda ise mesela bir çalışanın istersek bütün istersek tekçe telefon numarası veya yaşını görmek için yapıyoruz.
