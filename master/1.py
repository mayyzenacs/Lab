import json
import os


def checking(archive, list):
    if os.path.exists(archive):
        print("json file is ready")
    else:
        with open(archive, "a") as archive:
            json.dumps(archive)
        

todos = {
    "id": "",
    "description": "",
    "status": "",
    "createdAt": "",
    "updateAt": ""
}

archive = "todos_list.json"

checking(archive, todos)