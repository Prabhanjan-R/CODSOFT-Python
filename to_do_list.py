# Define a list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("To-Do List is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to update a task
def update_task(index, new_task):
    if index >= 1 and index <= len(tasks):
        tasks[index - 1] = new_task
        print(f"Task {index} updated successfully!")
    else:
        print("Invalid task index.")

# Function to remove a task
def remove_task(index):
    if index >= 1 and index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task {index} ('{removed_task}') removed successfully!")
    else:
        print("Invalid task index.")

def main():
    print("Welcome to the To-Do List App!")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            update_task(index, new_task)
        elif choice == '4':
            index = int(input("Enter the task index to remove: "))
            remove_task(index)
        elif choice == '5':
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
