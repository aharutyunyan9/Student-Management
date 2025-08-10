import logging

logging.basicConfig(
    filename="student_app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    students = []
    used_emails = set()

    manual = input("Do you want to enter student data manually? (yes/no): ").strip().lower()
    logging.info(f"User selected manual input: {manual}")

    if manual == "yes":
        students = get_students_manual(used_emails)
    elif manual == "no":
        students = get_students_from_file(used_emails)
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        logging.error(f"Invalid manual input choice: {manual}")
        return

    print_students(students)
    save_report(students)

def get_students_manual(used_emails):
    students = []
    max_students = get_positive_int("Enter the maximum number of students: ")
    logging.info(f"Max students to input manually: {max_students}")

    while len(students) < max_students:
        if input("\nDo you want to add a student? (yes/no): ").strip().lower() != "yes":
            logging.info("User chose to stop adding students manually.")
            break

        name = get_full_name()
        email = generate_unique_email(name, used_emails)
        age = get_positive_int("Enter student's age: ")
        print_age_category(age)

        grade_current = get_positive_int("Enter grade for current year: ")
        grade_past = get_positive_int("Enter grade for past year: ")

        avg = (grade_current + grade_past) / 2
        print(f"Average Grade: {avg:.2f}")
        print("Well done! You passed." if avg >= 50 else "Sorry, you failed.")
        logging.info(f"Added student: {name}, Age: {age}, Avg Grade: {avg:.2f}, Email: {email}")

        students.append({
            "name": name,
            "age": age,
            "avg": avg,
            "email": email
        })

    return students

def get_students_from_file(used_emails):
    students = []
    file_path = input("Enter the full path to 'StudentsList.txt': ").strip()
    logging.info(f"Loading students from file: {file_path}")

    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = [p.strip() for p in line.strip().split(",")]

                if len(parts) != 5:
                    print(f"Skipping invalid line: {line.strip()}")
                    logging.warning(f"Invalid line skipped: {line.strip()}")
                    continue

                try:
                    age = int(parts[2])
                    grade_past = int(parts[3])
                    grade_current = int(parts[4])
                except ValueError:
                    print(f"Invalid numeric data in line: {line.strip()}")
                    logging.warning(f"Invalid numeric data skipped: {line.strip()}")
                    continue

                full_name = f"{parts[0].capitalize()} {parts[1].capitalize()}"
                email = generate_unique_email(full_name, used_emails)
                avg = (grade_past + grade_current) / 2

                students.append({
                    "name": full_name,
                    "age": age,
                    "avg": avg,
                    "email": email
                })

        print(f"\nLoaded {len(students)} students from file.\n")
        logging.info(f"Loaded {len(students)} students from file successfully.")
    except FileNotFoundError:
        print(" File not found. Please check the path.")
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"Error reading file {file_path}: {e}")

    return students

def get_full_name():
    while True:
        name = input("Enter student's full name: ").strip()
        if " " in name:
            formatted_name = " ".join([p.capitalize() for p in name.split()])
            logging.debug(f"Full name entered: {formatted_name}")
            return formatted_name
        print("Please enter both first name and surname.")

def generate_unique_email(full_name, used_emails):
    first, last = full_name.split()[0], full_name.split()[-1]
    base_email = f"{first.lower()}.{last.lower()}"
    email = f"{base_email}@myschool.armstqb"

    count = 1
    while email in used_emails:
        email = f"{base_email}{count}@myschool.armstqb"
        count += 1
    used_emails.add(email)
    print(f"Email created: {email}")
    logging.debug(f"Generated unique email: {email}")
    return email

def get_positive_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            logging.debug(f"Positive integer received: {value}")
            return int(value)
        print("Please enter a positive number.")

def print_age_category(age):
    if age < 18:
        print("You are a Primary School student.")
        logging.debug("Age category: Primary School student")
    else:
        print(" You are a College student.")
        logging.debug("Age category: College student")

def print_students(students):
    print("\n--- All Students ---")
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Average Grade: {s['avg']:.2f}")
        print(f"Email: {s['email']}")
        print("----------------------")
    logging.info(f"Printed {len(students)} students.")

def save_report(students):
    report_path = "StudentsReport.txt"
    try:
        with open(report_path, "w") as report:
            for s in students:
                report.write(f"Name: {s['name']}\n")
                report.write(f"Age: {s['age']}\n")
                report.write(f"Average Grade: {s['avg']:.2f}\n")
                report.write(f"Email: {s['email']}\n")
                report.write("----------------------\n")
        print(f"\nStudent data saved to '{report_path}'")
        logging.info(f"Student data saved to report: {report_path}")
    except Exception as e:
        print(f"Error saving report: {e}")
        logging.error(f"Error saving report: {e}")

if __name__ == "__main__":
    main()