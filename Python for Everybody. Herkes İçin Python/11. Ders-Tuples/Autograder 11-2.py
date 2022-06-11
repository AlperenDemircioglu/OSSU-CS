name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"


lst = list()

x = dict()

newdict = x.items()

newlist = list()
try:
    handle = open(name)
    for line in handle:
         first= line.strip()
         if not first.startswith('From'): continue
         fifth = line.split()
         if len(fifth) == 7:
             lst.append(fifth[5][0:2])



    for line in lst:
        x[line] = x.get(line,0)+1 # x = x +1

    for key, value in newdict:
        newlist.append((key, value))

    z = sorted(newlist)

    for key, value in z:
        print(key, value)
except:
    print("Bad file name")
