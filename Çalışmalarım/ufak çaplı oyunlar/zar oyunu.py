import random 


kullanıcı1 = random.randint(1,6)

kullanıcı2 = random.randint(1,6)

print("Sizin attığınız zar",kullanıcı1)

print("BOT'un attığınız zar",kullanıcı2)

if kullanıcı1>kullanıcı2:
    print("kazandınız")

elif kullanıcı1==kullanıcı2:
    print("berabere kaldınız")
    
else:
    print("kaybettiniz")    
