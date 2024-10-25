#!/usr/bin/python3
"""
This module contains a Python script that returns
information about an employee's TODO list progress,
using this REST API, for a given employee ID
"""
import requests
import sys


id = sys.argv[1]

r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
t = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')
data = r.json()
task = t.json()

count = 0
total = 0
for item in task:
    if item['completed'] is False:
        total += 1
    else:
        total += 1
        count += 1

print(f"Employee {data['name']} is done with tasks({count}/{total})")
for item in task:
    print('\t', end='')
    print(f"{item['title']}")
