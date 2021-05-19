"""
#region odev
n1, n2 = int(input("Birinci sınav notunu giriniz : ")), int(input("İkinci sınav notunu giriniz : "))
ort = (n1+n2)/2
if ort >=85 :
    print(f"Yıl sonu notunuz {ort}, başarı durumunuz : Pekiyi")
elif ort >=70 :
    print(f"Yıl sonu notunuz {ort}, başarı durumunuz : İyi")
elif ort >=55 :
    print(f"Yıl sonu notunuz {ort}, başarı durumunuz : Orta")
elif ort >=45 :
    print(f"Yıl sonu notunuz {ort}, başarı durumunuz : Geçer")
else:
    print(f"Yıl sonu notunuz {ort}, başarı durumunuz : Geçemez")
#endregion

#region odev_1
s1, s2, s3 = int(input("1.sayıyı giriniz : ")), int(input("2.sayıyı giriniz : ")), int(input("3.sayıyı giriniz : "))
if s1 < s2 :
   s1 , s2 = s2, s1
if s1 < s3 :
    s1, s3 = s3, s1
if s2 < s3 :
    s2, s3 = s3, s2
print(f"Sıralamaları : {s1} > {s2} > {s3}")
#endregion

#region odev_2
a = int (input("Lütfen A kenarını giriniz : "))
b = int (input("Lütfen B kenarını giriniz : "))
if a == b :
    print(f"Karenin alanı : {a*b} cm2'dir.")
else :
    print(f"Dikdörtgenin alanı : {a*b} cm2'dir.")

#endregion 

#region odev_3
kisaKenar = int (input("Lütfen kısa kenarını giriniz : ")) 
uzunKenar = int (input("Lütfen uzun kenarını giriniz : "))
if kisaKenar < uzunKenar :
    print(f"Alanınız {kisaKenar*uzunKenar}, Çevresi {(kisaKenar+uzunKenar)*2}")
elif kisaKenar == uzunKenar :
    print("Kare için alan ve çevre ölçümü yapılamaz.")
else :
    print("Kısa kenar, uzun kenardan daha yüksek bir değer alamaz. Tekrar deneyin.")
#endregion

#region odev_4
a = int(input("Birinci sayıyı giriniz : "))
b = int (input ("İkinci sayıyı giriniz : "))
if a % b == 0:
    print(f"{a} sayısı {b} sayısına tam bölünür.")
else :
    print(f"{a} sayısı {b} sayısına tam bölünemez.")
#endregion

#region hop
a, b = int(input("İlk notu giriniz\t:")),int(input("İkinci notu giriniz\t:"))
ort = (a+b)/2
if ort >= 85 :
    print(f"Ortalamanız → {ort}, PEKİYİ")
elif ort >= 70 :
    print(f"Ortalamanız → {ort}, İYİ")
elif ort >= 55 :
    print(f"Ortalamanız → {ort}, ORTA")
elif ort >= 45 :
    print(f"Ortalamanız → {ort}, GEÇER")
else :
    print(f"Ortalamanız → {ort}, GEÇEMEZ")
#endregion

#region hop_1
a , b = int(input("Sayı giriniz\t:")),int(input("Sayı giriniz\t:"))
if a > b :
    print(f"{a}>{b}")
elif a < b :
    print(f"{a}<{b}")
else :
    print(f"{a}={b}")   
#endregion

#region hop_3
kullanici = input("Kullanıcı adınızı giriniz\t:")
if kullanici == "admin" :
    parola = input("Parolanızı giriniz\t:")
    if parola == "123" :
        print(f"Hoş geldin {kullanici},giriş başarılı ! ")
    else :
        print("Parolayı yanlış girdiniz. Tekrar deneyiniz.")
else :
    print("Kullanıcı adını yanlış girdiniz.")
#endregion

# region hop_3
a = int(input("1.sayı giriniz\t:"))
b = int(input("2.sayı giriniz\t:"))
c = int(input("3.sayı giriniz\t:"))
if b > a:
    a, b = b, a
if c > a:
    a, c = c, a
if c > b:
    b, c = c, b
print(f"{a}>{b}>{c}")
# endregion

#region hop_4
a = float(input("Dörtgenin bir kenarını giriniz :"))
b = float(input("Dörtgenin diğer kenarını giriniz :"))
if a == b :
    print(f"Karenin alanı → {a*b}")
else :
    print(f"Dikdörtgenin alanı → {a*b}")
#endregion

#region hop_5
a = int(input("1.sayıyı giriniz\t:"))
b = int(input("2.sayıyı giriniz\t:"))
if b != 0 :
    if a % b == 0 :
        print(f"{a} sayısı {b} sayısına tam bölünür.")
    else :
        print(f"{a} sayısı {b} sayısına tam bölmez.")
else:
    print("payda 0 girilemez.")

#endregion
"""

#region ödev 
"""
    - Klavyeden iki tane fiyat verisi alınır.
    - Eğer bu fiyat verileri düzgünse;
        - Eğer ödenecek tutar 200TL den fazlaysa, ikinci ürüne
            %25 indirim yapılacaktır.
        - Değilse bişey yapılmayacak.
    - 150,300 -> Ürünlerin fiyatı .. TL ve .. TL'dir. İkinci ürüne
     .. TL indirim yapılmıştır. Borcunuz : ..TL'dir.
"""
fiyat_1 = int(input("1.fiyatı giriniz\t:"))
fiyat_2 = int(input("2.fiyatı giriniz\t:"))
toplam = fiyat_1 + fiyat_2
if toplam >= 200 :
    indirim= fiyat_2 * 0.75
    print(f"{fiyat_1},{fiyat_2} TL değerindeki ürünlerin toplam fiyatı → {fiyat_1+indirim}, {fiyat_2*0.25} TL değerinde indirim yapılmıştır.")
else :
    print(f"{fiyat_1},{fiyat_2} TL değerindeki ürünlerin toplam fiyatı → {fiyat_1+fiyat_2}")
