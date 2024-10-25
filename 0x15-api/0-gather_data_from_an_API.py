#!/usr/bin/python3
"""
This module fetches data from a specified API endpoint.

Args:
    url: The URL of the API endpoint.
    params: Optional dictionary of query parameters.

Returns:
    A JSON object containing the fetched data.
"""
import requests
import sys


def main():
    """my func"""
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com'
    user = f'users/{id}'
    userdata = requests.get(f'{url}/{user}').json()
    taskdata = requests.get(f'{url}/{user}/todos').json()
    completed_task = requests.get(f'{url}/{user}/todos?completed=true').json()

    count = 0
    total = 0
    for item in taskdata:
        if item['completed'] is False:
            total += 1
        else:
            total += 1
            count += 1
    print(f"Employee {userdata['name']} is done with tasks({count}/{total}):")

    for item in completed_task:
        print('\t', end=' ')
        print(f"{item['title']}")


if __name__ == "__main__":
    main()
