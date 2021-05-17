#region hop
Hav_Dur = "yağmurlu"
if Hav_Dur == "yağmurlu" :
    print("Lütfen şemsiyenizi alınız.")
#endregion
#region hop_1
a = -10
if a < 0 :
    print(f"{a} sayısı negatiftir.")
#endregion
#region hop_2
s = int(input("Lütfen sayı giriniz :"))
if s == 0 :
    print("Lütfen 0 değeri girmeyin.")
#endregion
#region hop_3
uName = input("Kullanıcı adınızı giriniz \t:")
if uName != "Ekin" :
    print(f"{uName} adlı misafir panele giriş yapamaz.")
#endregion

sayi = int(input("Bir sayı giriniz :"))
if sayi < 0 :
    print(f"{sayi} negatiftir.")

kullanici = input("Adınızı giriniz : ")
if kullanici != "admin" : 
    print(f"{kullanici} yetkisi ile admin paneline giremezsiniz.")