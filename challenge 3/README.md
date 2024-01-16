# Python Challenge Project

## Overview

This repository contains Python scripts for analyzing financial records (PyBank) and election data (PyPoll). The scripts read CSV files, perform analyses, and produce results that are printed to the terminal and exported to text files.

## Project Structure

- `PyBank/`
  - `main.py`: Python script for financial analysis.
  - `Resources/`: Folder containing the CSV file (`budget_data.csv`).
  - `analysis/`: Folder containing the text file with financial analysis results.

- `PyPoll/`
  - `main.py`: Python script for election analysis.
  - `Resources/`: Folder containing the CSV file (`election_data.csv`).
  - `analysis/`: Folder containing the text file with election analysis results.

## Instructions

### PyBank Analysis

The PyBank script analyzes financial records to calculate:

- Total number of months
- Net total amount of "Profit/Losses"
- Changes in "Profit/Losses" over the entire period and the average of those changes
- Greatest increase in profits (date and amount)
- Greatest decrease in profits (date and amount)

The analysis results are printed to the terminal and exported to a text file (`analysis/financial_analysis.txt`).

### PyPoll Analysis

The PyPoll script analyzes election data to calculate:

- Total number of votes cast
- List of candidates who received votes
- Percentage of votes each candidate won
- Total number of votes each candidate won
- Winner of the election based on popular vote

The analysis results are printed to the terminal and exported to a text file (`analysis/election_results.txt`).

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/python-challenge.git
    ```
2. Navigate to the respective folders (`PyBank` or `PyPoll`).
3. Run the respective Python script (`main.py`) for analysis:

   ```bash
   python main.py
   ```
## Requirements

- Python 3.x
- CSV module
