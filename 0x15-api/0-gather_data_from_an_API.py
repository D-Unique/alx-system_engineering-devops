#!/usr/bin/python3
import requests
import sys

"""
This module fetches data from a specified API endpoint.

Args:
    url: The URL of the API endpoint.
    params: Optional dictionary of query parameters.

Returns:
    A JSON object containing the fetched data.
"""

def main():
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
    

if __name__ == "__main__":
    main()
