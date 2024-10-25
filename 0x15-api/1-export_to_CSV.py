Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
Example:


import csv

# Sample data
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Specify the filename
filename = "my_data.csv"

# Write the data to the CSV file
with open(filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)

print(f"Data exported to {filename}")
