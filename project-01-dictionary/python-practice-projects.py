students = {}

while True:
    line = input()

    if line == "End":
        break

    name, score = line.split()
    students[name] = int(score)

print(students)