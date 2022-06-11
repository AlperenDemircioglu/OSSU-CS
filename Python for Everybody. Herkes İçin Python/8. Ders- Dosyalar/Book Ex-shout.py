#@author: Alperen Demircioglu
#1. Get the file, 2. open the file and store it into fhandle
#3. try and except structure for insurance
#4. file might be too big to fit in main memory so we use a for loop to make each line uppercase and store into nfname
fname = input("Enter a file name:")
fhandle = open(fname)
nfname = ""
try:
    for line in fhandle:
        nfname = nfname + line.upper()
except:
    print("File cannot be processed:", fname)
print(nfname)
