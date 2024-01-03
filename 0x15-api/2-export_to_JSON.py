#!/usr/bin/python3
"""
This script uses a REST API for a given employee ID and returns information
about his/her TODO list progress and exports the data in JSON format
"""
import json
from requests import get
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = get(url)
    username = response.json().get("username")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    response = get(url)
    tasks = response.json()
    dictionary = {user_id: []}

    for task in tasks:
        dictionary[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                                    })
    with open(f"{user_id}.json", "w", newline='') as file:
        json.dump(dictionary, file)
