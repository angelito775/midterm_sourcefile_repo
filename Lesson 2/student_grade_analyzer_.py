"""Student Grade Analyzer - Starter Code

Complete every section marked TODO. Keep this file and grades.txt in the
same folder. Rename the completed file to student_grade_analyzer_.py.
"""

from fileinput import filename


def classify_grade(grade):#classify_grade function takes a grade as input and returns the classification and status of the grade.
    """Return the classification and status of a grade."""
    
    if grade >= 90:
        return "Excellent", "Passed"
    elif grade >= 85:
        return "Very Good", "Passed"
    elif grade >= 80:
        return "Good", "Passed"
    elif grade >= 75:
        return "Satisfactory", "Passed"
    else:
        return "Needs Improvement", "Failed"
 # TODO: Use if/elif/else and return (classification, status).
 
 

def load_students(filename):#load_students function reads student records from a text file and returns them as a list of dictionaries.
    """Read valid student records from a text file and return them as a list."""

    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                clean_line = line.strip()                    
                if not clean_line:
                    continue

                parts = clean_line.split(",")          
                if len(parts) != 3:
                    continue                               
                                                
                try:
                    grade = float(parts[2].strip())
                    if 0 <= grade <= 100:
                        students.append(
                            {
                                "student_id": parts[0].strip(),
                                "name": parts[1].strip(),
                                "grade": grade,
                            }
                        )
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"\nError: The file '{filename}' was not found.")

    return students

    # TODO: Open filename safely by using with open(...) and try/except.
    # TODO: Loop through the file, clean each line, and skip blank lines.
    # TODO: Split each record and check that it contains three fields.
    # TODO: Convert and validate the grade.
    # TODO: Append a dictionary for every valid record.
def calculate_statistics(students):#       """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        total_grade += student["grade"]
        classification, status = classify_grade(student["grade"])

        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if student["grade"] > highest_student["grade"]:
            highest_student = student

        if student["grade"] < lowest_student["grade"]:
            lowest_student = student

    average = total_grade / len(students)

    return {
        "total": len(students),
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student,
    }

    # TODO: Use one loop to update the accumulator, counters, highest, and lowest.
    # Do not use sum(), max(), or min() for this part.

    # TODO: Calculate the average and return all results in a dictionary.



def display_students(students):
    """Display all student records in a formatted table."""
    print(
        f"\n{'ID':<12} | {'Name':<20} | {'Grade':<6} | {'Classification':<18} | {'Status'}"
    )
    print("-" * 75)

    for student in students:
        classification, status = classify_grade(student["grade"])
        # Use slicing to shorten names longer than 20 characters
        name_display = student["name"][:20]
        print(
            f"{student['student_id']:<12} | {name_display:<20} | {student['grade']:<6.2f} | {classification:<18} | {status}"
        )

    # TODO: Print column headings.
    # TODO: Loop through students and call classify_grade for each record.



def display_statistics(statistics):
    """Display the calculated class statistics."""

    if not statistics:
        return
        
    print("\nCLASS STATISTICS")
    print(f"Number of students: {statistics['total']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    print(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}")
    print(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}")
    # TODO: Display every value in statistics clearly.



def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""

    matches = []
    keyword_lower = keyword.lower().strip()

    for student in students:
        if keyword_lower in student["name"].lower() or keyword_lower in student["student_id"].lower():
            matches.append(student)

    # TODO: Make keyword lowercase and remove extra whitespace.
    # TODO: Use a loop and partial, case-insensitive matching.

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    try:
            with open(filename, 'w') as file:
                file.write("STUDENT GRADE REPORT\n")
                file.write("====================\n\n")
                
                for student in students:
                    classification, status = classify_grade(student["grade"])
                    file.write(f"{student['student_id']} | {student['name']} | {student['grade']:.2f} | {classification} | {status}\n")
                    
                file.write("\nCLASS STATISTICS\n")
                file.write("----------------\n")
                file.write(f"Number of students: {statistics['total']}\n")
                file.write(f"Class average: {statistics['average']:.2f}\n")
                file.write(f"Passed: {statistics['passed']}\n")
                file.write(f"Failed: {statistics['failed']}\n")
                file.write(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}\n")
                file.write(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}\n")
                
            print(f"\nReport successfully saved to {filename}")
    except OSError as e:
            print(f"\nError saving report: {e}")


    # TODO: Safely open filename in write mode.
    # TODO: Write all student results and statistics.
    # TODO: Handle a possible OSError.
   


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
                display_students(students)
        elif choice == '2':
                display_statistics(statistics)
        elif choice == '3':
                keyword = input("\nEnter student name or ID to search: ")
                matches = search_student(students, keyword)
                if matches:
                    display_students(matches)
                else:
                    print("No matching students found.")
        elif choice == '4':
                save_report(students, statistics, "grade_report.txt")
        elif choice == '5':
                print("\nExiting program. Goodbye!")
                break
        else:
                print("\nInvalid choice. Please enter a number from 1 to 5.")
                continue
        # TODO: Call the appropriate function for choices 1 to 4.
        # TODO: For choice 3, ask for a keyword and display every match.
        # TODO: Use break for choice 5.
        # TODO: Use continue after an invalid choice.


if __name__ == "__main__":
    main()
