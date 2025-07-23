
while True:
    max_input = input("Enter the maximum number of students: ")
    if max_input.isdigit():
        max_students = int(max_input)
        break
    print(" Please enter a positive number.")

students = []
used_emails = set()

# Main loop
while len(students) < max_students:
    add_student = input("\nDo you want to add a student? (yes/no): ").strip().lower()

    if add_student == "no":
        break
    elif add_student != "yes":
        print(" Please enter 'yes' or 'no'.")
        continue

    # Get and student's name
    while True:
        student_name = input("Enter student's full name: ").strip()
        if " " not in student_name:
            print(" Please enter both first name and surname.")
            continue
        break

    first = student_name.split()[0].capitalize()
    last = student_name.split()[-1].capitalize()
    base_email = f"{first.lower()}.{last.lower()}"
    student_email = f"{base_email}@myschool.armstqb"

    # Ensure unique email
    count = 1
    while student_email in used_emails:
        student_email = f"{base_email}{count}@myschool.armstqb"
        count += 1
    used_emails.add(student_email)

    print(f"Email created: {student_email}")

    # Get student's age
    age_in = input("Enter student's age: ")
    if not age_in.isdigit():
        retry = input("Invalid age! Digits only: ")
        if retry.isdigit():
            age_in = retry
        else:
            print("Still invalid. Skipping this student.")
            continue
    student_age = int(age_in)

    # Age category
    print(f"Name: {student_name}")
    print(f"Age: {student_age}")
    if student_age < 18:
        print(" You are a Primary School student.")
    else:
        print(" You are a College student.")

    # Current year grade
    grade_current = input("Enter grade for current year: ")
    if not grade_current.isdigit():
        retry = input("Invalid input! Digits only: ")
        if retry.isdigit():
            grade_current = retry
        else:
            print(" Still invalid. Skipping this student.")
            continue
    grade_current = int(grade_current)

    # Past year grade
    grade_past = input("Enter grade for past year: ")
    if not grade_past.isdigit():
        retry = input("Invalid input! Digits only: ")
        if retry.isdigit():
            grade_past = retry
        else:
            print(" Still invalid. Skipping this student.")
            continue
    grade_past = int(grade_past)

    average_grade = (grade_current + grade_past) / 2
    print(f"📊 Average Grade: {average_grade}")

    if average_grade < 50:
        print(" Sorry, you failed.")
    else:
        print(" Well done! You passed.")

    # Store student data
    students.append({
        "name": student_name.title(),
        "age": student_age,
        "avg": average_grade,
        "email": student_email
    })

    if len(students) == max_students:
        print(f"\n Reached the maximum of {max_students} students.\n")

# Final
print("\n--- All Students ---")
for s in students:
    print(f"Name: {s['name']}")
    print(f"Age: {s['age']}")
    print(f"Average Grade: {s['avg']}")
    print(f"Email: {s['email']}")
    print("----------------------")