"""
#region hop
a = input("Ekrana yazılmasını istediğiniz yazıyı giriniz : ")
b = 0
while b < 5 :
    print(a)
    b += 1
#endregion

#region hop_1
i = 0 
while i < 5 :
    print("*",end = " ")
    i += 1
print()
#endregion

#region hop_2
i = 0 
while i < 10 :
    if i % 2 == 0 :
        print("*", end = " ")
    else :
         print("$", end = " ")
    i += 1
print()
#endregion

#region hop_3
i , j = 0 , 0
while i < 10 :
    if i % 2 == 0 :
        while j < 10 :
            print("*", end = " ")
            j += 1 
        print()
    else :
        while j < 10 :
            print("$", end = " ")
            j += 1 
        print()
    i += 1
    j = 0

#endregion

#region hop_4
i = 0
while i < 100 :
    if i % 2 != 0 :
        print(i , end= " ")
        if i % 20 == 19 :
            print()
    i += 1
#endregion

#region hop_5
i = 0
j = 0
while i < 100 :
    if i % 2 != 0 :
        j += i
    i += 1
print(f"1- 99 arasındaki sayıların toplamı → {j}")
#endregion

#region hop_6
sayi = int(input("Lütfen bir sayı giriniz :"))
j = 0
while j <= 10 :
    print(f"{sayi} x {j} = {sayi*j}")
    j += 1
#endregion

#region hop_7

gizli = input("Gizli kelimeyi söyleyiniz : ")
while gizli != "susam":
    print("Tekrar deneyiniz.")
    gizli = input("Gizli kelimeyi söyleyiniz : ")
print("Tebrikler kurtuldunuz.")

#endregion

#region hop_8
sayi = int(input("Lütfen sayı giriniz (0 girdiğinizde sayıların toplamı ve ortalamasına ulaşırsınız.) : "))
i = 0
j = 0
while sayi != 0 :
    i += sayi
    j += 1
    sayi = int(input("Lütfen sayı giriniz : "))
print(f"Girdiğiniz sayıların toplamı {i} ve ortalaması → {i/j}")
#endregion

#region hop_9
sayi = int(input("Lütfen bir sayı giriniz :"))
i = 1
while i <= 5 :
    print(f"{sayi*i}", end = " ")
    i += 1
#endregion

#region hop_10
i = 1
j = 1
while i <=5 :
    print(f"{i} faktöriyel → {j}")
    i += 1
    j *= i
#endregion

#region hop_11
i = 100
while i < 1000:
    a = i // 100
    b = (i % 100) // 10
    c = i % 10
    if a + b + c == 3 :
        print(f"Hanelerin toplamının 3 olduğu daireler → {i}")
    i += 1
#endregion

#region hop_12
import random
tahmin = random.randint(1,99)
print(tahmin)
i = 0
enfark = 99999999999
while i < 3 :
    kullanici = int(input("Tahmini sayınızı giriniz : "))
    fark = tahmin - kullanici
    if fark < 0 :
        fark *= -1
    if fark < enfark :
        enfark = fark
        enyakin = kullanici
    i += 1
print(enyakin)

#endregion

#region hop_13
i = 10 
j = 10
while i != 0 :
    while j != 0:
        print(f"*",end = " ")
        j -= 1
    print()
    i -= 1
    if j == 0 :
         j = i

while i != 11 :
    while j != i + 1:
        print(f"*",end = " ")
        j += 1
    print()
    i += 1
    j = 0

#endregion

#region hop_14
i , j = 0 , 4
n = 0
while i < 4 :
    while n > 0 :
        print("   ", end = "")
        n -= 1
    while j > 0 :
        print(" * ", end = "")
        j -= 1
    i += 1
    n = i
    j = 4 - i
    print()

#endregion

#region hop_15
i , j , n= 0 , 0 , 0
while i < 4 :
    while j < 4 :
        if n < i :
            print("   ", end = "")
        else :
            print(" * ", end = "")
        j += 1
        n += 1
    i += 1
    j = 0
    n = 0
    print()
#endregion

#region hop_16
i, j, n = 5, 0, 0
while i > 0 :
    while j <= 5 :
        if n < i :
            print(" ", end = "")
            n += 1
            j += 1
        else :
            print("*", end = " ")
            n += 1
            j += 1
    print()
    n = 0
    j = 0
    i -= 1 
#endregion

#region hop_17
metin = input("Metni giriniz :")
a = int(input("Lütfen tekrar sayısını giriniz :"))
i = 0
while i < a :
    print(metin)
    i += 1
#endregion

#region hop_18
i = 0
while i < 10 :
    print(" * ", end = "")
    i += 1
#endregion

#region hop_19
i = 0
while i < 10 :
    if i % 2 != 0 :
        print("*", end = " ")
        i += 1
    else :
        print("$", end = " ")
        i += 1
#endregion

#region hop_20
i = 0
j = 0
while i < 10 :
    if i % 2 == 0 :
        while j < 10 :
            print(" * ", end = "")
            j += 1
    else :
        while j < 10 :
            print(" $ ", end = "")
            j += 1
    i += 1
    j = 0
    print()  
#endregion

#region hop_21 
i = 0
j = 0
while i < 10 :
    while j < 10 :
        if j % 2 == 0 :
            print(" * ", end = "")
            j += 1
        else :
            print(" $ ", end = "")
            j += 1
    i += 1
    j = 0
    print()
#endregion

#region hop_21 
i = 0 
j = 0
while i < 10 :
    if i % 2 == 0 :
        while j < 10 :
            if j % 2 == 0 :
                print("*", end = " ")
                j += 1 
            else :
                print("$", end = " ")
                j += 1 
    else :
       while j < 10 :
            if j % 2 == 0 :
                print("$", end = " ")
                j += 1 
            else :
                print("*", end = " ")
                j += 1  
    i += 1
    j = 0
    print()
 
sayi = int (input("Lütfen sayı giriniz : "))
i = 1
while i <= 5 :
    print(f"{sayi} x {i} = {sayi*i}")  
    i += 1
#endregion

#region hop_21
i = 0
j = 0
while i < 10 :
    while j < 10 :
        if j < i :
            print(" * ", end = "")
        else :
            print("  ", end = "")
        j += 1
    i += 1
    j = 0
    print()
#endregion   

#region hop_22
i = 19
while i < 100 :
    if i % 2 != 0 :
        print(i, end= " ")
    if i % 20 == 17 :
        print()
    i += 1 
#endregion  
print()
#region hop_22 
gizli = input("Gizli kelimeyi söyleyiniz : ")
while gizli != "susam" :
    if gizli == "susam" :
      pass
    else :
        print("Tekrar deneyiniz.")
    gizli = input("Gizli kelimeyi söyleyiniz : ")
print("Kapı açıldı.")   
#endregion 
print()
#region hop_22
sayi = int(input("Bir sayı giriniz : "))
i = 0
j = 0
while sayi != 0 :
    i += sayi
    sayi = int(input("Bir sayı giriniz : "))
    j += 1
print(f"Ortalama = {i / j} ")
#endregion

#region 
sec = input("ç girene kadar notları giriniz. ")
j = 0
f = 0
i = 1
while sec != "ç" :
    a= int(input(f"{i}. öğrencinin vize notunu giriniz : "))
    b= int(input(f"{i}. öğrencinin final notunu giriniz : "))
    print(f"{i}. öğrencinin ortalaması → {(a+b)/2}")
    j += a
    f += b
    i += 1
    if (a+b)/2 >= 50 :
        print("Geçtin.")
    sec = input("ç girene kadar notları giriniz. ")
print(f"{i} öğrencinin vize ortalaması → {j/ i}, {i} öğrencinin final ortalaması → {f/ i}  ")
#endregion

#region 
i = int(input("Bir sayı giriniz : "))
j = 1
while j <= 5 :
    print(f"{j*i}", end = " ")
    j +=  1
#endregion

#region 
sayi = int(input("Faktöriyelini istediğiniz sayıyı giriniz "))
i = 1
j = 1
while i<= sayi :
    j *= i
    i += 1
print(f"{sayi}'nın faktöriyeli → {j}")
#endregion

import random
enKucukFark = 9999999
rSayi = random.randint(1, 99)
print(rSayi)  # bu satır bilgi amaçlıdır, publish etmeden önce sil
i = 0
while i < 3:
    tahmin = int(input("lütfen [1-99] arası sayı tahmin ediniz\t :"))
    fark = rSayi - tahmin
    if fark < 0:
        fark *= -1
    if fark < enKucukFark:
        enKucukFark = fark
        enYakinTahmin = tahmin
    i += 1
print(f"en yakın tahmininiz {enYakinTahmin}")
"""
#region
i = 0
j = 10
k = 10
while i < 10 :
    while j > 0 :
        if i < k :
            print(" * ", end = "")
            j -= 1
            k -= 1
            
        else :
            print("   ", end = "")
            j -= 1
            k -= 1
    print()   
    i += 1
    j = 10
    k = 10

while i < 10 :
    while j > 0 :
        if i > k :
            print("   ", end = "")
            j -= 1
            k -= 1
            
        else :
            print(" * ", end = "")
            j -= 1
            k -= 1
    print()   
    i += 1
    j = 10
    k = 10

#endregion

i, j = 0, 10, 
while i < 10:
    while j > 0:
        print(" * ", end=" ")
        j -= 1
    i += 1
    j = 10 - i
    print()
i, j = 0, 0 
while i < 10:
    while j < i:
        print(" * ", end=" ")
        j += 1
    i += 1
    j = 0
    print()
