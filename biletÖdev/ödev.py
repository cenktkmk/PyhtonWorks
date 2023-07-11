class Bilet:
    def bilet_olustur(self):
        self.kapasite = 0
        self.satis = 0
        self.bilet_sahibi = ""

    def biletkes(self, kapasite):
        self.kapasite = kapasite

    def biletayarla(self):
        self.satis = self.kapasite

    def biletSat(self, bilet_sayisi):
        if self.satis >= bilet_sayisi:
            self.satis -= bilet_sayisi
            print(bilet_sayisi, "bilet satıldı. Kalan bilet sayısı:", self.satis)
        else:
            print("Yetersiz bilet sayısı. Satış yapılamadı.")

    def biletDetay(self, bilet_sahibi):
        self.bilet_sahibi = bilet_sahibi
        print("Bilet sahibi:", self.bilet_sahibi)


bilet = Bilet()
bilet.bilet_olustur()  # Bilet nesnesini oluştur

bilet.biletkes(8)  # Maksimum kapasiteyi 8 olarak ayarla
bilet.biletayarla()  # 8 bilet alındı

satis_zamani = input("Bilet satışı yapılacak zamanı girin: ")
bilet_sayisi = int(input("Kaç bilet satın almak istiyorsunuz? "))

bilet.biletSat(bilet_sayisi)

isim = input("Bilet alıcının ismini girin: ")
bilet.biletDetay(isim)  # Bilet sahibi: <girilen_isim>
