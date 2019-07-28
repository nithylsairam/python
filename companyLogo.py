from collections import Counter

s = input()
lettr_freq = Counter(s)
most_comn = list(lettr_freq.items())
most_comn.sort(key=lambda t: (-t[1], t[0]))

for lettr, freq in most_comn[:3]:
    print(lettr, freq)
