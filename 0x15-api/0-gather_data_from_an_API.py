#!/usr/bin/python3
"""
This script uses a REST API for a given employee ID and returns information
about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    # Define the URL for the REST API
    url = "https://jsonplaceholder.typicode.com/"

    # Send a GET request to retrieve user info
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # Send a GET request to retrieve the TODO list
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Filter to get completed tasks
    completed = [task.get("title") for task in todos if task.get(
        "completed") is True]

    # Print employee's name, completed tasks and total number of tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print titles of the completed tasks
    for c in completed:
        print("\t {}".format(c))
