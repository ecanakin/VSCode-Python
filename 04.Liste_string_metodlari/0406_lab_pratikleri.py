
# region ornek
listeogrenci = []
while True:
    ogrenci = input("Öğrenci giriniz. Çıkmak için 0'a basınız. :")
    if ogrenci == "0":
        print("Çıkış yapıldı.")
        break
    listeogrenci.append(ogrenci)
    print(f"{ogrenci} adlı öğrenci başarıyla eklendi.")
print(listeogrenci)
# endregion

# region ornek_1

listeogrenci = []
while True:
    a = int(input(
        "Yapmak istediğiniz işlemi seçiniz (0→ çıkış yap, 1 → ekle, 2 → sil,3 → listele) : "))
    if a == 0:
        print("Çıkış yapıldı.")
        break
    elif a == 1:
        ogrenci = input("Öğrenci giriniz : ")
        listeogrenci.append(ogrenci)
        print(f"{ogrenci} adlı öğrenci başarıyla eklendi.")
    elif a == 2:
        ogrenci = input("Öğrenci giriniz : ")
        listeogrenci.remove(ogrenci)
        print(f"{ogrenci} adlı öğrenci başarıyla çıkarıldı.")
    elif a == 3:
        for j in listeogrenci:
            print(j)
    else:
        print("Hatalı işlem yapıldı.")

# endregion

# region ornek_2
liste_ad = []
listeNot1 = []
listeNot2 = []
liste_ort = []
while True:
    ad = input("Adınız (Çıkmak için 0'a basınız.):")
    if ad == "0" :
        print("Çıkış yapıldı.")
        break
    not1, not2 = int(input("1.notunuz :")), int(input("2.notunuz :"))
    liste_ad.append(ad)
    liste_ort.append((not1+not2)/2) 
    continue
for i in liste_ort :
        print(i)   
print(f"En düşük ortalama {min(liste_ort)}")
print(f"En yüksek ortalama {max(liste_ort)}")
# endregion

# region ornek_3

liste_ad = []
listeNot1 = []
listeNot2 = []
liste_ort = []
ort = 0
adet = 0
while True:
    ad = input("Adınız (Çıkmak için 0'a basınız.):")
    if ad == "0" :
        print("Çıkış yapıldı.")
        break
    not1, not2 = int(input("1.notunuz :")), int(input("2.notunuz :"))
    liste_ad.append(ad)
    liste_ort.append((not1+not2)/2) 
    continue
for i in liste_ort :
        ort += i
        adet += 1
print(f"Çan değeri → {ort / adet}")
for i in liste_ort :
    if i < ort :
        print(f"{i} puanıyla {liste_ad[liste_ort.index(i)]} adlı öğrencinin sonucu → Geçemediniz.")   

    else :
        print(f"{i} puanıyla {liste_ad[liste_ort.index(i)]} adlı öğrencinin sonucu → Geçebildiniz.")   
print(f"En düşük ortalama {min(liste_ort)}")
print(f"En yüksek ortalama {max(liste_ort)}")


# endregion

# region ornek_4

while True :
    a = int (input("Okunmasını istediğiniz değeri giriniz :"))
    birler = a % 10 
    onlar = a // 10
    bb =["", "bir", "iki", "üç", "dört","beş","altı","yedi","sekiz","dokuz"]
    ob = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    if birler == 0 :
        print(ob[onlar])
    else :  
        print(f"{ob[onlar]} {bb[birler]}")
        
# endregion
