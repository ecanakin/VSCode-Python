#region hop
i , j = 0 , 0
while i < 3 :
    while j < 3 :
        print(f"{i} x {j}")
        j += 1
    i += 1
    j = 0
#endregion

#region hop_1
i = 0 
while i < 10 :
    print("* "*10)
    i += 1


i , j = 0 , 0 
while i < 10 :
    while j < 10 :
        print("*", end = " ")
        j += 1 
    print()
    i += 1
    j = 0
#endregion

#region hop_2
i , j = 0 , 0 
while i < 10 :
    while j < 10 :
        pass
#endregion