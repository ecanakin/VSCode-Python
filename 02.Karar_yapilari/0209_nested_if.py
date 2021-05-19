#nested if → iç içe if demektir.
"""
#region odev
havaYagisliMi = False 
havaSogukMu = True
if havaYagisliMi :
    if havaSogukMu :
        print("Montunuzu giyiniz.")
    else :
        print("Hırka giyiniz.")
else :
    if havaSogukMu:
        print("Montunuzu ve berenizi giyiniz.")
    else :
        print("Tişört giymeniz yeterlidir.")
#endregion

#region odev_1
a = int(input("Bir değer giriniz(0 veya negatif sayı girmeyiniz.) : "))
if a <= 0 :
    print("0 veya negatif sayılar girilemez.")
else:
    if a < 100 :
        print(f"{a} olarak girdiğiniz değer 100'den küçüktür.")
    elif a == 100 :
        print("100 değerini girdiniz.")
    else :
        print(f"{a} olarak girdiğiniz değer 100'den büyüktür..")
#endregion
"""
#region odev_2
sayi = int(input("Bir sayı giriniz\t:"))
if sayi <= 0 :
    print("Başka bir değer giriniz.")
else :
    if sayi > 0 :
        if sayi < 100 :
            print("Sayınız 100'den küçük pozitiftir.")
        else :
            print("Sayı 100'den küçük, pozitiftir.")
#endregion