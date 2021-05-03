#!/usr/bin/python3
""" Module that export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_name = 'https://jsonplaceholder.typicode.com/users/' + argv[1]

    response_todo = requests.get(url_todo)
    response_name = requests.get(url_name)

    todo = json.loads(response_todo.text)
    name = json.loads(response_name.text)['username']

    tasks = [i for i in todo if i.get('userId') == int(argv[1])]
    for i in tasks:
        i['task'] = i.pop('title')
        i['username'] = name
        i.pop('id')
        i.pop('userId')

    with open(argv[1] + '.json', 'w') as f:
        dict = {argv[1]: tasks}
        json.dump(dict, f)
