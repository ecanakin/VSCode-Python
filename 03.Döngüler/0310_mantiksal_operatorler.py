
# region
"""
1 → ve     and
2 → veya   or
3 → değil  not
"""
# endregion
"""
# region and

print(5 == 5 and 15 > 5)
print(5 == 5 and 15 < 5)
print(5 == 15 and 15 > 5)
print(5 == 15 and 15 < 15)

# endregion

# region or

print(5 == 5 or 15 > 5)
print(5 == 5 or 15 < 5)
print(5 == 15 or 15 > 5)
print(5 == 15 or 15 < 15)

# endregion

# region not

print(not 5 == 5)
print(not 5 != 5)

# endregion

# region hop
a = int(input("Bir sayı giriniz : "))
if a > 0 and a < 100 :
    print(f"{a} değeri 100'den küçük ve pozitiftir.")

a = int(input("Bir sayı giriniz : "))
if 0 < a < 100:
    print(f"{a} değeri 100'den küçük ve pozitiftir.")
# endregion

# region hop_1
yas = int(input("Lütfen yaş giriniz : "))
if 4 <= yas <= 6:
    print("Kurs 1ê hoşgeldiniz.")
else :
    print("Kurs 1'e uygun değilsiniz.")
#endregion

# region hop_2
toplam = 0
while True :
    sayi = int(input("Lütfen sayı giriniz. Çıkmak için 0'a basınız."))
    if sayi == 0:
        break
    if sayi < 0 or sayi % 2 == 1 :
        print("Negatif ve tek olan sayı giremezsiniz.")
        continue
    toplam += sayi
print(toplam)
#endregion

#region hop_3
yasiniz = int(input("Yaşınızı giriniz : "))
if 4 <= yasiniz <= 6 :
    print("Kursa hoşgedlin.")
elif yasiniz <= 0 :
    print("Yaş negatif veya 0 olamaz.")
else :
    print(f"{yasiniz} olarak girdiğiniz yaş kursumuza uygun değildir.")
#endregion

# region hop_4
kilo = float(input("Kilonuz : "))
boy = float(input("Boyunuz[m] :"))
vki = kilo / boy**2
if vki < 18.49:
    print("İdeal kilonun altında.")
elif vki > 18.5 and 24.99 > vki:
    print("İdeal kilo")
elif vki > 25 and vki < 29.99 :
    print("İdeal kilonun üstünde")
    print(f"{kilo - (vki*boy**2)} kilo vermelisiniz.")
else :
    print("Kilonun çok üzerinde")
# endregion
"""
#region hop_5
izleme = int(input("Kaç izleme alındı : "))
if izleme < 1000000 :
    print(f"{izleme // 1000} B")
elif izleme >= 1000000 and izleme < 1000000000 :
    print(f"{izleme // 1000000} Mn")
else :
    print(f"{izleme // 1000000000} Ml")
#endregion
