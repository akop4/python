'''
10.2 Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the
hour out from the 'From ' line by finding the time and then splitting the
string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
'''

fname = input("Enter file: ")
if len(fname) < 1: 
    fname = "PythonForEverybody_Course_Book/0.Files_Examples/mbox-short.txt"
handle = open(fname)

dct_hours = {}
for line in handle:
    if line.startswith('From '):
        pos = line.find(':')
        hour = line[pos-2:pos]
        dct_hours[hour] = dct_hours.get(hour, 0) + 1

lst_dct_kv = [(k,v) for k,v in dct_hours.items()]
lst_dct_kv.sort()

for k,v in lst_dct_kv:
    print(k, v)