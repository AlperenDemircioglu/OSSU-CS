#@author: Alperen Demircioglu
#Program tries to find the cube root of the variable cube with epsilon as margin of error using bisection search
#1. Section: variables are defined
cube = float(input("Please enter a number:"))
epsilon = float(input("Please enter a margin error value:"))
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2
#2. Section, case cube > 1 already exists in the slide
if cube >= 1:
    while abs(guess**3 - cube) >= epsilon:
        if(guess**3 > cube):
            high = guess
        else:
            low = guess
        num_guesses += 1
        guess = (high + low)/2.0
# 3. Section: if value of cube variable is lower than 0, this part of the program starts working.
# Flow is same as above and the only difference is that we have to reverse the guess**3 > cube expression for negative values.
elif cube < 0:
    while abs(guess**3 - cube) >= epsilon:
        if(guess**3 < cube):
            high = guess
        else:
            low = guess
        num_guesses += 1
        guess = (high + low)/2.0
    guess = guess*(-1)
# 4. Section: for case 0
elif cube == 0:
    print('Root of cube is', guess)
# 5. Section: for case 0 <cube< 1
else:
    low = cube
    high = 1
    guess = (high + low)/2.0
    while abs(guess**3-cube) >= epsilon:
        if(guess**3 < cube):
            low = guess
        else:
            high = guess
        num_guesses += 1
        guess = (high + low)/2.0
print(guess, 'is the cube roof of', cube)
print('number of guesses is', num_guesses)
