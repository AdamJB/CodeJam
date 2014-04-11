#!/usr/bin/env python

def printItemsToBuy(piCredit, plItems, piCaseNum):
	parsedItem = {}
	for i in range (0, len(plItems)):
		remaining = piCredit - plItems[i]
		if remaining in parsedItem:
			firstItem = parsedItem[remaining] + 1
			secondItem = i + 1
			print("Case #%d: %d %d" % ((piCaseNum+1), firstItem, secondItem))
			break
		else:
			parsedItem[plItems[i]] = i

numCases = int(input())

for case in range(0, numCases):
	credit = input()
	numItems = input()
	items = [int(i) for i in raw_input().strip().split()]
	printItemsToBuy(credit, items, case)