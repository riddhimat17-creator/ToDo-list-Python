while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # ADD TASK
    if choice == "1":
        task = input("Enter task to add: ")
        with open("hello.txt", "a") as file:
            file.write(task + "\n")
        print("Task added successfully!")

    # VIEW TASKS
    elif choice == "2":
        try:
            with open("hello.txt", "r") as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks found.")
            else:
                print("\nYOUR TASKS ARE:")
                for i, task in enumerate(tasks, start=1):
                    print(i, ".", task.strip())

        except FileNotFoundError:
            print("No tasks file found.")

    # DELETE TASK
    elif choice == "3":
        try:
            with open("hello.txt", "r") as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks to delete.")
            else:
                for i, task in enumerate(tasks, start=1): # here we are distributing tasks with points starting from 1
                    print(i, ".", task.strip())

                task_num = int(input("Enter task number to delete: "))

                if 1 <= task_num <= len(tasks):
                    del tasks[task_num - 1] # as python starts from 0 index we are subtracting 1 for the output to come from 1 not 0
                    with open("hello.txt", "w") as file:
                        file.writelines(tasks)
                    print("Task deleted successfully!")
                else:
                    print("Invalid task number.")

        except FileNotFoundError:
            print("No tasks file found.")

    # EXIT
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice try again..")