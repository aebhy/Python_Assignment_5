user_input=input("Enter student's name: ")
student_report_dict = {"Alice": 85, "Bob": 90, "Charlie": 78}
if user_input in student_report_dict:
    print(f"{user_input}'s marks : {student_report_dict[user_input]}")
else:
    print("Student not found.")