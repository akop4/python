'''
Exercise 1: Write a while loop that starts at the last character in the string
and works its way backwards to the first character in the string, printing each
letter on a separate line, except backwards.
'''
def main():
    words = getListWordsForReverse()
    result = [reverseWord(word) for word in words]
    print('\n'.join(result))

def getListWordsForReverse():
    return [
        'test',
        'teXt',
        'Zettelkasten',
        'Spider'
    ]

def reverseWord(text):
    last_char = len(text)
    curr_char = 1
    result = list()

    while curr_char != last_char+1:
        simb_char = text[curr_char*-1]
        simb_char = simb_char.upper() if curr_char == 1 else simb_char.lower()
        result.append(simb_char)
        curr_char += 1

    result = ''.join(result)
    return ' '.join([text, 'became', result])

main()