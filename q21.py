import math
pos = [0, 0]
while True:
    s = input()
    if not s:
        break
    movements = s.split(' ')
    direction = movements[0]
    steps = int(movements[1])

    if direction == 'UP':
        pos[1] += steps
    elif direction == 'DOWN':
        pos[1] -= steps
    elif direction == 'LEFT':
        pos[0] -= steps
    elif direction == 'RIGHT':
        pos[0] += steps
    else:
        pass

print(round(math.sqrt(pos[0]**2+pos[1]**2)))
