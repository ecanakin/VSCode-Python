#region append → eleman ekleme

meyveler = ["elma","armut","muz","ayva","üzüm"]
meyveler.append("karpuz")
print(meyveler)

#endregion

#region insert → istediğiniz indekse eleman eklerc
meyveler = ["elma","armut","muz","ayva","üzüm"]
print(meyveler)
meyveler.insert(2,"portakal")
print(meyveler)
#endregion

#region remove → listeden siler
meyveler = ["elma","armut","muz","ayva","üzüm"]
print(meyveler)
meyveler.remove("armut")
print(meyveler)
#endregion

#region pop → listeden siler
meyveler = ["elma","armut","muz","ayva","üzüm"]
print(meyveler)
meyveler.pop() #boş olunca listedeki en son değeri siler, boş kümeyi silemez
print(meyveler)
meyveler.pop(2)
print(meyveler)
#endregion
"""
#region clear → listeyi temizler(ram'de olmaya devam eder, del ile tamamen silinir.)
meyveler = ["elma","armut","muz","ayva","üzüm"]
print(meyveler)
meyveler.clear()
print(meyveler)
del meyveler
print(meyveler)
#endregion
"""
#region copy → listeyi kopyalar
meyveler = ["elma","armut","muz","ayva","üzüm"]
print(meyveler)
meyveTabagi = meyveler.copy()
print(meyveTabagi)
#endregion

#region count → elemanı sayar
listeRakamlar = [2,5,6,1,9,7,5]
elemanAdedi = listeRakamlar.count(9)
print(elemanAdedi)
#endregion

#region ornek
meyveler = ["elma","armut","muz","ayva","üzüm"]
aranan = "muz"
elemanAdedi = meyveler.count(aranan)
if elemanAdedi : # elemanAdedi != 0
    print(f"Aradığınız {aranan}, listede yer almaktadir.")
else :
    print(f"Aradığınız {aranan}, listede yer almamaktadir.")
#endregion

#region sort_reverse → sırala_tersten sırala
meyveler = ["elma","armut","muz","ayva","üzüm"]
meyveler.sort()
print(meyveler)
meyveler.reverse()
print(meyveler)
#endregion

#region index → arama_index_dondurme
meyveler = ["elma","armut","muz","ayva","üzüm"]
print(meyveler.index("elma"))
#endregion
