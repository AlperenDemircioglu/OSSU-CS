# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    index = line.find('0')
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    total = total + float(line[index:])
print("Average spam confidence:", float(total/count))
