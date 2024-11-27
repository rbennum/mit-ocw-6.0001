from math import isclose

def calculate_total_month(annual_salary, portion_saved):
    total_cost = 1000000
    portion_down_payment = 0.25
    investment_rate = 0.04
    monthly_salary = annual_salary / 12
    current_savings = 0
    total_month = 0
    semi_annual_raise = 0.07
    while current_savings < total_cost * portion_down_payment:
        current_savings += current_savings * investment_rate / 12
        current_savings += monthly_salary * portion_saved
        total_month += 1
        if total_month % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    return total_month

annual_salary = float(input("Enter your annual salary: "))
a = 0
b = 10000
tolerance = 0.01
iter_max = 10000
iter = 1
savings_rate = 0.0

while iter <= iter_max:
    c = (a + b) / 2
    temp_total_month = calculate_total_month(annual_salary, c / 10000.0)
    if temp_total_month == 36:
        savings_rate = c / 10000.0
        break
    iter += 1
    if temp_total_month < 36:
        b = c
    else:
        a = c

if isclose(savings_rate, 0.0):
    print("It is not possible to pay the down payment in three years.")
else:
    print(f"Best savings rate: {savings_rate:.4f}")
    print(f"Steps in bisection search: {iter}")