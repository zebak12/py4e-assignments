"""Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines
of the form: X-DSPAM-Confidence:    0.8475 Count these lines and extract the floating point values from each of the
lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or
a variable named sum in your solution. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
and when you are testing below enter mbox-short.txt as the file name """

fname = input("Enter filename: ")
fh = open(fname, 'r')

count = 0
total = 0

for line in fh:
    if line.startswith('X-DSPAM-Confidence'):
        colon_pos = line.find(':')
        confidence_str = line[colon_pos + 1:]
        total += float(confidence_str)
        count += 1

print("Average spam confidence:", total/count)
