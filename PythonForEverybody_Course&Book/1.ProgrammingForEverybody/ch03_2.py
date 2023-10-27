'''
Exercise 2: Rewrite your pay program using try and except so that your program
handles non-numeric input gracefully by printing a message and exiting the
program.
'''
def main():
    hrs = input("Enter Hours: ")
    pay_rate = input('Enter pay rate: ')

    try:
        pay_rate = float(pay_rate)
        h = float(hrs)
        calculate(h, pay_rate)
    except:
        print('Error, please enter numeric input!')
    
def calculate(h, pay_rate):
    over_hrs = 0
    if h > 40:
        over_hrs = h - 40
        h = 40
    print(h * pay_rate + over_hrs * (pay_rate * 0.5 + pay_rate))

main()