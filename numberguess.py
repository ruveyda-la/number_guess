import random
# x = random.randint(1,100)
x=55

def numberguess(low_guess, high_guess):

    line_input = int(input('Enter a number-> '))
    
    if line_input ==x:
        print('Congratulations!')
        return x
    elif (line_input >100) or  (line_input<1):
        print("invalid number")
    elif line_input>x:
        print(f'Number is between {low_guess} and {line_input}')
        high_guess=line_input
    elif line_input<x:
        print(f'Number is between {line_input} and {high_guess}')
        low_guess=line_input
    numberguess(low_guess,high_guess)
numberguess(1,100)
