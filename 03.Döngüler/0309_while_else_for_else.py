#region while-else
"""
while döngüsü break satırı çalışarak biterse,else içerisine girmez.
while döngüsü break satırı çalışmadan biterse, else içerisine girer.
"""
i = 1 
while i <= 10 :
    print(i, end = " ")
    if i == 2 :
        break
    i += 1
else :
    print("Else'deyim.")
print("Döngü bitti.")
#endregion

#region for else :
"""
for döngüsü break satırı çalışarak biterse,else içerisine girmez.
for döngüsü break satırı çalışmadan biterse, else içerisine girer.
"""
for i in range(10, 1, -1) :
    print(i, end = " ")
    if i == 9 :
        break
else :
    print("şuan else'deyim.")
print("Buradayım !")
#endregion

#region for else 
serachId = 11069
for orderId in range(1,10000) :
    if orderId == serachId :
        print(f"{orderId} nolu siparişiniz için detay listesi")
        print("...")
        break
else :
    print(f"{serachId} nolu arama bulunamadı.")
#endregion
