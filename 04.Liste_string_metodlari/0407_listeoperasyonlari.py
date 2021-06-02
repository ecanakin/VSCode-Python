
# region yer_degistirme
listem = [1, 2, 3, 4, 5]

temp = listem[2]
listem[2] = listem[3]
listem[3] = temp
print(listem)
listem[2], listem[3] = listem[3], listem[2]
print(listem)

# endregion

# region slice
# listeler iterable'dır.

listem = [1, 2, 3, 4, 5]
ad = "Ekin"
print(ad[0])
print(ad[0:2])
print(ad[-2:])
print(ad[1:3])
print(ad[:])
print(ad[:3: 2])

# endregion

# region slice_ornek
url = input ("Sitenin adını giriniz : ")
if not url[-3:] == "com" or not url[:3] == "www" :
    print("url formatında giriniz.")
else :
    print(f"Yükleniyor... → {url}")
# endregion
