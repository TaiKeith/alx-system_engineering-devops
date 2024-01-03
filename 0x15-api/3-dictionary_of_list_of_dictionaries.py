#!/usr/bin/python3
"""
This script uses a REST API for all employee IDs and returns information
about their TODO list progress and exports the data in JSON format
"""
import json
from requests import get
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    response = get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                user_id)
        response = get(url)
        tasks = response.json()
        dictionary[user_id] = []

        for task in tasks:
            dictionary[user_id].append({
                                        "task": task.get('title'),
                                        "completed": task.get('completed'),
                                        "username": username
                                        })
    with open("todo_all_employees.json", "w", newline='') as file:
        json.dump(dictionary, file)
