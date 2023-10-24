# hesap1 = {
#     'Ad': 'Erkan Erikci',
#     'HesapNo': '123456',
#     'Bakiye': 11000,
#     'Borç': 2000,
# }
# def paracek(hesap1,miktar):
#     print(f"Merhaba {hesap1['Ad']}")
#     hesap1['Bakiye'] = hesap1['Bakiye'] - miktar
    
#     if (hesap1['Bakiye'] >= miktar):
#         print('Paranızı Alabilirsiniz.')
#         print("Kalan bakiyeniz",hesap1['Bakiye'])
#     else:
#         print("Yetersiz Bakiye")

# paracek(hesap1,2000)




#Burada kullanıcıya girmesini istedim.
hesap1 = {
    'Ad': input("Adınızı Giriniz: "),
    'HesapNo': float(input("Hesap No Giriniz: ")),
    'Bakiye': float(input("Bakiye Giriniz: ")),  
    'Borç': float(input("Borcunuzu Giriniz: "))  
}

def paracek(hesap, miktar):
    print(f"Merhaba {hesap['Ad']}")
    
    if hesap['Bakiye'] >= miktar:
        hesap['Bakiye'] -= miktar
        print('Paranızı Alabilirsiniz.')
        print("Kalan bakiyeniz:", hesap['Bakiye'])
    else:
        print("Yetersiz Bakiye")

paracek(hesap1, 2000)
