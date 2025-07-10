while True:
    max_input = input("Enter the maximum number of students: ")
    if max_input.isdigit():
        max_students = int(max_input)
        break
    print("Please enter a positive number.")

students = []

while len(students) < max_students:
    add_student = input("Do you want to add a student? (yes/no): ")

    if add_student == "no":
        break
    elif add_student != "yes":
        print("Please enter 'yes' or 'no'.")
        continue

    student_name = input("Enter student name: ")

    age_in = input("Enter age: ")
    if age_in.isdigit():
        student_age = int(age_in)
    else:
        retry = input("Invalid age! Digits only: ")
        if retry.isdigit():
            student_age = int(retry)
        else:
            print("Still invalid. Skipping this student.")
            continue

    if student_age < 18:
        print("Name:", student_name)
        print("Age:", student_age)
        print("You are a Primary School student.")
    else:
        print("Name:", student_name)
        print("Age:", student_age)
        print("You are a College student.")

    grade_current = input("Enter grade for current year: ")
    if grade_current.isdigit():
        grade_current = int(grade_current)
    else:
        retry = input("Invalid input! Digits only: ")
        if retry.isdigit():
            grade_current = int(retry)
        else:
            print("Still invalid. Skipping this student.")
            continue
    grade_past = input("Enter grade for past year: ")
    if grade_past.isdigit():
        grade_past = int(grade_past)
    else:
        retry = input("Invalid input! Digits only: ")
        if retry.isdigit():
            grade_past = int(retry)
        else:
            print("Still invalid. Skipping this student.")
            continue

    average_grade = (grade_current + grade_past) / 2
    print("Average Grade:", average_grade)

    if average_grade < 50:
        print("Sorry, you failed.")
    else:
        print("Well done! You passed.")

    students.append({
        "name": student_name,
        "age": student_age,
        "avg": average_grade
    })

    if len(students) == max_students:
        print(f"\n✅ Reached the maximum of {max_students} students.\n")
print("\n--- All Students ---")
for s in students:
    print("Name:", s["name"])
    print("Age:", s["age"])
    print("Average Grade:", s["avg"])
    print("----------------------")