import math as m
c = 50
h = 30
items = [x for x in input().split(',')]
ans = []
for i in items:
    ans.append(str(round(m.sqrt((2*c*int(i))/h))))

print(','.join(ans))
