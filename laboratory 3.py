# Welcome the user to the bank
print("\nWelcome to Python Loan Bank!")

# Request for the user monthly salary
monthly_salary = float(input("\nPlease enter your Monthly Salary to proceed: $"))

# Monthly salary decision
qualified_salary = 30000.00

if monthly_salary >= qualified_salary:
  # Display monthly salary qualified
  print(f">>> Your Monthly Salary of ${monthly_salary} is Qualified!")

  # Request for the user loan amount
  loan_amount = float(input("\nPlease enter your Loan Amount to proceed: $"))

  qualified_loan = 10 * monthly_salary

  # Loan amount decision
  if loan_amount <= qualified_loan:
    # Display loan amount qualified
    print(f">>> Your Loan Amount of ${loan_amount} is Qualified!")

    # Request how many months to pay
    month_duration = int(input("\nEnter how many Months to pay: "))

    # Add 10% interest to the loan amount
    loan_interest = 0.1 # 0.1 = 10%
    new_loan = loan_amount + loan_amount * loan_interest

    # Display the transaction details
    print("\n\n\nTransaction Success!" +
          "\n\n======= Transaction Details =======" +
          f"\nMonthly Salary: ${monthly_salary}" +
          f"\nLoan Amount: ${loan_amount}" +
          f"\nLoan Amount w/ Interest: ${new_loan}" +
          f"\nMonths to Pay: {month_duration}\n")
  
  else:
    # Display too high loan request
    print("\nYou are NOT QUALIFIED for a Loan!" +
          f"\n[Reason:] Loan Amount is too high (${loan_amount}).")
    
else:
  # Display too low salary
  print("\nYou are NOT QUALIFIED for a Loan!" +
        f"\n[Reason:] Monthly Salary is amount too low (${monthly_salary}).")