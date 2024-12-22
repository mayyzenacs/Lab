import json
import os

todos_list = "todos_list.json"

def check():
    if not os.path.exists(todos_list): 
          return "socorro"
    else: 
        with open(todos_list, "r") as archive:
            return json.load(archive)
        
def write(list):
    with open(todos_list, "W") as archive:
        json.dumps(list, archive)        

def new_task():
    description = input("Enter a description to your task" )
    status = input("Enter task status" )



print(check())



