try:
 hrs = input("Enter Hours:")
 h = float(hrs)
 rate = input("Enter Rate:")
 r = float(rate)
 if h <= 40:
    print(hrs*r)
 else:
    print(40*r + (h-40)*r*(1.5))
except:
 print('Please enter int or float')
