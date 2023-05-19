import os
# Challenge 1
path_to_csv = os.path.join("ch_09.csv")
with open(path_to_csv, "r") as txt_csv:
    print(txt_csv.read())