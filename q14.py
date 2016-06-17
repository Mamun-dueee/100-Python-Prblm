s = input()
ans = {"upcase":0, "lowcase":0}

for c in s:
    if c.isupper():
        ans["upcase"] += 1
    elif c.islower():
        ans["lowcase"] += 1
    else:
        pass

print("UPPER CASE", ans["upcase"])
print("LOWER CASE", ans["lowcase"])
