portion_down_payment = 0.25
current_savings = 0
r = 0.04 


starting_annual_salary = input("Enter your starting annual salary:")
portion_saved = input("Enter the percent of your salary to save, as a decimal:")
monthly_salary = starting_annual_salary/12

print monthly_salary


total_cost =input("Enter the cost of your dream home:")
down_payment = total_cost *portion_down_payment

semi_annual_raise = input("Enter the semi_annual raise, as a decimal:")

n=0

while current_savings< down_payment:
	if n>0 and (n%6) == 0:
		starting_annual_salary = starting_annual_salary*(1+semi_annual_raise)
		monthly_salary = starting_annual_salary/12
		current_savings = current_savings +portion_saved*monthly_salary+current_savings*r/12
		n += 1
	else:
		current_savings = current_savings +portion_saved*monthly_salary+current_savings*r/12
		monthly_salary = starting_annual_salary/12
		n += 1





print monthly_salary
print "Number of months:", n
