portion_down_payment = 0.25
current_savings = 0
r = 0.04 


annual_salary = input("Enter your annual salary:")
portion_saved = input("Enter the percent of your salary to save, as a decimal:")
monthly_salary = annual_salary/12


total_cost =input("Enter the cost of your dream home:")
down_payment = total_cost *portion_down_payment

n=0

while current_savings< down_payment:
	current_savings = current_savings +portion_saved*monthly_salary+current_savings*r/12
	n += 1

print "Number of months:", n
