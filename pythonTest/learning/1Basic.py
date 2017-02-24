#!/usr/bin/env python
# python built-in types
print "float: {}".format(10/3.0)
print "complex: {}".format(3 + 4j)
print "repr: {}".format(repr(1.0 - 0.8))
print "str: {}".format(str(1.0 - 0.8))
print "raw string: {}".format(r'C:\test')

# for loop
string = "Test"
for strs in string:
    print strs

# string slice
lang = "Python"
print lang[1:3] # begin inclusive but end exclusive
print lang[-1] # reverse retrieve
print lang[0:] # if not provide end, it will traverse to the end
print lang[:3] # if not provide start, it will be 0
print lang[0:6:2] # traverse in a gap
print lang[::-1] # reverse string

# string formatting
print "{user} is {status}".format(user = 'jason', status = 'alive')

# switch case
switcher = {
    0: 'Zero',
    1: 'One'
}
print(switcher.get(0, 'None'))
# switch case (get immediately)
switcher = {
    0: 'Zero',
    1: 'One'
}.get(0, 'None')
print(switcher)
