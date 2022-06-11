# Use the file name mbox-short.txt as the file name
#@author: Alperen Demircioglu
#1. Section: Get the file with input and store it into fname variable
#open fname and store it into fh variable
#assign count and total variables to zero
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
#2. Section: File may be too big so we do not use read and use for loop instead to get each line
#find method is used to find the location of the 0 and we store location into index variables
#if condition makes it so that if the line does not start with X-DSPAM-Confidence, loop continues to the next line
#count variable is increased by 1 if the line starts with X-DSPAM-Confidence.
#value that comes after X-DSPAM-Confidence is added to the total variable
#average is printed 
for line in fh:
    index = line.find('0')
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    total = total + float(line[index:])
print("Average spam confidence:", float(total/count))
