fname = input("Enter a file name:")
count = 0
try:
    fhandle = open(fname)
    for line in fhandle:
        count+=1
except:
    if fname == ("na na boo boo"):
        print("old bugger- You have been punk'd!")
    else:
        print("File cannot be opened:", fname)
