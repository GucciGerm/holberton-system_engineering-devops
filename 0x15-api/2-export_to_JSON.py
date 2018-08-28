#!/usr/bin/python3
import json
from json import dump
from requests import get
from sys import argv

"""
    This python script will use the REST API, for given employee id
    Will return information about his/her todo list process
"""


def export_to_json(employee_id):
    """
        export_to_json - This script will export data to the json format

        employee_id: This represents the employees id

        Return: This script will return a dictionary of information

    """

    employees = get('https://jsonplaceholder.typicode.com/users/{}'
                    .format(employee_id)).json()
    USER_ID = employee_id
    USERNAME = employees["username"]
    to_do_tasks = get("https://jsonplaceholder.typicode.com/todos").json()
    titles = []

    records = {}
    records[str(employee_id)] = []

    dictofinfo = {}

    with open("{}.json".format(USER_ID), "w") as json_file:
        for task in to_do_tasks:
            if task["userId"] == employee_id:
                dictofinfo = {}
                dictofinfo["task"] = task["title"]
                dictofinfo["completed"] = task["completed"]
                dictofinfo["username"] = USERNAME
                records[str(employee_id)].append(dictofinfo)
        json.dump(records, json_file)


if __name__ == "__main__":
    export_to_json(int(argv[1]))
