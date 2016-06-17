n = int(input())
print('NO' if all([n%i for i in[4,7,47,74,447,474,477,747,774]]) else 'YES')
