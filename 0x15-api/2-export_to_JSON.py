#!/usr/bin/python3
""" Module that export data in the JSON format """
import requests
from sys import argv
import json


if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'

    response_todo = requests.get(url_todo)

    todo = json.loads(response_todo.text)

    tasks = [i for i in todo if i['userId'] == int(argv[1])]

    with open(argv[1] + '.json', 'w') as f:
        dict = {argv[1]: tasks}
        json.dump(dict, f)
