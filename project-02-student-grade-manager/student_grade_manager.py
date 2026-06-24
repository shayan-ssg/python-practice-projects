students = {}

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Find Student")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))

        students[name] = score

        print("Student Added!")

    elif choice == "2":
        for name, score in students.items():
            print(f"{name}: {score}")

    elif choice == "3":
        name = input("Name: ")

        if name in students:
            print(f"{name}: {students[name]}")
        else:
            print("Student Not Found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
