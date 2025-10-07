# def task():
#     tasks = []
#     print("----Welcome to the Task Management App----")
#     total_task = int(input("Enter the task yo want to add: "))
#     for i in range(1,total_task+1):
#         task_name = input("Enter task {i}= ")
#         task.append(task_name)
#     print(f"Today's tasks are\n{tasks}")  
#     while True:
#        operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-stop"))
#        if operation == 1:
#           add = input("Enter task you want to add:")
#           tasks.append(add)
#           print(f"taask {add} has been added successfully....")

#        elif operation == 2:
#            updated_val = input("Enter task you want to update:")
#            if updated_val in tasks:
#                up = input("add new task:")
#                ind = tasks.index(updated_val)
#                tasks[ind ] = up
#                print(f"updated_task{up}")

def task():
    tasks= []
    print("---Welcome to the task management app---")
    total_task=int(input("Enter task you want to add:"))
    for i in range(1,total_task+1):
        task_name=input("Enter task {i}=")
        tasks.eppend(task_name)
    print(f"Today's tasks are\n {task}")    