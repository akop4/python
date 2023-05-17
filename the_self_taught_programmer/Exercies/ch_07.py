import random
tv = ['The Breaking bad', 'The big bang theory']
# print(tv)
for i, show in enumerate(tv):
    tv[i] = show.upper()
# print(tv)

anime = ['Berserk', 'Bleach']
lst_anime_tv = tv + anime
# print(lst_anime_tv)
for i, show in enumerate(lst_anime_tv):
    # lst_anime_tv[i] = show.capitalize()
    words_in_name = lst_anime_tv[i].split(' ')
    new_name = ''
    for word in words_in_name:
        new_name += word.capitalize() + ' '
    lst_anime_tv[i] = new_name.strip()
# print(lst_anime_tv)

# for i in range(0,6):
    # print(i)
# for i in range(6,10):
    # print(i)

# Challenge 1
for i in lst_anime_tv:
    print(i)
    break

# Challenge 2
for i in range(25,51):
    print(i)
    break

# Challenge 3
for i in lst_anime_tv:
    print(lst_anime_tv.index(i),i,sep=' | ')
    break

# Challenge 4
max_range = 10 ** 10
rng = random.randrange(1, max_range)
print('Right number:', rng)
low = 1
high = max_range - 1
try_count = 0
while True:
    mid = int(low + high) // 2
    # inp = int(input())
    inp = mid
    # print('input:', inp)
    if inp == 'q':
        print('Exit')
        break
    try:
        if int(inp) == rng:
            print(inp,' is right number\n','You are win in ',try_count,' steps',sep='')
            break
        elif int(inp) > max_range or int(inp) < 1:
            print(inp,'is out of range')
            break
        elif int(inp) > rng:
            print(inp,'is too big')
            high = inp - 1
        else:
            print(inp,'is too small')
            low = inp + 1
    except (ValueError):
        print('Bad value of input')
    try_count += 1

# Challenge 5
list_a, list_b, list_c = [8, 19, 148, 4], [9, 1, 33, 83], []
for i in list_a:
    for j in list_b:
        k = i * j
        list_c.append(k)
        # print(i, '*', j, '=', k)
print(list_c)