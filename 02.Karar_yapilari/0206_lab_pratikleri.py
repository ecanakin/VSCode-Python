#region odev
bilet = int(input("Lütfen bilet fiyatını giriniz : "))
bavulKilo = 10
agirlik = int(input("Bavul ağırlığınızı giriniz(kg)\t→ "))
if agirlik >15 :
    fark = agirlik -15
    fiyatFarki = fark * 5
print(f"Güncel Fiyat\t→{(bilet * 1.18)+ fiyatFarki} TL'dir.")
#endregion
#region odev_2
bFiyat = float(input("Bilet fiyatını giriniz : "))
kBavul = float(input("Bavul ağırlığınızı giriniz(kg) : "))
ekUcret = 0
if kBavul >15 :
    ekUcret =(kBavul-15)*5
    print(f"Bu uçuştaki {kBavul-15} kg fazlalığınızdan dolayı {ekUcret} TL fazla ödeyeceksiniz.")
print(f"Uçuşunuzun KDV miktarı → {bFiyat*0.18} TL'dir.")
print(f"Toplam Ücret → {bFiyat*1.18 + ekUcret} TL'dir.")
print("İyi uçuşlar dileriz.")
#endregion
#region odev_3
a = int (input("Bir sayı giriniz :"))
if a < 0 :
    a *= -1
print(f"{a} değerinin mutlak değeri → {a}")
#endregion
#region odev_4
bMusteri = 5000
bKodu = 101
eftBKodu = 102
kesinti = 0
transfer = float (input("lütfen EFT tutarını giriniz : "))
Kod =int(input("EFT yapacağınız bankayı seçin (Kendi bankanız → 101, başka banka → 102) : "))
if Kod == eftBKodu :
    kesinti = transfer * .05
print(f"{Kod} ile gönderdiğiniz tutardan hesabınızda kalan bakiyeniz = {bMusteri- transfer - kesinti}")
#endregion
#region odev_5
eb = 0
s = int(input ("1.sayı giriniz : "))
if s > eb :
    eb = s
b = int(input("2.sayıyı giriniz : "))
if b > eb :
    eb = b
c = int(input("3.sayıyı daha giriniz : "))
if c > eb :
    eb = c
print(f"{s},{b},{c} değerleri arasında girilen en büyük değer → {eb}")
#endregion
#region odev_6
s1 = int(input ("1.sayı giriniz : "))
s2 = int(input ("2.sayı giriniz : "))
if s1 > s2 :
    print(f"{s1} değeri {s2} değerine göre büyüktür.")
if s2 > s1 :
    print(f"{s2} değeri {s1} değerine göre büyüktür.")
if s2 == s1 :
    print(f"{s1} değerli iki sayı birbirine eşittir.")
print(f"{s1} ve {s2} değerlerinin ortalaması → {(s1+s2)/2}")
if (s1+s2)/2 > 50:
    print(f"GEÇTİNİZ. {s1} ve {s2} değerlerinin ortalaması → {(s1+s2)/2}")
print("Sağlıkla kalın.", end = " :)")
#endregion
