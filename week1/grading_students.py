def grading_students(grades):
    for i, grade in enumerate(grades):
        if grade < 38:
            continue

        if (grade + 1) % 5 == 0:
            grades[i] = grade + 1
        elif (grade + 2) % 5 == 0:
            grades[i] = grade + 2

    return grades



def get_input():
    n = int(input())
    grades = []

    for _ in range(n):
        grade = int(input())
        grades.append(grade)

    return grades


grades = get_input()
print(grading_students(grades))
