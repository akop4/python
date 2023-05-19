import os, csv

# Challenge 1
def reading_txt_file(path_to_file):
    with open(path_to_file, "r") as txt_file:
        print(txt_file.read())
path_to_file = os.path.join('the_self_taught_programmer', 'Exercies', 'ch_09_1.txt')
reading_txt_file(path_to_file)

# Challenge 2
path_to_file = os.path.join('the_self_taught_programmer', 'Exercies', 'ch_09_2.txt')
with open(path_to_file, "w") as txt_file:
    txt_file.write('Challenge 2')
reading_txt_file(path_to_file)

# Challenge 3
list = [['one', 'two', 'three'], ['four', 'five', 'six'], ['seven', 'eight', 'nine']]
path_to_file = os.path.join('the_self_taught_programmer', 'Exercies', 'ch_09_3.txt')
with open(path_to_file, "w") as txt_file:
    csv_file = csv.writer(txt_file,delimiter=',')
    csv_file.writerows(list)
reading_txt_file(path_to_file)