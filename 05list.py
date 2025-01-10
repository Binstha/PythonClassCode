# Create a list of your income in last 12 months.
# Calculate the total income, average income.

monthly_income = [22000, 22000, 22000, 22000, 22000, 22000, 45000, 22000, 22000, 23000, 22000, 24000]

# Calculate the yearly income
yearly_income = sum(monthly_income)

# Calculate the average income
average_income = yearly_income / len(monthly_income)

# Output
print("=================================================")
print(f"{'               Income Summary             ':^}")
print("=================================================")
print(f"{'Total Yearly Income'}              : Rs {yearly_income:,.2f}")
print(f"{'Average Income'}                   : Rs  {average_income:>,.2f}")
print("=" * 50)
