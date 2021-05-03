#!/usr/bin/python3
""" Module that use REST API """
import requests
from sys import argv
import json


if __name__ == "__main__":
    url_name = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'

    response_name = requests.get(url_name)
    response_todo = requests.get(url_todo)

    name = json.loads(response_name.text)['name']
    todo = json.loads(response_todo.text)

    tasks = [i for i in todo if i.get('userId') == int(argv[1])]
    complete_task = [i for i in tasks if i.get('completed') is True]

    final_response = 'Employee {} is done with tasks({}/{}):'.format(
        name, len(complete_task), len(tasks))

    print(final_response)
    [print('\t ' + i.get('title')) for i in complete_task]
