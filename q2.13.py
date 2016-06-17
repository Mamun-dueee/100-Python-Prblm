tp = tuple(x for x in range(1, 11))
li = list()
for i in tp:
    if tp[i]%2==0:
        li.append(tp[i])

tp2 = tuple(li)
print(tp2)
