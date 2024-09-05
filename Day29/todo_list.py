class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        # Add a new task to the todo list
        task = (task_description, "Incomplete")
        self.tasks.append(task)
        print(f"Task '{task_description}' added successfully!\n")

    def view_tasks(self):
        # Display all tasks with their status
        if not self.tasks:
            print("No tasks in the todo list.\n")
        else:
            print("Your Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                task_description, task_status = task
                print(f"{index}. {task_description} - {task_status}")
            print()

    def mark_task_completed(self, task_number):
        # Mark a specific task as completed
        if 0 < task_number <= len(self.tasks):
            task_description, _ = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = (task_description, "Completed")
            print(f"Task '{task_description}' marked as completed.\n")
        else:
            print(f"Invalid task number: {task_number}. Please choose a valid task.\n")

    def remove_task(self, task_number):
        # Remove a task from the list
        if 0 < task_number <= len(self.tasks):
            task_description, _ = self.tasks.pop(task_number - 1)
            print(f"Task '{task_description}' removed successfully.\n")
        else:
            print(f"Invalid task number: {task_number}. Please choose a valid task.\n")


def display_menu():
    print("Todo List Application")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove a Task")
    print("5. Exit")


def main():
    todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            todo_list.add_task(task_description)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            if todo_list.tasks:
                try:
                    task_number = int(input("Enter the task number to mark as completed: "))
                    todo_list.mark_task_completed(task_number)
                except ValueError:
                    print("Invalid input. Please enter a valid task number.\n")

        elif choice == '4':
            todo_list.view_tasks()
            if todo_list.tasks:
                try:
                    task_number = int(input("Enter the task number to remove: "))
                    todo_list.remove_task(task_number)
                except ValueError:
                    print("Invalid input. Please enter a valid task number.\n")

        elif choice == '5':
            print("Exiting the Todo List Application. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option (1-5).\n")


if __name__ == "__main__":
    main()
