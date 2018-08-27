#!/usr/bin/python3
from requests import get
from sys import argv

"""
    This python script will use the REST API, for given employee id
    Will return information about his/her todo list process

"""


def get_data(employee_id):
    """
        get_data - This script will get data from an API

        employee_id: This represents the employees id

        Return: standard output the employee TODO list progress

    """
    employees = get('https://jsonplaceholder.typicode.com/users/{}'
                    .format(employee_id)).json()

    EMPLOYEE_NAME = employees["name"]
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    to_do_tasks = get("https://jsonplaceholder.typicode.com/todos").json()
    titles = []

    for task in to_do_tasks:
        if task["userId"] == employee_id:
            TOTAL_NUMBER_OF_TASKS += 1
            if task["completed"]:
                NUMBER_OF_DONE_TASKS += 1
                titles.append(task["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, TOTAL_NUMBER_OF_TASKS,
                  NUMBER_OF_DONE_TASKS))

    for title in titles:
        print("\t {}".format(title))

if __name__ == "__main__":
    get_data(int(argv[1]))
