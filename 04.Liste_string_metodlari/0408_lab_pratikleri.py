# region

listem = [9, 7, 5, 1, 3, 4, 2, 6, 8]

listem.append(listem[0])
listem.remove(listem[0])
print(listem)

listem.remove(listem[0])
listem.insert(5,7)
print(listem)

for i in listem[:6] :
    if listem[0] < i :
        listem.insert((listem.index(i))+1,listem[0])
        listem.remove(listem[0])
print(listem)

for i in listem[5:8] :
    if listem[4] < i :
        listem.insert((listem.index(i)),listem[4])
        listem.remove(listem[4])
print(listem)

# endregion
