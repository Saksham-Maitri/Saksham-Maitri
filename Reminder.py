import json
from tabulate import tabulate

def loadtasks():
    try:
        with open('tasks.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

def clear_list():
    with open('tasks.txt', 'w') as file:
        json.dump({}, file)

def savetasks(tasks):
    with open('tasks.txt', 'w') as file:
        json.dump(tasks, file)

def add(task,time_frame):
    tasks=loadtasks()
    tasks[task]=time_frame
    savetasks(tasks)

def print_green(text):
    return "\033[92m" + text + "\033[0m"

def completion(task):
    tasks=loadtasks()
    if task in tasks:
        tasks[task] = "Task completed"
        savetasks(tasks)
    else:
        print("Task doesn't exist in the list")

def print_red(text):
    return "\033[91m" + text + "\033[0m"

def print_yellow(text):
    return "\033[93m" + text + "\033[0m"

def could_not(task):
    tasks = loadtasks()
    if task in tasks:
        tasks[task] = "Task could not be completed"
        savetasks(tasks)
    else:
        print("Task doesn't exist in the list")

def remove(task):
    tasks = loadtasks()
    if task in tasks:
        confirmation=input("Are you sure you want to remove the task? (y/n): ")
        if confirmation=="y":
            tasks.pop(task)
            savetasks(tasks)
            print("Task removed successfully.")
        else:
            pass
    else:
        print("Task doesn't exist in the list.")

def view():
    tasks=loadtasks()
    if not tasks:
        print("No tasks available.")
        return
    count=1
    for i in tasks:
        if tasks[i]=="Task completed":
            print(count,".",print_green(i),"  Time duration:","Task completed")
        elif tasks[i]=="Task could not be completed":
            print(count,".",print_red(i),"  Time duration:","Task could not be completed")
        else:
            print(count,".",i,"  Time duration:",tasks[i])
        count+=1


def print_menu():
    menu=[[1,"Add Task"],[2,"View Tasks"],[3,"Task Completion"],[4,"Task could not be completed"],[5,"Remove Task"],[6,"Clear List"],[7,"Exit"]]
    print(tabulate(menu, headers=["Option", "Action"], tablefmt="fancy_grid"))



if __name__=="__main__":
    while True:
        print("\n===== Task Manager =====")
        print_menu()


        choice=input("Enter your choice: ")
        if choice == "1":
            task=input("Enter the task: ")
            time_frame=input("Enter the time frame: ")
            add(task,time_frame)
        elif choice == "2":
            print(print_yellow("===YOUR LIST OF TASKS==="))
            view()
        elif choice == "3":
            task=input("Enter the task: ")
            completion(task)
        elif choice == "4":
            task=input("Enter the task: ")
            could_not(task)
        elif choice == "5":
            task=input("Enter the task: ")
            remove(task)
        elif choice=="6":
            clear_list()
        elif choice == "7":
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Not valid choice. Please enter 1, 2, 3, 4, 5 or 6.")