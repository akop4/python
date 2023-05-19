# import os
'''cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''
# Challenge 1
with open("ch_09.txt", "r") as txt_csv:
    print(txt_csv.read())