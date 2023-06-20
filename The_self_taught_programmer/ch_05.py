# Chalenge 1
musicians = ["Radio tapok", "Sabaton"]
print(str(type(musicians)) + ':', musicians)

# Chalenge 2
list_with_tuples = [("123","456"),("78",9)]
print(type(list_with_tuples), list_with_tuples)

# Chalenge 3
dict_1 = dict()
dict_1["dog"] = "dog"
dict_1["cat"] = "cat"
print(type(dict_1), dict_1)

# Chalenge 4
def who_better(answer):
    if not answer in dict_1:
        return "idk this animal"
    else:
        return dict_1[answer]

print(who_better('mouse'))
print(who_better('dog'))

# Chalenge 5
dict_musicians = {
    "Sabaton":['Bismark', 'The atack of the dead man'],
    "Radio tapok":["Night witches", "Phantom"]
    }

print(type(dict_musicians), dict_musicians)

# Chalenge 6
set_nums = {1,2,3,3,3,4,5,6}
print(type(set_nums), set_nums)
set_nums.add(8)
print(type(set_nums), set_nums)
set_musicians = set(musicians)
set_musicians.add("Radio tapok")
set_musicians.add("Jan Sibelius")
print(type(set_musicians), set_musicians)
set_musicians.discard("Jan Sibelius")
print(type(set_musicians), set_musicians)
try:
    set_musicians.remove("AC/DC")
except(KeyError):
    print("except KeyError: AC/DC not in set_musicians")
print(type(set_musicians), set_musicians)
poped_musician_in_set = set_musicians.pop()
print(type(set_musicians), set_musicians)
set_musicians.add(poped_musician_in_set)
print(type(set_musicians), set_musicians)

set_all = set_musicians.union(set_nums)
print(type(set_all), set_all)

set_all.clear()
print(type(set_all), set_all)