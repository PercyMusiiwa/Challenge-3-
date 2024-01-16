import csv
import os

# Here we set the file path
file_path = os.path.join("Resources", "budget_data.csv")

# Initialization of variables
total_months = 0
total_profits_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Store the header row

    # Iterate through rows
    for row in csvreader:
        # Update total months and total profits/losses
        total_months += 1
        total_profits_losses += int(row[1])

        # Calculate profit/loss change
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_loss_changes.append(profit_loss_change)
        dates.append(row[0])

        # Update previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = sum(profit_loss_changes[1:]) / (total_months - 1)

# Find the greatest increase and decrease
greatest_increase = max(profit_loss_changes)
greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

# Print results to the terminal
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits_losses}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results to a text file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profits_losses}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
