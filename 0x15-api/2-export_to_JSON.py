#!/usr/bin/python3
"""
 extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]
    username = user.get('username')
    with open("{}.json".format(user_id), "w", newline="") as f:
        content = json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username,
        } for t in todos]}, f)
