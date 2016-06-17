import re
s = input()
mo = re.match(r"^[0-9][0-9]*", s)
if mo:
    print(mo.group())
else:
    print("Don't match")
