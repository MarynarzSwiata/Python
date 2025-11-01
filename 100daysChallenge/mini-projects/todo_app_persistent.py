import json
from colorama import Fore, Style, init

init(autoreset=True)

TASK_FILE = "100daysChallenge/mini-projects/tasks.json"


def add_task(tasks_list, task_description):
    tasks_list.append({"task": task_description, "completed": False})
    print(Fore.GREEN + f'Task "{task_description}" added.')


def view_tasks(tasks_list):
    if not tasks_list:
        print(Fore.RED + "No tasks found.")
    else:
        for idx, task in enumerate(tasks_list, start=1):
            status = Fore.GREEN + "✓" if task["completed"] else Fore.RED + "✗"
            print(f"{idx}. [{status}] {task['task']}")


def complete_task(tasks_list, task_number):
    if 0 < task_number <= len(tasks_list):
        tasks_list[task_number - 1]["completed"] = True
        print(
            Fore.GREEN
            + f'Task "{tasks_list[task_number - 1]["task"]}" marked as completed.'
        )
    else:
        print(Fore.RED + "Invalid task number.")


def remove_task(tasks_list, task_number):
    if 0 < task_number <= len(tasks_list):
        removed_task = tasks_list.pop(task_number - 1)
        print(Fore.GREEN + f'Task "{removed_task["task"]}" is removed.')
    else:
        print(Fore.RED + "Invalid task number.")


def save_tasks(tasks_list):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks_list, f, indent=4)


def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            tasks = json.load(f)
            file_name = f.name.rsplit(".", 1)[0]
        return tasks, file_name
    except FileNotFoundError:
        print(Fore.RED + "File not Found.")
        return [], None


tasks, file_name = load_tasks()

while True:
    print(Fore.YELLOW + f"\nTo-Do List Application. Tasks list loaded: {file_name}")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task description: ")
        add_task(tasks, task)
        save_tasks(tasks)
    elif choice == "2":
        print("Current Tasks:")
        view_tasks(tasks)
    elif choice == "3":
        print("Tasks to be completed:")
        view_tasks(tasks)
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            task_number = int(input("Enter the task number to mark as completed: "))
            complete_task(tasks, task_number)
            save_tasks(tasks)
    elif choice == "4":
        print("Tasks to be removed:")
        view_tasks(tasks)
        if len(tasks) == 0:
            print(Fore.GREEN + "No tasks to remove.")
        else:
            task_number = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_number)
            save_tasks(tasks)
    elif choice == "5":
        print(Fore.BLUE + "Exiting the application.")
        break
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
