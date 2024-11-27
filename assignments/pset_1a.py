annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
investment_rate = 0.04
monthly_salary = annual_salary / 12
current_savings = 0
total_month = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * investment_rate / 12
    current_savings += monthly_salary * portion_saved
    total_month += 1

print(f"Number of months: {total_month}")
