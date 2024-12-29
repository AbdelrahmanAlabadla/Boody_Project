# Function to calculate grade based on the average
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Function to generate the report card
def generate_report_card(student_name, subjects, marks):
    # Calculate total marks and average
    total_marks = sum(marks)
    average = total_marks / len(marks)

    # Assign grade based on average marks
    grade = calculate_grade(average)

    # Print the report card
    print(f"Report Card for {student_name}")
    print("-" * 30)
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {marks[i]} marks")
    print("-" * 30)
    print(f"Total Marks: {total_marks} / {len(subjects) * 100}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
    print("-" * 30)

# Step 4: Input
student_name = input("Enter student's name: ")

# List of subjects
subjects = ['Math', 'Science', 'English', 'History', 'Geography']

# Get marks for each subject
marks = []
for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Generate and display the report card
generate_report_card(student_name, subjects, marks)
