import os

def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_todo_list():
    if os.path.exists("todo_list.txt"):
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour To-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List is empty.")

def add_task():
    task = input("\nEnter the task: ")
    with open("todo_list.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def remove_task():
    view_todo_list()
    if os.path.exists("todo_list.txt"):
        task_number = int(input("\nEnter the number of the task to remove: "))
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
            with open("todo_list.txt", "w") as file:
                file.writelines(tasks)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
