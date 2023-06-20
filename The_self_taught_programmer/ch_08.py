import ch_08_module

# Challenge 1
print(ch_08_module.challenge_1())

# Challenge 2
results = ch_08_module.challenge_2(10*10)
for result in results:
    print(result)

while input('Again? Y\n') == 'Y':
    results = ch_08_module.challenge_2(10*10)
    for result in results:
        print(result)