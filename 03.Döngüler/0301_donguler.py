#region hop
i = 0
while i < 10 :
    i += 1
    print("24 saatte kargoda")
print(i)
#endregion

#region aman 
"""
while True :
    print("şu an while döngüsü içindeyim.")

i = 1
while i < 3 :
    print("a")
    if i == 2 :
        i += 1
        print("c")
print("d")
"""
#endregion

#region while_yazim_kurallari
"""
1 → Başlangıç
2 → Bitiş
3 → Artış miktari
"""
#endregion

#region hop_1
i = 1
while i <= 5 :
    print(i)
    i += 1
#endregion

#region hop_2
sayac = 5
while sayac :      #boolean default sonucu → True
    print("Ekin")  #int default değeri → 0
    sayac -= 1
#endregion

#region hop_3
sayac = 5
devamMi = True
while devamMi :
    print("Ekin")
    if sayac == 2 :
        devamMi = False
    sayac -= 1
#endregion