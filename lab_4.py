import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1
x = ("I am what I am")
words = x.split()
print(words)
d = dict()
for word in words:
	if word in d:
		d[word] = d[word] + 1
	else:
		d[word] = 1
print(d)

#2
x = ("I like artificial intelligence")
x = x.replace(" ", "")
x = x.lower()
ngram_len = 3
print(x)
d = dict()
a = []
if ((len(x) % 2 > 0) & (ngram_len % 2 == 0)):
	del a[-1]
elif ((len(x) % 3 > 0) & (ngram_len % 3 == 0)):
	del a[-1]
for letter in range(len(x))[ : : ngram_len]:
	abc = x[letter] + x[letter + 1] + x[letter + 2]
	a.append(abc)
print(a)
for ngram in a:
	if ngram in d:
		d[ngram] = d[ngram] + 1
	else:
		d[ngram] = 1
print(d)