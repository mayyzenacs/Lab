import json
import os
from datetime import date

todos_list = "todos_list.json"

def load_checker():
    if not os.path.exists(todos_list): 
          return []
    else: 
        with open(todos_list, "r") as archive:
            return json.load(archive)
        
def write(tasks):
    with open(todos_list, "w") as a:
        json.dump(tasks, a)        

def new_task(tasks):
    description = input("Enter a description to your task " )
    status = input("Enter task status " )
    task_id = len(tasks) + 1
    createdAt = date.today()
    updatedAt = date.today()
    task = {
        "id": task_id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt
    }
    tasks.append(task)
    print(f"task ID{task_id} successfully created!")



def main():
    list = load_checker()
    while True:
        print("CLI Task Tracker")
        print( """
            1 - Add new task
            2 - Update task
            3 - Delete task
            4 - View all tasks
            5 - Exit
            """)


        option = int(input("Choose an menu option "))
        if option == 1:
            new_task(list)
            write(list)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            break

main()

