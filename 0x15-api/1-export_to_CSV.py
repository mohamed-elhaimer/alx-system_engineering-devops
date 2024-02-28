#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    tasks = [t.get("title") for t in todos if t.get("completed") is True]
    user_id = sys.argv[1]
    username = user.get('username')
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        content = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [content.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
