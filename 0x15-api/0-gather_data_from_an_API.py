#!/usr/bin/python3
"""Data from an API"""

import requests
import sys


def getInformation(employeeid):
    """Returns information based on ID"""
    url = "https://jsonplaceholder.typicode.com/"
    endpoint = url + 'users/{}'.format(employeeid)
    employee = requests.get(endpoint).json()
    taskendpoint = url + 'TODOs?userId={}'.format(employee.get('id'))
    tasks = requests.get(taskendpoint).json()
    data = {"employee": employee, "tasks": tasks}
    totalTasks = len(data['tasks'])
    tasks = [task for task in data['tasks'] if task['completed']]
    completedTasks = len(tasks)
    print('Employee {} is done with tasks({}/{}):'
          .format(data['employee']['name'], completedTasks, totalTasks))
    for task in tasks:
        print('\t {}'.format(task['title']))


if __name__ == '__main__':
    getInformation(sys.argv[1])