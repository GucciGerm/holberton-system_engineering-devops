#!/usr/bin/python3
import json
from json import dump
from requests import get
from sys import argv

"""
    This python script will use the REST API, for all employee id
    Will return information about his/her todo list process
"""


def exporting_all_to_json():
    """
        export_all_to_json - This script will export all data to the json
        format

        Return: This script will return a dictionary of list of dictionaries

    """

    employees = get('https://jsonplaceholder.typicode.com/users/').json()
    to_do_tasks = get("https://jsonplaceholder.typicode.com/todos").json()

    records = {}
    dictofinfo = {}

    with open("todo_all_employees.json", "w") as json_file:
        for user in employees:  # how to go through user ids
            records["{}".format(user["id"])] = []
            for task in to_do_tasks:
                if task["userId"] == user["id"]:
                    dictofinfo = {}
                    dictofinfo["username"] = user["username"]
                    dictofinfo["task"] = task["title"]
                    dictofinfo["completed"] = task["completed"]

                    records["{}".format(user["id"])].append(dictofinfo)
        json.dump(records, json_file)


if __name__ == "__main__":
    exporting_all_to_json()
