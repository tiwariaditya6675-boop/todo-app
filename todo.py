tasks = []


def show_menu():
    print("\n===== MY TO-DO LIST =====")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Quit")
    print("=========================")


def view_tasks():
    print("\n--- YOUR TASKS ---")

    if len(tasks) == 0:
        print("No tasks yet! Add some tasks first.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

    print("------------------")


def add_task():
    task = input("Enter the task you want to add: ")

    task = task.strip()

    if task == "":
        print("You didn't type anything! Task not added.")
    else:
        tasks.append(task)
        print(f"Task added: '{task}'")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    choice = input("Enter the task NUMBER you want to delete: ")

    try:
        task_number = int(choice)

        if task_number < 1 or task_number > len(tasks):
            print("That number is not valid. Please try again.")
        else:
            index = task_number - 1
            removed_task = tasks.pop(index)
            print(f"Deleted task: '{removed_task}'")

    except ValueError:
        print("Please enter a valid number, not letters!")


if __name__ == "__main__":

    print("Welcome to your To-Do List App!")
    print("This app helps you track your daily tasks.")

    while True:

        show_menu()

        user_choice = input("Enter your choice (1/2/3/4): ")

        if user_choice == "1":
            view_tasks()

        elif user_choice == "2":
            add_task()

        elif user_choice == "3":
            delete_task()

        elif user_choice == "4":
            print("Goodbye! See you later!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")