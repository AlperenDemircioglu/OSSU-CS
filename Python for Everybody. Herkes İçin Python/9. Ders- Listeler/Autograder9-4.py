fname = input("Enter file name: ")

try:
    fh = open(fname)
    lst = list()

    for line in fh:
        new = line.split()
        for n in range(len(new)):
            if new[n] in lst:
                continue
            else:
                lst.append(new[n])
                lst.sort()
except:
    print("File cannot be opened:", fname)
print(lst)
