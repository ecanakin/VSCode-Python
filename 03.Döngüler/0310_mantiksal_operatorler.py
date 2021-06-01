# region
"""
1 → ve     and
2 → veya   or
3 → değil  not
"""
# endregion

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
