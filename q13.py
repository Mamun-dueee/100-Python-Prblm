s = input()
ans = {"digits":0, "letters":0}

for c in s:
    if c.isdigit():
        ans["digits"] += 1
    elif c.isalpha():
        ans["letters"] += 1
    else:
        pass

print("LETTERS", ans["letters"])
print("DIGITS", ans["digits"])
