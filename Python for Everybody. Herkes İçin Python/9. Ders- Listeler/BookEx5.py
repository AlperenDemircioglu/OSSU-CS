'''
MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by
early email servers and desktop apps. Without getting into too many details, MBOX is a text file, which
stores emails consecutively. Emails are separated by a special line which starts with From (notice the space).
Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a
separator.
Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts
the number of emails.

Write a program to read through the mail box data and when you find line that starts with “From”, you will
split the line into words using the split function. We are interested in who sent the message, which is
the second word on the From line.
'''

result = []

try:
    '''1. Section: To get the file with input statement, if nothing is entered use mbox file.
    open the file and store it into fname
    '''
    fname = input("Please enter file name:")
    if len(fname) < 1:
        fname = "mbox-short.txt"
    fhand = open(fname)
    """2. Section: I want to find the lines in the fhand which starts with 'From' word.
    If the line is blank or the line does not start with 'From' continue to the next line
    if it does, split the line and store it as a list in the words variable.
    append the index#1 item in the words into the result list.
    """
    for line in fhand:
        if len(line) == 0 or line[:4] != 'From' : continue
        words = line.split()
        result.append(words[1])
except:
    print("File cannot be found or opened")
print(result)
