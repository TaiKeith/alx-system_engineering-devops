#!/usr/bin/python3
"""
This script uses a REST API for a given employee ID and returns information
about his/her TODO list progress and exports the data in CSV format
"""
import csv
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

    with open(f"{user_id}.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['User_ID', 'Username', 'Completed', 'Title'])

        for task in tasks:
            csv_writer.writerow([user_id, username, task.get("completed"),
                                task.get("title")])
