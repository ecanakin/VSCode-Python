# region ornek
sayilar = [11, 5, 36, 78, 99, 2]
n = 0
for i in sayilar :
    if i == 99 :
        break
    n += 1
print(f"Aradığınız elemanın index'i → {n}")
# endregion

# region ornek_1

olistesi = ["ali","kemal","mehmet","mustafa"]
while True :
    oad = input("Aradığınız öğrencinin ismi (çıkmak için ç) : ")
    if oad == "ç" :
        break
    for i in olistesi :
        if i == oad :
            print(f"{oad} isimli öğrencimiz kayıtlıdır.")
            break
    else :
        print(f" {oad} adlı öğrenci bulunamadı.")
#endregion

# region ornek_2
olistesi = ["ali","kemal","mehmet","mustafa"]
while True :
    oad = input("Aradığınız öğrencinin ismi (çıkmak için ç) : ")
    if oad == "ç" :
        break
    for i in range(len(olistesi)) :
        if olistesi[i] == oad :
            print(f"{oad} isimli öğrencimiz kayıtlıdır ve sırası {i+1}.")
            break
    else :
        print(f" {oad} adlı öğrenci bulunamadı.")
#endregion

