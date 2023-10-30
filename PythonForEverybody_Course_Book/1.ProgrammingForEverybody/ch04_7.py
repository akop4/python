'''
Exercise 7: Rewrite the grade program from the previous chapter using a 
function called computegrade that takes a score as its parameter and returns a 
grade as a string.
'''

def main():
    score = input("Enter Score: ")
    try:
        score = float(score)
    except:
        print('Bad score')
        return
    
    if score > 1.0:
        print('Bad score')
    else:
        computegrade(score)

def computegrade(score):
    if score < 0.6:
        print('F')
    elif score < 0.7:
        print('D')
    elif score < 0.8:
        print('C')
    elif score < 0.9:
        print('B')
    elif score <= 1.0:
        print('A')

main()