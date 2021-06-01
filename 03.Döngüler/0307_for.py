"""
while → adım sayısı belli değilse
for → adım sayısı belliyse
for → koleksiyonlarda (list, dictionary...)

for i in range(1,10) :
    print("hızlı gönderim")

i = list(range(1,10))
print(i)

for i in range(1,11) :
    if i == 5 :
        continue
    print(f"{i}.Öğrenci")

for i in range(1,6) :
    for j in range(1,6) :
        print(f"{i}x{j} = {i*j}",end = " ")
"""


