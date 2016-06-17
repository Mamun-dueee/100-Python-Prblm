n = input()
numbers = [x for x in n.split(',') if int(x)%2]
print(','.join(numbers))
