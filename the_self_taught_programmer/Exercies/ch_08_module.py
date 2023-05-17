import random
#if __name__ == "__main__":
def challenge_1():
    return "Let's play the game!"

def challenge_2(max_range_of_numbers = None):
    
    """Let's your computer to guess number

    Take maximum range for numbers and right number and return list with try results

    Args:
    max_range_of_numbers:
        :int: Maximum range for numbers

    Returns:
    Return list with try results
    """

    try_list = list()
    if max_range_of_numbers == None or type(max_range_of_numbers) != type(1):
        try_list.append('Game over! Check your input! Only integer!')
        return try_list
    right_number = random.randint(1, max_range_of_numbers)
    try_list.append('Right number for this round: ' + str(right_number))
    low = 1
    high = max_range_of_numbers - 1
    try_count = 0
    while True:
        mid = int(low + high) // 2
        if int(mid) == right_number:
            try_list.append(str(mid) + ' is right number\n' 
                            + 'You are win in ' + str(try_count) + ' steps')
            break
        elif int(mid) > right_number:
            try_list.append(str(mid) + ' is too big')
            high = mid - 1
        else:
            try_list.append(str(mid) + ' is too small')
            low = mid + 1
        try_count += 1
    return try_list