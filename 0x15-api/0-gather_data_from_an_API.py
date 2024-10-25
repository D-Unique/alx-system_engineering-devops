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
    for i, item in enumerate(completed_task):
        print(f"\t{' '}{item['title']}", end="\n"
              if i < len(completed_task) - 1 else "")


if __name__ == "__main__":
    main()

"""

Employee *NAME* is done with tasks(*DONE*/*TOTAL*):
     *TITLE*
     *TITLE*
     *TITLE*


https://jsonplaceholder.typicode.com/users?id=1
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
https://jsonplaceholder.typicode.com/todos?userId=5
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  },
  ]

https://jsonplaceholder.typicode.com/todos?userId=5&completed=true
https://jsonplaceholder.typicode.com/todos?userId=5&completed=false
  """
