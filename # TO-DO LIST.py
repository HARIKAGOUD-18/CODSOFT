# TO-DO LIST

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            n = int(input("Enter task number to update: "))
            if 1 <= n <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[n - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            n = int(input("Enter task number to delete: "))
            if 1 <= n <= len(tasks):
                tasks.pop(n - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")