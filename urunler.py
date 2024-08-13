from datetime import datetime
import os

zmn = datetime.now()
tarih = zmn.date().isoformat()
saat = zmn.strftime("%H:%M")
ürün_isimleri = []
ürün_fiyatları = []
sepet = []
kasiyerler = ["onur","0"]
adminler = {"onur":"123","1":"1"}
ürün_adet = 1
veri_tabanı= [
("ekmek",1,10),
("Muz",2,35),
("Süt",3,20),
("Yumurta",4,60),
("Çikolata",5,10)
    ]
katalog = veri_tabanı



class ürün():
    ürün_dict = {}
    ürün_barkodları = []
    ürün_list = []

    def __init__(self,ürün_adı,barkod,fiyat):
        self.ürün_adı = ürün_adı
        self.barkod = barkod
        self.fiyat = fiyat    
        ürün.ürün_dict[barkod] = self
        ürün.ürün_barkodları.append(self.barkod)
        ürün.kasiyer_adı ="bilinmiyor"
    
    def başla():
        while True:
            print("1.kasiyer girişi\n2.admin girişi\n3.uygulamayı kapat\n[1,2,x]")
            cvp0 = str(input("girişinizi seçşiniz : "))
            if cvp0 == "1":
                ürün.kasiyer_girişi()
            elif cvp0 == "2": 
                ürün.admin_girişi()
            elif cvp0 == "x": 
                ürün.admin_girişi()
                break
            else : pass

    def admin_girişi():
        admin_Ad = str(input("admin adı giriniz: "))
        while admin_Ad not in adminler.keys():
            print("admin adı geçersizdir")
            admin_Ad = str(input("admin adı giriniz: "))
        şifre = str(input("şifre giriniz: "))
        if şifre in adminler.values():
            ürün.admin_işlemler()

    def kasiyer_girişi():
        isim = str(input("kasiyer adnınızı giriniz : "))
        if isim in kasiyerler:
            ürün.kasiyer_adı=isim
            ürün.kasiyer_işlemler()
        else : 
            print("kasiyer bulunamadı,tekrar deneyiniz")
            ürün.kasiyer_girişi()

    def katalog_görüntüle():
        print("ürün adı\tbarkod")
        for a in ürün.ürün_dict.values():
            print(f"{a.ürün_adı}\t{a.barkod}")

    def kataloga_ürün_ekle():
        ürün.katalog_görüntüle()
        ü_isim = str(input("kataloğa eklenicek olan ürünün ismi:"))
        ü_barkod = int(input("kataloğa eklenicek olan ürünün barkodu:"))
        while ü_barkod in ürün.ürün_barkodları:
            print("dikkat her ürünün kendi barkodu olmak zorundadır")
            print("lütfen tekrar deneyiniz")
            ü_barkod = int(input("kataloğa eklenicek olan ürünün barkodu:"))
        ü_fiyat = int(input("kataloğa eklenicek olan ürünün fiyatı:"))
        ürün(ü_isim,ü_barkod,ü_fiyat)
        print("ürün başarıyla eklenmiştir")
        ürün.katalog_görüntüle()

    def katalogdan_ürün_çıkart():
        ürün.katalog_görüntüle()
        silinecek_barkod = input("lütfen çıkartılacak ürünün barkodunu giriniz:")
        while silinecek_barkod not in str(ürün.ürün_barkodları):
            print("lütfen var lan bir barkod seçiniz")
            silinecek_barkod = input("lütfen çıkartılacak ürünün barkodunu giriniz:")
        del ürün.ürün_dict[int(silinecek_barkod)]
        ürün.katalog_görüntüle()    

    def admin_işlemler():
            while True:
                print("1.kataloga ürün ekle\n2.katalogdan ürün çıkart\n[1,2,x]")
                cvp1 = str(input("işlemin1izi seçin : "))
                if cvp1 == "1":
                    ürün.kataloga_ürün_ekle()
                elif cvp1 == "2":
                    ürün.katalogdan_ürün_çıkart()
                elif cvp1 == "x":
                    print("oturum kapatıldı")
                    break
                else : 
                    print("lütfen geçerli bir giriş yapnınız")


    def kasiyer_işlemler():
        while True:
            print("1.sepeti görüntüle\n2.sepete ürün ekle\n3.sepetten ürün çıkart\n4.fişi göster\n[1,2,3,4,x]")
            cvp1 = str(input("işleminizi seçin : "))
            if cvp1 == "1":
                ürün.sepeti_görüntüle()
            elif cvp1 == "2":
                ürün.ürün_al()
            elif cvp1 == "3":
                ürün.ürün_çıkart()
            elif cvp1 == "4": 
                print(ürün.fiş_göster())
            elif cvp1 == "x":
                print("oturum kapatıldı")
                break
            else : 
                print("lütfen geçerli bir giriş yapnınız")



    def ürün_al():
        abc = 1
        ürün.katalog_görüntüle()
        spete_eklenicek_barkod = int(input("barkod giriniz = "))
        if spete_eklenicek_barkod in ürün.ürün_barkodları:
            eklenen_ürün = ürün.ürün_dict[spete_eklenicek_barkod]
            cvp2 = int(input("kaç tane almak istersiniz : "))
            if cvp2 > 0:
                ürün_adet = cvp2
                eklenen_ürün.fiyat = eklenen_ürün.fiyat*ürün_adet
                sepet.append(eklenen_ürün)
                print("güncel sepet:")
                ürün.sepeti_görüntüle()
            else : 
                print("lütfen tekrar deneyiniz") 
                ürün.ürün_al()
        else : 
            print("barkod bulunamadı,tekrar deneyiniz")
            ürün.ürün_al()

    def ürün_çıkart():
        print(ürün.sepeti_görüntüle())
        spete_eklenicek_barkod = int(input("barkod giriniz = "))
        if spete_eklenicek_barkod in ürün.ürün_barkodları and ürün.ürün_dict[spete_eklenicek_barkod] in sepet:
            çıkartılan_ürün = ürün.ürün_dict[spete_eklenicek_barkod]  
            sepet.remove(çıkartılan_ürün)
            print("güncel sepet:")
            print(ürün.sepeti_görüntüle())
        else : 
            print("ürün sepetnizde bulunmuyor,tekrar deneyiniz")
            ürün.ürün_çıkart()

    def şimdiki_zaman():
        print(f"Tarih: {tarih}\nSaat: {saat}")


    def sepeti_görüntüle():
            a = 1
            toplam_bakiye = 0
            for b in sepet:
                toplam_bakiye += int(b.fiyat)
            if toplam_bakiye==0:
                print("sepetiniz boş")
            else:
                for i in sepet:
                    print("{2}. {0}\t{1}".format(i.ürün_adı,i.fiyat,a))
                    a += 1 
            print("toplam fiyat =\t{}".format(toplam_bakiye))

            




for eee in katalog:
    ürün(eee[0],eee[1],eee[2])

ürün.başla()









