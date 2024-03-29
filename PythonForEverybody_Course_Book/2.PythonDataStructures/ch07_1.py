"""
7.1 Write a program that prompts for a file name, then opens that file and 
reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.

You can download the sample data at http://www.py4e.com/code3/words.txt
"""
# Use words.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1: 
    fname = "PythonForEverybody_Course_Book/0.Files_Examples/words.txt"
fh = open(fname)

for line in fh:
    print(line.strip().upper())
