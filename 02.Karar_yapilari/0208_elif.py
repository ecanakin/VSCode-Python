#region odev
havaDurumu = "sıcak"
if havaDurumu == "yağmurlu" :
    print(f"Hava {havaDurumu} olduğundan şemsiye alın.")
elif havaDurumu == "sıcak" :
    print(f"Hava {havaDurumu} olduğundan şemsiye almanıza gerek yoktur.")
else :
    print("İlginç bir durum.")
#endregion

#region odev_1
s = int(input("1 sayı giriniz : "))
if s < 0 :
    print(f"{s} olarak girdiğiniz sayı negatiftir.")
elif s == 0 :
    print("0 değeri girdiniz.")
else :
    print(f"{s} olarak girdiğiniz sayı pozitiftir.")