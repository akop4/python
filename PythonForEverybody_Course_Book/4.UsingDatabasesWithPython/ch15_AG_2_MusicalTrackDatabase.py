import sqlite3
import re

# Connect to database
conn, cur = connect_to_database()

# Connect to file with tracks
fh = get_file_handle()

def main():
    # Read data from file
    # Check we have data for parse
    if len(data) < 1:
        print('  Err:Empty data from url!')
        return
    
    # Parse file, and get clear data
    print('Parse data from url')
    clean_data = getClearDataForDatabase(data)
    # Write clean data in db
    if len(clean_data) < 1:
        print('  Err:Empty clean data!')
        return
    
    print('Start to update data in database:')
    updateDatabase(clean_data)
    checkDataInDataBase()
    
    # Close cursor
    cur.close()
    print('Fin!')

def create_tables_if_not_exist(cur):
    # Create new tables if not exist
    cur.execute('''
    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
    ''')

def connect_to_database():
    # Connection and cursor for sqlite
    folder_path = 'PythonForEverybody_Course_Book/0.Files_Examples/databases/'
    db_name = 'MusicalTracks.sqlite'
    full_path = folder_path + db_name

    print('Connection to database:', full_path, sep = '\n  ')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    print('Connected to database')

    create_tables_if_not_exist(cur)
    print('Creates tables if they not exist')
    
    return (conn, cur)


def get_file_handle():
    file_path = ''
    fh = open(file_path)

    return fh

def getClearDataForDatabase(data):
    # Get list of domains by re findall
    list_orgs = re.findall('From [a-zA-Z0-9]\S*@(\S*[a-zA-Z])', data)
    
    # put them in dict, and count them
    dict_orgs = dict()
    for domain in list_orgs:
        dict_orgs[domain] = dict_orgs.get(domain, 0) + 1
    
    return dict_orgs

def updateDatabase(data):
    n = 1
    for organisation, count in data.items():
        cur.execute('''INSERT INTO Counts (org, count)
            VALUES (?, ?)''', (organisation, count))
        if n > 9:
            conn.commit()
            print(' ', n, 'orgs commited')
            n = 1
            continue
        n += 1
    else:
        conn.commit()
        print('  Last', n-1, 'org(s) commited')
        
def checkDataInDataBase():
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 3'
    print('Top 3 orgs:')
    for row in cur.execute(sqlstr):
        print(' ', str(row[0]), row[1])

main()
