s1 = 2
s2 = 4
ortalama = (s1+s2)/2
print("Ortalama : ", ortalama)

s1 = 2
s2 = 4
print("ortalama : ", (s1+s2)/2 )
print( s1, " sayısı ile ", s2," sayısının ortalaması : ", ortalama)

#region odev_1
a = 1
b = 65
print(a," metre", b, "santimetre")
#endregion

#region ödev_1a

a =165
m = 165 // 100
cm = 165 % 100
print("Kişinin boyu ",m," metre", cm, " santimetredir", end = ".\n")

#endregion

#region ödev_2
adim_sayisi = 5000
harcanan_kalori = adim_sayisi/20
print("Hedeflenen", adim_sayisi, " adım ile günlük harcanan kalori", harcanan_kalori,". Haftalık ise bu değer", harcanan_kalori*7, " kalori, aylık ise ", harcanan_kalori*30," kaloridir", end = ".")

#endregion

#region ödev_2a

adim_sayisi = 5000
harcanan_kalori = adim_sayisi/20
print("\nGirdiğiniz",adim_sayisi,"adıma göre ulaştığınız bedensel nokta şunlardır;\n","Harcanan kalori : ",harcanan_kalori," cal\n","Haftalık : ",harcanan_kalori*7," cal\n","Aylık : ", harcanan_kalori*30," cal'dir", end = ".\n")

#endregion

#region ödev_3
km = 5000
mil = km/1.609344
print(km," kilometrenin mil cinsinden değeri : ",mil,"mildir", end = ".")
#endregion