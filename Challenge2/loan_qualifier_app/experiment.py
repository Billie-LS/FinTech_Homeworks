from ast import If
import questionary


def prompt_user_inputs():
    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text(
        "What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score, debt, income, loan_amount, home_value = validate_user_inputs(
        credit_score, debt, income, loan_amount, home_value)

    return credit_score, debt, income, loan_amount, home_value


# internal operation/hidden validation criteria
# this will screen to check if applicant's individual
# credit score is compatible with the minimum value
# listed by the banks from daily_rate_sheet.csv
def validate_user_inputs(credit_score, debt, income, loan_amount, home_value):
    if int(credit_score) >= 600:
        credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)
    return credit_score, debt, income, loan_amount, home_value
