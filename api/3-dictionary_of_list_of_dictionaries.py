#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to fetch data about all employees
and exports a summary of their tasks to a JSON file.
"""

import json
import requests


def export_all_to_json():
    user_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = user_response.json()

    all_tasks = {}
    for user in users_data:
        employee_id = user['id']
        employee_name = user['name']

        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        todos_data = todos_response.json()

        tasks = []
        for task in todos_data:
            tasks.append({
                "username": employee_name,
                "task": task['title'],
                "completed": task['completed']
            })

        all_tasks[employee_id] = tasks

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    export_all_to_json()
