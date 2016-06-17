net_amount = 0
while True:
    s = input()
    if not s:
        break
    submit = s.split(' ')
    key = submit[0]
    value = int(submit[1])
    if key == "D":
        net_amount += value
    elif key == "W":
        net_amount -= value
    else:
        pass

print(net_amount)
