#!/usr/bin/python3
"""Write a script that returns information, for a given employee ID, about
his/her TODO list
"""
import requests
import sys

employee_id = sys.argv[1]
user_response = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{employee_id}')

data = user_response.json()
employee_name = data['name']

todos_response = requests.get(
    f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
todos_data = todos_response.json()


total_todos = len(todos_data)
ok_todos = sum(1 for task in todos_data if task['completed'])

print(
    f'Employee {employee_name} is done with tasks({ok_todos}/{total_todos}):')

for task in todos_data:
    if task['completed']:
        print('\t ' + task['title'])
