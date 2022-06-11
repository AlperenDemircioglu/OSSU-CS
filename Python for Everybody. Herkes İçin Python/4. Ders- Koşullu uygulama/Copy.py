total = 0.0
count = 0

while True:

    data = input('Enter a number: ')
    if data == 'done': break

    fdata = float(data)

    try:
        count = count + 1
        total = total + fdata
        avg = total/count
    except:
        print('Invalid input')

print(count, total, avg)
