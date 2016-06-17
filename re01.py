import re

fh = open("mamun_phn_book.txt")
for line in fh:
    if re.search(r"J.*Neu", line):
        print(line.strip())

fh.close()
