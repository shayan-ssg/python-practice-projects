while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        task = input("Enter task: ")

        with open("tasks.txt", "a") as f:
            f.write(task + "\n")

        print("Task Added!")

    elif choice == "2":
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()

            print("\nTasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

        except FileNotFoundError:
            print("No tasks found!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
