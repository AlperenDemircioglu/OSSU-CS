# Part A: House Hunting
# @author: Alperen Demircioglu
total_cost = float(input("Please enter house cost:"))
annual_salary = float(input("Please enter annual salary:"))
portion_saved = float(input("Please enter saving rate:"))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
yearly_r = 0.04
monthly_r = yearly_r/12
montyhl_salary = annual_salary/12
month_count = 0

while down_payment > current_savings:
    current_savings = current_savings*(1+monthly_r) + montyhl_salary*portion_saved
    month_count +=1
print("In " + str(month_count) + " months, " + str(current_savings) +" is saved")
