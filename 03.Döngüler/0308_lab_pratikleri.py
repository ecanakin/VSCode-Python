"""
sayi = int(input("Lütfen sayı giriniz : "))
for i in range(1,sayi+1) :
    if sayi % i == 0 :
        print(i, end = " ")

a = int(input("1.sayıyı giriniz : "))
b = int(input("2.sayıyı giriniz : "))
if a < b :
    for i in range(a,b+1):
        print(i, end = " ")
else :
    for i in range(b,a+1) :
        print(i, end = " ")

sayi = int(input("Sayı giriniz : "))
a = 0
for i in range (1,sayi+1):
    if sayi % i == 0 :
        a += 1
if sayi % a == 0 :
    print(f"{sayi} TAU'dur.")
else :
    print(f"{sayi} TAU değildir.")
"""
b= 0
sayi = int(input("Bir sayı giriniz : "))
for i in range(1,sayi) :
    if sayi % i == 0 :
        b += i
if sayi == b :
    print(f"{sayi} mükemmel sayıdır.")
else :
    print(f"{sayi} mükemmel sayı değildir.")    

