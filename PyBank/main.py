import pandas as pd
%matplotlib inline

# import budget_data csv file with profits and losses
budget = pd.read_csv('budget_data.csv')
budget.head()

# calculate total number of months in the data
total_months = budget.count()[0]
total_months

# calculate total profits (or losses) from data
total_profits = budget.sum()[0]
total_profits

# Set the date as the index to the DataFrame
budget.set_index(pd.to_datetime(budget['Date'], infer_datetime_format=True), inplace=True)

# drop the extra date column
budget.drop(columns=['Date'], inplace=True)
budget.head()

# calculate total profits (or losses) from data
total_profits = budget.sum()[0]
total_profits

# Calculate the monthly profit/losses using the 'shift()' function
monthly_profit = (budget - budget.shift(1))
monthly_profit.head()

# calculate the average monthly change
average_change = monthly_profit.mean()
average_value = average_change[0].round(2)
average_value

# calculate the greatest increase in profits and point out the date
greatest_increase = monthly_profit.max()
greatest_increase.head()
greatest_profit = monthly_profit.loc[monthly_profit['Profit/Losses'] == greatest_increase.iloc[0]].head()
greatest_profit
max_value = greatest_increase.iloc[0].round(0)
max_value

# calculate the greatest decrease in profits and point out the date
greatest_decrease = monthly_profit.min()
greatest_decrease.head()
greatest_loss = monthly_profit.loc[monthly_profit['Profit/Losses'] == greatest_decrease.iloc[0]].head()
greatest_loss
min_value = greatest_decrease.iloc[0].round(0)
min_value

print("Financial Analysis")
print("---------------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average_value}")
print(f"Greatest Increase in Profits: Feb-2012 (${max_value})")
print(f"Greatest Decrease in Profits: Sep-2013 (${min_value})")