#region break_continue
"""
break → döngüyü sonlandırır
continue → tepeye geri döndürür

#endregion

#region
i = 1
while i <= 10 :
    print(i, end = " ")
    if i == 6 :
        break
    i += 1
#endregion

#region
a = int (input("Sayıyı giriniz :"))
b = -99999999
while True :
    if a > b :
        b = a
    a = int (input("Sayıyı giriniz :"))
    if a == -1 :
        break
print(f"En büyük değer {b}")
#endregion

#region
i = 0
b = -9999
while True :
    a = int(input("Bir sayı giriniz :"))
    i += 1
    if i == 1 :
        if a ==  -1 :
            print("Daha ilk sayınızı girmediniz ki !")
            i += 1
            continue 
    if a > b :
        b = a
        i += 1
    if a == -1 :
        break
print(f"{i} kadar sayı arasında en büyük değer {b}")
#endregion

#region
while True :
    a = 0
    sayi = int(input("Bir sayı giriniz -1 yazarsanız sistem durur.\t:"))
    if sayi == -1 : 
        print("Kendinize iyi bakın.")
        break
    elif sayi % 2 == 0 :
        print("Tek sayı giriniz.")
        continue
    else :
        a += sayi
print(f"Tek sayıların toplamı {a}")
#endregion
"""
while True :
    b = input("Gizli kelimeyi giriniz\t:")
    if b == "q" :
    if b == "susam" :
        print("Kapı açıldı.")
        break
    print("Tekrar deneyiniz.")
