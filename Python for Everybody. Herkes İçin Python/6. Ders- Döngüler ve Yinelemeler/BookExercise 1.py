total = 0.0
count = 0

while True:
  data = input('Enter a number:')
  if data == "done": break
  fdata = float(data)
  try:
      total = total + fdata
      count = count+1
      avg = total/count
  except:
      print('Invalid input')
      continue

print(total, count,avg)
