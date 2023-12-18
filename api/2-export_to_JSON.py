#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to fetch data
about a specific employee
and exports a summary of the tasks to a JSON file.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    data = user_response.json()
    employee_name = data['name']

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_data = todos_response.json()

    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })

    with open(f'{employee_id}.json', 'w') as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    export_to_json(employee_id)
