if __name__ == "__main__":
    def challenge_1():
        print("Let's play game!")
    def challenge_2():
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
