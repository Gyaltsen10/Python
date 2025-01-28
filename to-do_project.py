# To-Do List Application

# Global list to store tasks
tasks = []

# Function to view tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("\nEnter the task to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("Task cannot be empty. Please try again.")

# Function to remove a task
def remove_task():
    view_tasks()  # Show tasks before asking which one to remove
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("\nNo tasks to remove.")

# Main menu function
def main_menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    print("Welcome to the To-Do List Application!")
    main_menu()
