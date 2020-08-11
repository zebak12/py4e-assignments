import sqlite3

conn = sqlite3.connect('mbox.sqlite')
cur = conn.cursor()

#empty data from db if exists
cur.execute('DROP TABLE IF EXISTS Counts')
#create table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#file to read data from
fname = input('Enter filename: ')
if len(fname) < 1: fname = 'mbox.txt'
fhandle = open(fname, 'r')
for line in fhandle:
    if line.startswith('From: '):
        org_name = line.strip().split('@')[1].split(' ')[0]
        cur.execute('SELECT count FROM Counts WHERE org = ?', (org_name,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)',(org_name,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org_name,))

conn.commit() #write the data to sql

#get organization in decreasing order of count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()
