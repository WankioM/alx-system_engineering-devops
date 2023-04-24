#!/usr/bin/python3
"""Takes one employee info to csv"""

import csv
import json
import sys
import urllib.request

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    with urllib.request.urlopen(url + "users/{}".format(user_id)) as response:
        user = json.loads(response.read().decode())
    username = user.get("username")
    with urllib.request.urlopen(url + "todos?userId={}".format(user_id)) as response:
        todos = json.loads(response.read().decode())

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
