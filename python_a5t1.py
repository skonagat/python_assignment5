# Task 1 : Create a dictionary of student marks

# Step 1: Create a dictionary with student names as keys and marks as values

student_marks = {
    "Rama" : 100,
    "Lakshmana" : 95,
    "Bharatha" : 90,
    "Shatrughna" : 85
}

# Step 2: Ask the user to input a student's name
def std_name():
    global student_name
    student_name = input("Enter the student name: ").strip().lower().upper().capitalize()
    std_marks()

# Step 3 and 4: Retrieve and display marks or show an error message if not found
def std_marks():
    if student_name in student_marks:
        print("{} scored {}".format(student_name, student_marks[student_name]))
    else:
        print("{} is not in the students list".format(student_name))
        std_name()

std_name()
