from urllib.request import Request, urlopen
import sqlite3
import ssl
import re

# Connection and cursor for sqlite
db_path = 'PythonForEverybody_Course_Book/0.Files_Examples/'
db_path += 'databases/CountOrganisations.sqlite'
print('Connection to database')
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Delete table if exist
cur.execute('DROP TABLE IF EXISTS Counts')
# Create new table if not exist
cur.execute('''
CREATE TABLE IF NOT EXISTS Counts
(org TEXT, count INTEGER)'''
)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def main():
    # Connect and read file from web
    url = 'https://www.py4e.com/code3/mbox.txt'
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    print('Connection to url:\n ', url)
    connection = urlopen(req, context=ctx, timeout=10)
    print('Reading data from url')
    data = connection.read().decode()

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
