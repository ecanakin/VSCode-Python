# region list
"""
katilimcilistesi = ["alperen","kübra"]
"""
# endregion

# region bosliste

isimler = []
print(isimler)

# endregion

# region ornek

sayilar = [11, 15, 17, 3.14]
print(sayilar)

# endregion

# region index

sayilar = [11, 7, 12, 1, 0, 3.14]
print(sayilar[1])
print(sayilar[-1])

# endregion

# region guncelleme_degistirme

sayilar = [11, 15, 7, 12]
print(sayilar)
sayilar[1] = 34
print(sayilar)
sayilar[1], sayilar[3] = sayilar[3], sayilar[1]
print(sayilar)
# endregion

# region listenin_uzunluğu
sayilar = [11, 15, 7, 12, 15, 25]
print(len(sayilar))
print(sayilar[len(sayilar)-1])
print(sayilar[len(sayilar) // 2])  # ortadaki değer

print()
# endregion

# region del
sayilar = [11, 15, 7, 12, 15, 25]
print(sayilar)
del sayilar[1]
print(sayilar)
# endregion

# region loop_ile_oku
sayilar = [12, 36, 9, 5, 3, 74]
print(sayilar)
for i in sayilar:
    if i > 30:
        print(i, end=" ")
# endregion

# region toplama

sayilar = [12, 36, 9, 5, 3, 74]
toplam = 0
print(sayilar)
for i in sayilar:
    toplam += i
print(toplam)

# endregion

#region
sayilar = [12, 36, 9, 5, 3, 74]
adet = 0
print(sayilar)
for i in sayilar:
    if i % 2 != 0:
        adet += 1
print(adet)
# endregion
