"""#region hop
kAdi = input("Kullanıcı Adını giriniz :")
if kAdi != "admin":
    print(f"{kAdi} yetkisi ile admin paneline giremezsiniz.")
#endregion 

#region deneme
a = int (input ("1.notunuzu giriniz : "))
b = int (input ("2.notunuzu giriniz : "))
c = int (input ("3.notunuzu giriniz : "))
ort = (a+b+c)/3
if ort >= 50 :
    print(f"GEÇTİNİZ, ortalamanız → {ort}")
#endregion

#region deneme_1
a = int(input("1.değeri giriniz :"))
b = int(input("2.değeri giriniz :"))
if a > b :
    print(f"{a} > {b}")
#endregion

#region deneme_3
a = int(input("Bir sayı giriniz : "))
if a < 0 :
    print(f"{a} değerinin mutlak değeri {a*-1} sayısıdır.")
if a >= 0 :
    print(f"{a} değerinin mutlak değeri {a} sayısıdır.")
#endregion 

#region deneme_4
bakiye = 5000 
kullaniciEFT = int(input("Ne kadar transfer edeceksiniz (TL) : "))
bankaAdi = "Halk"
bankaAdi2 = "Halk"
if bankaAdi != bankaAdi2 :
    kullaniciEFT *= 1.05
print(f"Şuanki bakiyeniz → {bakiye - kullaniciEFT}")
#endregion

biletFiyat = int(input("Ücretiniz : "))
bavulA = 15
if bavulA > 15 :
    biletFiyat += (bavulA-15)*7.5
print(f"Bilet fiyatınız → {biletFiyat*1.18} TL'dir.")
"""

Alinan = int(input("Ne kadar ücretlik ürün aldığınızı giriniz : "))
if Alinan <= 250 :
    Alinan += 7.5
print(f"Toplam ücretiniz → {Alinan} TL'dir.")


Alinan = int(input("Ne kadar ücretlik ürün aldığınızı giriniz : "))
Alinan  += 7.5
if Alinan >= 250 :
    Alinan -= 7.5

print(f"Toplam ücretiniz → {Alinan} TL'dir.")