#!/usr/bin/env python

# list

# tuple

# set
testSet = {'Jason', 'Johnny'}
testSet2 = {'Winnie', 'Mary', 'Jason'}
print testSet & testSet2
print testSet | testSet2
print testSet - testSet2

# dict
password = {'Jason': 123, 'Winnie': 456}
# get dict with defaul value
print password.get('Jason', 0)
print password.get('W', 0)

# Flatten a list of lists (nested for loop in one line)
lists = [[1,2,3], [4,5,6], [7,8]]
print [element for slist in lists for element in slist]

# for loop in one line
print ", ".join([str(number) for number in range(20)])

