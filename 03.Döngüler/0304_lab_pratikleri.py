#region hop
a = input("Ekrana yazılmasını istediğiniz yazıyı giriniz : ")
b = 0
while b < 5 :
    print(a)
    b += 1
#endregion

#region hop_1
i = 0 
while i < 5 :
    print("*",end = " ")
    i += 1
print()
#endregion

#region hop_2
i = 0 
while i < 10 :
    if i % 2 == 0 :
        print("*", end = " ")
    else :
         print("$", end = " ")
    i += 1
print()
#endregion

#region hop_3
i , j = 0 , 0
while i < 10 :
    if i % 2 == 0 :
        while j < 10 :
            print("*", end = " ")
            j += 1 
        print()
    else :
        while j < 10 :
            print("$", end = " ")
            j += 1 
        print()
    i += 1
    j = 0

#endregion