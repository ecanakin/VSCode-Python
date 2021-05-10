"""

Leylek Uygulamasına Hoşgeldiniz !
Sürüş Ücreti → 0.69 krş/dk
"""

""")
s = int(input("Sürüş için geçen süre (saat) \t:"))
d = int(input("Sürüş için geçen süre (dakika) \t:"))
toplam_süre = (s*60)+d
ucret = toplam_süre*.69
print(f"{s} saat {d} dakikalık yolculuğun ücreti {round(ucret,2)} TL'dir.")
"""

"""
a = int(input("Mil\'e çevrilmesini istediğiniz değeri kilometre cinsinden giriniz :"))
print(f" {a} km olarak verilen mesafenin mil cinsinden değeri → {round(a/1.609344,2)} mildir", end = ".")

"""
"""
a = int(input("Aracınız kaç kilometre yol girdiği giriniz :"))
s_lt = a / 100
ucret = s_lt*4.8*7.09
print(f"{a} km yol giden aracınızın benzin ücreti {round(ucret,2)} TL'dir.")

miktar=float(input("lütfen benzin endeksini girin\t:"))
yakit_tuketimi=float(input("lütfen yakıt tüketimini(100 km )  girin\t: "))
alinan_yol=int(input("aracın aldığı yolu girin \t:"))
toplam_tuketim=(yakit_tuketimi*alinan_yol*miktar)/100

print(toplam_tuketim)
"""

"""
a = input("Ürün adını giriniz :")
b = int(input(f"{a}\'dan satın alınacak adet sayısını giriniz :"))
c = int(input("Lütfen ürün fiyatını giriniz [KDV-Dahil] :"))
d = int(input("Ürün için yapılacak indirim yüzdesini giriniz :"))
e_toplam = b*c*95/100
print(f"Ödemeniz gereken fiyat : {e_toplam} TL'dir.")
"""
"""
- Kısaltmalar;
    - at    aylık tüketim giriniz
    - aeb   aktif enerji bedeli
    - db    dağıtım bedeli
    - teb   toplam enerji bedeli
    - tp    trt payı
    - ef    enerji fonu
    - etv   elektrik tüketim vergisi
    - vt    vergiler toplamı
- elektrik faturamızı hesaplayalım
    - aylık tüketim giriniz ? [kWh]  : 500
    - aktif enerji bedeli = aylık tüketim x 0.39736
    - dağıtım bedeli = aktif enerji bedeli x 0,2474
    - toplam enerji bedeli = aktif enerji bedeli + dağıtım bedeli
    - trt payı = 3.97
    - enerji fonu = 1.39
    - elektrik tüketim vergisi = 9.92
    - KDV = (toplam enerji bedeli + trt payı + enerji fonu + elektrik tüketim vergisi) x 0.18
    - vergiler toplamı = trt payı + eerji fonu + elektrik tüketim vergisi + kdv
    - toplam fatura = vergiler toplamı + toplam enerji bedeli
    """
"""
sayi = int(input("Lütfen bir sayı giriniz :"))
islem = sayi*(1+11+111)
print(f"Sonuç : {islem}")

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
"""