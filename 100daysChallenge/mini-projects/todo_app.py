def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')


def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{status}] {task['task']}")


def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f'Task "{tasks[task_number - 1]["task"]}" marked as completed.')
    else:
        print("Invalid task number.")


def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task["task"]}" is removed.')
    else:
        print("Invalid task number.")


tasks = []

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task description: ")
        add_task(task)
    elif choice == "2":
        print("Current Tasks:")
        view_tasks()
    elif choice == "3":
        print("Tasks to be completed:")
        view_tasks()
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            task_number = int(input("Enter the task number to mark as completed: "))
            complete_task(task_number)
    elif choice == "4":
        print("Tasks to be removed:")
        view_tasks()
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
    elif choice == "5":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")
