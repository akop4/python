# Challenge 1
Chehov = 'Chehov'
for letter in Chehov:
    print(letter)

# Challenge 2
#user_input_1, user_input_2 = input("What are you did yesterday?\n"), input("Where you was yesterday?\n")
user_input_1, user_input_2 = "swimming", "swimming pool"
explanation = "Yesterday i am {} in {}".format(user_input_1, user_input_2)
print(explanation)

# Challenge 3
text_dog = "The dog run away from the cat"
text_dog.capitalize()
print(text_dog)

# Chalenge 4
text_with_questions = "Where is it? Who is it? When is it?"
text_with_questions = text_with_questions.replace("? ","?&")
print(text_with_questions.split("&"))

# Challenge 5
words_in_list = ["The", "dog", "run", "away", "from", "a", "cat", "!"]
joined_string = " ".join(words_in_list).replace(" !", "!")
print(joined_string + "!!")

# Challenge 6
normal_string = "Somebody read a book"
zeroish_string = normal_string.replace("o","0")
print(zeroish_string)

# Challenge 7
mr_mastermind = "Mastermind"
print(mr_mastermind.index("i"))

# Challenge 8
print('Text with "quotes"')

# Challenge 9
print("3" + "3" + "3")
print("7" * 3)

# Challenge 10
double_string = "How are you? Fine."
print(double_string[:double_string.index("?") + 1])