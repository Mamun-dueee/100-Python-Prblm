s = input()
freq = {}
for word in s.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
#words.sort()
for w in sorted(words):
    print("%s:%d" %(w,freq[w]))
