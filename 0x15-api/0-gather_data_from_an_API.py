#!/usr/bin/python3
"""Takes an employee ID. And returns the to do list """

import json
import sys
import urllib.request

url = "https://jsonplaceholder.typicode.com/"
with urllib.request.urlopen(url + "users/{}".format(sys.argv[1])) as response:
    user = json.loads(response.read().decode())

with urllib.request.urlopen(url + "todos?userId={}".format(sys.argv[1])) as response:
    todos = json.loads(response.read().decode())

completed = [t.get("title") for t in todos if t.get("completed") is True]
print("Employee {} is done with tasks({}/{}):".format(
    user.get("name"), len(completed), len(todos)))
[print("\t {}".format(c)) for c in completed if True]

