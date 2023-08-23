# Function to calculate gross salary
def calculate_gross_salary(basic, grade):
    # Constants
    HRA_PERCENT = 0.20
    DA_PERCENT = 0.50
    ALLOW_A = 1700
    ALLOW_B = 1500
    ALLOW_C = 1300
    PF_PERCENT = 0.11

    # Calculate HRA, DA, Allowance, and PF
    HRA = basic * HRA_PERCENT
    DA = basic * DA_PERCENT
    if grade == 'A':
        allowance = ALLOW_A
    elif grade == 'B':
        allowance = ALLOW_B
    else:
        allowance = ALLOW_C
    PF = basic * PF_PERCENT

    # Calculate gross salary
    gross_salary = basic + HRA + DA + allowance - PF

    return gross_salary

# Input data
basic_A = 10000
grade_A = 'A'
basic_B = 4567
grade_B = 'B'

# Calculate and print gross salary for grade A and B
gross_salary_A = calculate_gross_salary(basic_A, grade_A)
gross_salary_B = calculate_gross_salary(basic_B, grade_B)

print(f"Gross Salary for Grade A: {gross_salary_A}")
print(f"Gross Salary for Grade B: {gross_salary_B}")
