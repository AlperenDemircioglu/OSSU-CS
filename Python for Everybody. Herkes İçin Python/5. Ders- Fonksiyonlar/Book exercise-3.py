
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

"""
Exercise 3: Move the function call back to the bottom and move the definition of
print_lyrics after the definition of repeat_lyrics. What happens when you run this program?
Answer: I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
It works
"""
