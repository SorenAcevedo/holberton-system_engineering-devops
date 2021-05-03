#!/usr/bin/python3
""" Module that export data in the CSV format """
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    url_name = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'

    response_name = requests.get(url_name)
    response_todo = requests.get(url_todo)

    name = json.loads(response_name.text)['name']
    todo = json.loads(response_todo.text)

    tasks = [i for i in todo if i.get('userId') == int(argv[1])]

    with open(argv[1] + '.csv', 'w', newline='') as f:
        for i in tasks:
            csvwriter = csv.writer(f, quoting=csv.QUOTE_ALL)
            csvwriter.writerow(
                [argv[1], name, i.get('completed'), i.get('title')])
