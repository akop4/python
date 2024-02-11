import re
'''
Write a program which repeatedly reads numbers until the user enters “done”.
Once “done” is entered, print out the total, count, and average of the 
numbers. If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''

def main():
    usr_input = get_usr_input()
    if len(usr_input) == 0:
        print(0, 0, 0)
    else:
        total, count, average = compute_numbers_in_list(usr_input)
        print(f'Total: {total}, Count: {count}, Average: {average}')

def get_usr_input():
    result = list()
    while True:
        usr_inp = input('Enter integer number: ')
        if usr_inp.lower() == 'done': break
        re_usr_inp = re.findall('[-.0-9]+', usr_inp)
        if len(re_usr_inp) == 1:
            result.append(float(re_usr_inp[0]))
        else:
            print('Bad input!')
    
    return result

def compute_numbers_in_list(lst_numbers):
    total = sum(lst_numbers)
    count = len(lst_numbers)
    average = total / count

    return total, count, average

main()