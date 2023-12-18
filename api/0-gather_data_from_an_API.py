#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


def get_data(url):
    """Get data from url"""
    response = requests.get(url)
    return response.json()


def get_employee_name(url, employee_id):
    """Get employee name"""
    data = get_data(url)
    for employee in data:
        if employee.get('id') == employee_id:
            return employee.get('name')


def get_employee_tasks(url, employee_id):
    """Get employee tasks"""
    data = get_data(url)
    tasks = []
    for employee in data:
        if employee.get('userId') == employee_id:
            tasks.append(employee.get('completed'))
    return tasks


def get_number_of_done_tasks(tasks):
    """Get number of done tasks"""
    done_tasks = 0
    for task in tasks:
        if task is True:
            done_tasks += 1
    return done_tasks


def get_total_number_of_tasks(tasks):
    """Get total number of tasks"""
    total_tasks = 0
    for task in tasks:
        total_tasks += 1
    return total_tasks


def get_employee_done_tasks(url, employee_id):
    """Get employee done tasks"""
    data = get_data(url)
    tasks = []
    for employee in data:
        if employee.get('userId') == employee_id:
            if employee.get('completed') is True:
                tasks.append(employee.get('title'))
    return tasks


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    employee_id = int(argv[1])
    employee_name = get_employee_name(url, employee_id)
    url = 'https://jsonplaceholder.typicode.com/todos'
    tasks = get_employee_tasks(url, employee_id)
    done_tasks = get_number_of_done_tasks(tasks)
    total_tasks = get_total_number_of_tasks(tasks)
    employee_done_tasks = get_employee_done_tasks(url, employee_id)
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
          done_tasks, total_tasks))
    for task in employee_done_tasks:
        print('\t {}'.format(task))
