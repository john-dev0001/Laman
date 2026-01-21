tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(index, "-", task)

def delete_task():
    view_tasks()
    if tasks:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed_task = tasks.pop(task_no - 1)
            print("Deleted task:", removed_task)
        else:
            print("Invalid task number")

def menu():
    while True:
        print("\n--- Laman Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting Laman...")
            break
        else:
            print("Invalid choice")

menu()
