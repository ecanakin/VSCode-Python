"""
rakam = int (input("lütfen sayı giriniz :"))
print(f"girdiğiniz {rakam} rakamın 1 fazlası {rakam+1}")

sayi=int(input("Bir sayi girin\t: "))
print(f"{sayi} değerinin karesi {sayi**2}")

a= int(input("Birinci sayıyı giriniz :"))
b = int(input("İkinci sayıyı giriniz :"))
c = int(input("Üçüncü sayıyı giriniz :"))
print(f"{a},{b},{c} sayılarının ortalaması → {(a+b+c)/3}")
"""
"""
Lütfen Üçgenin A Kenarı Açısını Giriniz: 30
Lütfen Üçgenin B Kenarı Açısını Giriniz: 60
C Kenarı 90 Derecedir
"""

"""
a = int(input("Üçgenin A kenarı açısını giriniz :"))
b = int(input("Üçgenin B kenarı açısını giriniz :"))
c = 180-(a+b)
print(f"Bir üçgenin {a} ve {b} derecelerinde iki açısı varsa üçüncü açı {c}")
"""
"""
a = int(input("Lütfen A kenarının uzunluğunu giriniz :"))
b = int(input("Lütfen B kenarını giriniz :"))
print(f"Bir kenarı {a} m , bir kenarı {b} m olan dörtgenin alanı → {a*b} metrekaredir", end = ".")
"""
x1 = int(input("x1 değerini giriniz"))
y1 = int(input("y1 değerini giriniz"))
x2 = int(input("x2 değerini giriniz"))
y2 = int(input("y2 değerini giriniz"))
uzaklık = ((x1-x2)**2+(y1-y2)**2)**.5
print(f"({x1},{y1}) ile ({x2},{y2}) arasındaki uzaklık → {round(uzaklık,2)}")

