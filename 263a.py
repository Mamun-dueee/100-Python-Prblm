for i in range(5):
    s = input()
    if '1' in s:
        print(abs(2-i)+abs(2-s.index('1')))
        break
