import random

meyveler = ["elma", "armut", "muz", "çilek", "karpuz"]

# Rastgele bir meyve seçme
secilen_meyve = random.choice(meyveler)

print("Meyveler:", meyveler)
print("Seçilen meyve:", secilen_meyve)

# Kullanıcıdan meyve girmesini isteme
girilen_meyve = input("Bir meyve girin: ")

# Girilen meyveyi listeden çıkarma
if girilen_meyve in meyveler:
    meyveler.remove(girilen_meyve)
    print(girilen_meyve, "listedeki meyvelerden çıkartıldı.")
else:
    print(girilen_meyve, "listedeki meyveler arasında bulunamadı.")

print("Güncellenmiş meyveler:", meyveler)





meyveler.append("kiraz")
meyveler.append("şeftali")
print("Güncellenmiş meyveler:", meyveler)





# 3. indexe sahip olan meyveyi portakal olarak değiştirme
if len(meyveler) > 3:
    meyveler[3] = "portakal"
    print("Güncellenmiş meyveler:", meyveler)
else:
    print("Listede yeterli sayıda meyve yok.")




isimler = ["Ali", "Ayşe", "Mehmet", "Fatma", "Ahmet"]

# Kullanıcıdan isim girmesini isteme
girilen_isim = input("Bir isim girin: ")

# İsim kontrolü ve karşılama
if girilen_isim in isimler:
    print("Hoş geldiniz,", girilen_isim)
else:
    isimler.append(girilen_isim)
    print("Yeni isim listeye eklendi.")

print("Güncellenmiş isimler:", isimler)



# Listenin başına yeni bir veri eklemek için insert() fonksiyonunu kullanabilirsiniz.
meyveler.insert(0, "ananas")
print("Güncellenmiş meyveler:", meyveler)
