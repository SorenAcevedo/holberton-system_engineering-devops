#!/usr/bin/python3
""" Module that use REST API """
import json
import requests


if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'

    response_todo = requests.get(url_todo)
    response_user = requests.get(url_user)

    user = json.loads(response_user.text)
    todo = json.loads(response_todo.text)

    todo_all = {}
    for user_id in range(1, len(user) + 1):
        tasks = [i for i in todo if i.get('userId') == user_id]
        for i in tasks:
            i['task'] = i.pop('title')
            i['username'] = user[user_id - 1].get('username')
            i.pop('id')
            i.pop('userId')
        todo_all[str(user_id)] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(todo_all, f)
