'''
9.4 Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail. The
program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to
find the most prolific committer.
'''
fname = input("Enter file: ")
if len(fname) < 1: fname = "PythonForEverybody_Course_Book/0.Files/mbox-short.txt"
handle = open(fname)
emails = {}
for line in handle:
    if not line.startswith('From:'): continue
    words = line.split()
    emails[words[1]] = emails.get(words[1], 0) + 1
b_word, b_count = None, -1
for k, v in emails.items():
    if b_word == None or v > b_count: b_word, b_count = k, v
print(b_word, b_count)
