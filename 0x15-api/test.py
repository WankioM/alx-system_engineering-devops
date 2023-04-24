#!/usr/bin/python3
"""Takes an employee ID. And returns the to do list """

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit()

employee_id = sys.argv[1]

# Make a GET request to retrieve the employee's TODO list
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

# Parse the JSON response
todos = response.json()

# Count the number of completed tasks and the total number of tasks
completed_tasks = 0
total_tasks = len(todos)
completed_task_titles = []

for todo in todos:
    if todo["completed"]:
        completed_tasks += 1
        completed_task_titles.append(todo["title"])

# Print the progress report
employee_name = todos[0]["userId"]
print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
for title in completed_task_titles:
    print(f"\t {title}")
