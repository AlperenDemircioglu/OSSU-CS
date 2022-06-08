cube = float(input("Please enter a number:"))
epsilon = float(input("Please enter a margin error value:"))
guess = 0
increment = float(input("Please enter an increment value:"))
num_guesses = 0
if cube > 1:
    while abs(guess**3 - cube) >= epsilon:
        if(guess**3 > cube):
            high = guess
        else:
            low = guess
        num_guesses += 1
        guess = (high + low)/2.0
print 'num_guesses=', num_guesses
print guess, 'is close to the cube root of', cube
