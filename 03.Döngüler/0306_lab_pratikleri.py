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