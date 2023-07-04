ad_soyad = input("Adınız ve soyadınızı girin: ")
dogum_tarihi = input("Doğum tarihinizi girin: ")

print("Ad Soyad:", ad_soyad)
print("Doğum Tarihi:", dogum_tarihi)



# Kullanıcıdan sınav notlarını girmesini isteme
not1 = float(input("1. sınav notunu girin: "))
not2 = float(input("2. sınav notunu girin: "))
not3 = float(input("3. sınav notunu girin: "))
not4 = float(input("4. sınav notunu girin: "))

# Notların ortalamasını hesaplama
ortalama = (not1 + not2 + not3 + not4) / 4

print("Not Ortalaması:", ortalama)



# Kullanıcıdan cümle girmesini isteme
cumle = input("Bir cümle yazın: ")
cumleUpper = cumle.upper
# Cümleyi başlık stiliyle yazdırma
print(cumleUpper)
