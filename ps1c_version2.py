#!/usr/bin/env


portion_down_payment = 0.25
current_savings = 0
r = 0.04 
semi_annual_raise = .07
total_cost  = 1000000
down_payment = total_cost *portion_down_payment

starting_annual_salary = input("Enter your starting salary:")


a=0
b=1
c=(a+b)/2.0
s=1


def calculating_c_and_s():

	def calculating_current_savings(n,savings,annual_salary,rate):
		n = 0
		while n<36:
			if n>0 and (n%6) == 0:
				annual_salary = annual_salary*(1+semi_annual_raise)
				monthly_salary = annual_salary/12
				savings = savings +rate*monthly_salary+savings*r/12
				n += 1

			else:
				monthly_salary = annual_salary/12
				savings = savings +rate*monthly_salary+savings*r/12
				n += 1

		global current_savings
		current_savings = savings

	global current_savings

	calculating_current_savings(0,current_savings,starting_annual_salary,1)

	if current_savings < down_payment:
		print "It is not possible to pay the down payment in three years."
		exit(1)


	current_savings = 0
	annual_salary = starting_annual_salary

	global c

	calculating_current_savings(0,current_savings,starting_annual_salary,c)


	while abs(current_savings- down_payment) >100 :

		global a 
		global b

		if (current_savings- down_payment) >100:
			b = c

		else :
			a = c


		c = (a+b)/2.0
	
		current_savings  = 0

		calculating_current_savings(0,current_savings,starting_annual_salary,c)

		global s
		s += 1

calculating_c_and_s()



print "Best saving rate:", round(c, 4) 
print "Steps in bisection search",s