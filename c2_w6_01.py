"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the
counts for each hour, print out the counts, sorted by hour as shown below. """

fname = input('Enter the filename: ')
if len(fname) < 1: fname = 'mbox-short.txt'
fhandle = open(fname, 'r')

hours = list()
hours_count = dict()

for line in fhandle:
    if line.startswith('From '):
        pieces = line.split()
        time = pieces[5].split(':')
        hours.append(time[0])

for hour in hours:
    hours_count[hour] = hours_count.get(hour, 0) + 1

for key, value in sorted(hours_count.items()):
    print(key, value)
