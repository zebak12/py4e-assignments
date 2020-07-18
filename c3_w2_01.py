"""The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a
regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers. """

import re

fname = input('Enter filename:')
if len(fname) < 1: fname = 'regex_sum_693852.txt'
fhandle = open(fname, 'r')
numbers = list()

for line in fhandle:
    num = re.findall('[0-9]+', line.strip())
    if num:
        for i in range(len(num)):
            numbers.append(num[i])

total = 0
for x in numbers:
    total += int(x)

print(total)
