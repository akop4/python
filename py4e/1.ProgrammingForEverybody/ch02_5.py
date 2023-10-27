import re
'''
Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.
'''

while True:
    celsius_temp = input('Input celsius temperature: ')
    list_celsius_temp = re.findall('[-.0-9]+', celsius_temp)
    if len(list_celsius_temp) == 1:
        fl_celsius_temp = float(list_celsius_temp[0])
        break
    elif len(list_celsius_temp) > 1:
        print('Please write only one temperature!', list_celsius_temp)
    else:
        print('Please write digits, not text!')
    
fahrenheit_temp = fl_celsius_temp * 1.8 + 32
print(str(fl_celsius_temp) + "C is " + str(fahrenheit_temp) + 'F')