largest = 5
smallest = 5
while True:
    num = input("Enter a number: ")
    if num == "done": break
    try:
      if int(num) > largest :
        largest = int(num)
      if int(num) < smallest :
        smallest = int(num)

    except:
      print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
