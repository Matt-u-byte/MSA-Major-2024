
user_hours_worked = 0
while True:
    try:
        user_hours_worked = (float(input("Please enter your hours worked:")))
        if user_hours_worked <= 0 or user_hours_worked >= 24:
            print("ERROR: Please enter an appropriate interger")
            continue              
        else:
            break
    except:
        print("ERROR: Please enter an integer")

user_hourly_wage = 0
while True:
    try:
        user_hourly_wage = (float(input("Please enter your hourly wage:$")))
        if user_hourly_wage <= 0:
            print("ERROR: Please enter an appropriate interger")      
        else:
            break
    except:
        print("ERROR: Please enter an integer")

user_wage_per_day = user_hourly_wage * user_hours_worked
user_amount_of_days_worked = 350
user_wage_before_taxes = user_wage_per_day * user_amount_of_days_worked
tax_percentage = .12
percentage_kept_from_taxes = .88
tax_amount = tax_percentage * user_wage_before_taxes
wage_after_taxes = user_wage_before_taxes * percentage_kept_from_taxes
print()
print("Pay Advice")
print("-------------")
print(f"Hours Worked: {user_hours_worked}")
print(f"Hourly Wage: ${user_hourly_wage}")
print(f"Wages Before Taxes: ${user_wage_before_taxes:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Annual Wage After Taxes: ${wage_after_taxes:.2f}")
