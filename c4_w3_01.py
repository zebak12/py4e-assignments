import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
db_handle = conn.cursor()

#empty data from db if exists and/or create table
db_handle.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

#read data from xml file
fname = input('Enter filename: ')
if len(fname) < 1: fname = 'Library.xml'
data = ET.parse(fname)

#helper function from sample code
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

content = data.findall('dict/dict/dict')
print('Tracks count:', len(content))

for track in content:
    if ( lookup(track, 'Track ID') is None ) : continue

    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    album = lookup(track, 'Album')
    genre = lookup(track, 'Genre')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')
    length = lookup(track, 'Total Time')

    if name is None or artist is None or album is None or genre is None : continue

    print("Name: {}, Artist: {}, Album: {}, Genre: {}, Count: {}, Rating: {}, Length: {}".format(name, artist, album, genre, count, rating, length))

    db_handle.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    db_handle.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = db_handle.fetchone()[0]

    db_handle.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (name, artist_id))
    db_handle.execute('SELECT id FROM Album WHERE title = ?', (name,))
    album_id = db_handle.fetchone()[0]

    db_handle.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    db_handle.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = db_handle.fetchone()[0]

    db_handle.execute('''INSERT OR REPLACE INTO Track
    (title, album_id, genre_id, len, rating, count) 
    VALUES (?, ?, ?, ?, ?, ?)
    ''',(name, album_id, genre_id, length, rating, count))
    
    conn.commit()
