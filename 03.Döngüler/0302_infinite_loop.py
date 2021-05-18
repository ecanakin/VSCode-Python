#region hop
eb = -9999999999
sayi = int (input ("Lütfen bir sayı giriniz, çıkmak için -1 giriniz : "))
while sayi != -1 :
    if sayi > eb :
        eb = sayi
    sayi = int (input("Lütfen bir sayı giriniz, çıkmak için -1 giriniz : "))
print(f"Girdiğiniz en büyük değer → {eb}")
#endregion

#region hop_1
Tek, Cift = 0, 0
tekToplam, ciftToplam = 0, 0
sayi = int (input ("Lütfen bir sayı giriniz, çıkmak için 0 giriniz : "))
while sayi != 0 :
    if sayi % 2 ==  0 :
        Cift += 1
        ciftToplam += sayi
    else :
        Tek += 1 
        tekToplam += sayi
    if sayi > eb :
        eb = sayi
    sayi = int (input("Lütfen bir sayı giriniz, çıkmak için -1 giriniz : "))
print(f"Girdiğiniz en büyük değer → {eb} \nGirdiğiniz tek sayı adedi → {Tek}\t Toplamı → {tekToplam}\nGirdiğiniz çift sayı adedi → {Cift}\t Toplamı → {ciftToplam} ")
#endregion