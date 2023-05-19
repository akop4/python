import os
'''cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''
# Challenge 1
path_to_file = os.path.join('the_self_taught_programmer', 'Exercies', 'ch_09_1.txt')
with open(path_to_file, "r") as txt_file:
    print(txt_file.read())

# print('Challenge 1')

# Challenge 2
path_to_file = os.path.join('the_self_taught_programmer', 'Exercies', 'ch_09_2.txt')
with open("ch_09_answer.txt", "w") as txt_file:
    txt_file.write(input('Write text:\n'))
    # print('Challenge 2')
