import json

employees = [
    {"id": 101, "name": "Ajay", "department": "IT"},
    {"id": 102, "name": "Rahul", "department": "Finance"},
    {"id": 103, "name": "Priya", "department": "HR"}
]

print("Starting employee processing...")

with open("employee_output.json", "w") as file:
    json.dump(employees, file, indent=4)

print("Employee processing completed.")