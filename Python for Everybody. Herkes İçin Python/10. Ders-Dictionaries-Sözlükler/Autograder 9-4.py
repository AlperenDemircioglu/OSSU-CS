name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

x = dict()

k = list()

for line in handle:
 y = line.rstrip()
 if not line.startswith('From '): continue
 words = line.split()
 k.append(words[1])

for line in k:
 x[line] = x.get(line,0)+1 # x = x +1

bigcount = None
email_address = None

for key,value in x.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        email_address = key

print(email_address, bigcount)
