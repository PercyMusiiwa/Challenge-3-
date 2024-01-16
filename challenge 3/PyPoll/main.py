import csv
import os

# Set the file path
file_path = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Store the header row

    # Iterate through rows
    for row in csvreader:
        # Update total votes
        total_votes += 1

        # Update candidates' votes
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Print results to the terminal
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    # Check for the winner
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate
print("----------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")

# Export results to a text file
output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("----------------------------------------\n")
    for candidate, votes in candidates.items():
        vote_percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("----------------------------------------\n")
