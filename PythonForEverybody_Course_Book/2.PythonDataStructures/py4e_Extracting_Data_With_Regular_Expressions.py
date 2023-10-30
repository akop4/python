import re

def main():
    reg_line = "[0-9]+"
    file_list = ["py4e-data.dr-chuck.net_regex_sum_42.txt", "py4e-data.dr-chuck.net_regex_sum_1885536.txt"]
    for file_name in file_list:
        print(sum_int_in_file(open(file_name).read(), reg_line))

def sum_int_in_file(text, reg_line):
    return sum([int(i) for i in re.findall(reg_line, text)])

main()
