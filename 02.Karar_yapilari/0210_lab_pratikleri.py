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