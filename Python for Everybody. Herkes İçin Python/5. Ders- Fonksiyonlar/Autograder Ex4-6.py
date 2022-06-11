def computepay(h, r):

    if h > 40:
        return (h-40)*rate*(1.5) + 40*rate
    else:
        return h*r

try:
 hrs = float(input("Enter Hours:"))
 rate = float(input("Enter Rate:"))
 p = computepay(hrs, rate)
 print("Pay", p)
except:
 print('Please enter int or float')
