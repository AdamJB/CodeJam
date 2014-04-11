#!/usr/bin/env python

def reverseWords(plWords, piCaseNum):
	numWords = len(plWords)
	for i in range (0, numWords/2):
		tmp = plWords[i]
		plWords[i] = plWords[numWords-i-1]
		plWords[numWords-i-1] = tmp
	words = " ".join(plWords)
	print("Case #%d: %s" % (case+1, words))

numCases = int(input())

for case in range(0, numCases):
	words = [s for s in raw_input().strip().split()]
	if (len(words) == 1):
		print("Case #%d: %s" % (case+1, words[0]))
	else:
		reverseWords(words, case)