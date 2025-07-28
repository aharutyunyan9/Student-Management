import os

students = []
used_emails = set()

manual = input("Do you want to enter student data manually? (yes/no): ")

if manual == "yes":
    while True:
        max_input = input("Enter the maximum number of students: ")
        if max_input.isdigit():
            max_students = int(max_input)
            break
        print(" Please enter a positive number.")

    # Main loop
    while len(students) < max_students:
        add_student = input("\nDo you want to add a student? (yes/no): ")

        if add_student == "no":
            break
        elif add_student != "yes":
            print(" Please enter 'yes' or 'no'.")
            continue

        # Get student's name
        while True:
            student_name = input("Enter student's full name: ").strip()
            if " " not in student_name:
                print("Please enter both first name and surname.")
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

        print(f" Email created: {student_email}")

        # Get student's age
        age_in = input("Enter student's age: ")
        if not age_in.isdigit():
            retry = input(" Invalid age! Digits only: ")
            if retry.isdigit():
                age_in = retry
            else:
                print(" Still invalid. Skipping this student.")
                continue
        student_age = int(age_in)

        # Age category
        print(f"Name: {student_name.title()}")
        print(f"Age: {student_age}")
        if student_age < 18:
            print(" You are a Primary School student.")
        else:
            print("🎓 You are a College student.")

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
        print(f" Average Grade: {average_grade:.2f}")

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

elif manual == "no":
    file_path = input("Enter the full path to 'StudentsList.txt': ")

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            parts = [p.strip() for p in line.strip().split(",")]

            if len(parts) != 5:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            first_name = parts[0].capitalize()
            last_name = parts[1].capitalize()
            full_name = f"{first_name} {last_name}"

            try:
                age = int(parts[2])
                grade_past = int(parts[3])
                grade_current = int(parts[4])
            except ValueError:
                print(f"Invalid numeric data in line: {line.strip()}")
                continue

            base_email = f"{first_name.lower()}.{last_name.lower()}"
            email = f"{base_email}@myschool.armstqb"
            count = 1
            while email in used_emails:
                email = f"{base_email}{count}@myschool.armstqb"
                count += 1
            used_emails.add(email)

            average_grade = (grade_past + grade_current) / 2

            students.append({
                "name": full_name,
                "age": age,
                "avg": average_grade,
                "email": email
            })

        print(f"\n Loaded {len(students)} students from file.\n")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

else:
    print("⚠️ Invalid choice. Please enter 'yes' or 'no'.")
    exit()


#  Display Report
print("\n --- All Students ---")
for s in students:
    print(f"Name: {s['name']}")
    print(f"Age: {s['age']}")
    print(f"Average Grade: {s['avg']:.2f}")
    print(f"Email: {s['email']}")
    print("----------------------")

# Write to Report File
report_path = "/Users/anushharutyunyan/Desktop/PythonCourse/Student managment system/StudentsReport.txt"
with open(report_path, "w") as report:
    for s in students:
        report.write(f"Name: {s['name']}\n")
        report.write(f"Age: {s['age']}\n")
        report.write(f"Average Grade: {s['avg']:.2f}\n")
        report.write(f"Email: {s['email']}\n")
        report.write("----------------------\n")

print(f"\n Student data saved to '{report_path}'")