#!/usr/bin/python3
import csv
from requests import get
from sys import argv


"""
    This python script will use the REST API, for given employee id
    Will return information about his/her todo list process

"""


def export_csv(employee_id):
    """
        export_csv - This script will export data in the csv format

        employee_id: This represents the employees id

        Return: csv output the userid, username, completion, title

    """
    employees = get('https://jsonplaceholder.typicode.com/users/{}'
                    .format(employee_id)).json()

    USER_ID = employee_id
    USERNAME = employees["username"]
    to_do_tasks = get("https://jsonplaceholder.typicode.com/todos").json()
    titles = []

    with open("{}.csv".format(USER_ID), "w") as USER_ID_csv:
        writer = csv.writer(USER_ID_csv, quoting=csv.QUOTE_ALL)
        for task in to_do_tasks:
            if task["userId"] == employee_id:
                writer.writerow([USER_ID, USERNAME,
                                 task["completed"], task["title"]])
if __name__ == "__main__":
    export_csv(int(argv[1]))
