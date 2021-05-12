
#region ödev_1
Leylek Uygulamasına Hoşgeldiniz !
Sürüş Ücreti → 0.69 krş/dk
"""

""")
s = int(input("Sürüş için geçen süre (saat) \t:"))
d = int(input("Sürüş için geçen süre (dakika) \t:"))
toplam_süre = (s*60)+d
ucret = toplam_süre*.69
print(f"{s} saat {d} dakikalık yolculuğun ücreti {round(ucret,2)} TL'dir.")
#endregion

#region ödev_2
a = int(input("Mil\'e çevrilmesini istediğiniz değeri kilometre cinsinden giriniz :"))
print(f" {a} km olarak verilen mesafenin mil cinsinden değeri → {round(a/1.609344,2)} mildir", end = ".")
#endregion

#region ödev_3
a = int(input("Aracınız kaç kilometre yol girdiği giriniz :"))
s_lt = a / 100
ucret = s_lt*4.8*7.09
print(f"{a} km yol giden aracınızın benzin ücreti {round(ucret,2)} TL'dir.")
#endregion

#region ödev_4
miktar=float(input("lütfen benzin endeksini girin\t:"))
yakit_tuketimi=float(input("lütfen yakıt tüketimini(100 km )  girin\t: "))
alinan_yol=int(input("aracın aldığı yolu girin \t:"))
toplam_tuketim=(yakit_tuketimi*alinan_yol*miktar)/100

print(toplam_tuketim)
#endregion

#region ödev_5
a = input("Ürün adını giriniz :")
b = int(input(f"{a}\'dan satın alınacak adet sayısını giriniz :"))
c = int(input("Lütfen ürün fiyatını giriniz [KDV-Dahil] :"))
d = int(input("Ürün için yapılacak indirim yüzdesini giriniz :"))
e_toplam = b*c*95/100
print(f"Ödemeniz gereken fiyat : {e_toplam} TL'dir.")
#endregion

#region ödev_6
sayi = int(input("Lütfen bir sayı giriniz :"))
islem = sayi*(1+11+111)
print(f"Sonuç : {islem}")
#endregion

#region ödev_7
at = int(input("Aylık elektrik tüketiminizi giriniz (kWh) :"))
aeb = at * 0.39736
db = aeb * 0.2474
teb = aeb + db
tp = 3.97
ef = 1.39
etv = 9.92
kdv = (teb + tp + ef + etv) * 0.18
vt = tp + ef + etv + kdv
tf = vt + teb
print(f"Aylık ödemeniz gereken elektrik ücreti : {round(tf,3)} TL\'dir.")
#endregion