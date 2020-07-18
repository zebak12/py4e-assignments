"""Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
loop to find the most prolific committer. """

fname = input('Enter the filename: ')
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname, 'r')

sender = []
sender_count = dict()

# making a list of all senders
for line in handle:
    if line.startswith('From '):
        pieces = line.split()
        sender.append(pieces[1])

# counting senders
for email in sender:
    sender_count[email] = sender_count.get(email, 0) + 1

# finding the most prolific committer
max_mails = None
max_sender = None

for key, value in sender_count.items():
    if max_mails is None or value > max_mails:
        max_mails = value
        max_sender = key

print(max_sender, max_mails)
