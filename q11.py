n = input()
n = n.split(',')
ans = []
for i in n:
    i = int(i,2)
    if(i%5==0):
        ans.append(str(bin(i)[2:]))

print(','.join(ans))

        
