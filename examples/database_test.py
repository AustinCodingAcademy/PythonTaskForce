# pip install MySQL-python
import MySQLdb
import MySQLdb.cursors
from pprint import pprint

# Create a connection object by calling the connect() method on MySQLdb
conn = MySQLdb.connect(host='localhost', user='root', passwd='something', db='acadb', port=3306,
                       cursorclass=MySQLdb.cursors.DictCursor)

# Acquire a cursor to operate on this connection with MySQL
cur = conn.cursor()

# Remove all existing parse data from the table prior to beginning.

# Query to create a table called music. Only create this table if it does not exist
create_music_table_query = '''
CREATE TABLE IF NOT EXISTS `music` (
  `music_id` int(11) NOT NULL AUTO_INCREMENT,
  `full_path` text,
  `size` float(5,2) DEFAULT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `artist` varchar(100) DEFAULT NULL,
  `album` varchar(255) DEFAULT NULL,
  `date_added` datetime DEFAULT NULL,
  PRIMARY KEY (`music_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
'''

# Now run this query against the current connection cursor, and create the table
cur.execute(create_music_table_query)

# Remove all the data from this table
cur.execute('truncate music');

# Lets create a dummy dictionary with some fake music data
# @todo: get this data from the file system
tracks = [
    {
        'full_path': '/tmp/song1.mp3',
        'size': 9.564565,
        'genre': 'Rockabilly',
        'artist': 'The Fentones',
        'album': 'Hot Rod',
        'date_added': 'NOW()'
    },
    {
        'full_path': '/tmp/song2.mp3',
        'size': 12.498734,
        'genre': 'Classic Rock',
        'artist': 'U2',
        'album': 'Songs of Innocence',
        'date_added': 'NOW()'
    },
    {
        'full_path': '/tmp/song3.mp3',
        'size': 10.653466,
        'genre': 'Classic Rock',
        'artist': 'U2',
        'album': 'Blue Sky',
        'date_added': 'NOW()'
    }
]

# Iterate over this data and insert it into the table we just created.
for track in tracks:
    # create an insert query
    # @todo: Create database class so we don't have to create a query every time!
    insert_query = 'INSERT INTO music (full_path, size, genre, artist, album, date_added) ' \
                   'VALUES ( ' \
                   '"%s ", %.2f, "%s", "%s", "%s", %s );' % (
                       track['full_path'], track['size'], track['genre'],
                       track['artist'], track['album'], track['date_added'])

    # Run the insert query
    cur.execute(insert_query)

print('Do a select to fetch the data that we just inserted')
select_query = 'SELECT * FROM music'
cur.execute(select_query)
track_rows = cur.fetchall()

#Loop through each returned row and print it to screen nicely
for row in track_rows:
    pprint(row)
    print('------------------------------')


# Commit this whole transaction to MySQL atomically. If any one statement fails, everything fails.
conn.commit()