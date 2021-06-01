#region ornek

kg =float(input("Kilonuz : "))
mt =float(input("Boyunuz : "))
vki = round(kg / mt**2)
if vki< 18.49 :
    print("İdeal kilonun altı")
elif vki > 18.5 and vki < 24.99 :
    print("İdeal kilo")
elif vki > 25 and vki < 29.99 :
    print("İdeal kilonun üzeri")
elif vki > 30 :
    print("İdeal kilonun çok üzerinde")

#endregion

#region ornek_1

a = int(input("Yıllık geliriniz : "))
if a < 22000 :
    b = a * 0.15
elif a > 22000 and a <49000 :
    b = a * 0.2
elif a > 4900 and a < 180000 :
    b = a * 0.27
elif a > 180000 and a < 600000 :
    b = a * 0.35
else :
    b = a * 0.40
print(f"Yıllık gelir verginiz {b}")

#endregion
