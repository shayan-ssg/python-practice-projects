while True:
    print("\n1. Add Note")
    print("2. Show Notes")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        note = input("Enter note: ")

        with open("notes.txt", "a") as f:
            f.write(note + "\n")

        print("Note Added!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as f:
                print("\nNotes:")
                print(f.read())

        except FileNotFoundError:
            print("No notes found!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
