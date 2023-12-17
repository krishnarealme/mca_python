from kris import add_student,calculate_marks,display_student
number_of_students=int(input("Enter Number of students: "))
students_list=[]

for k in range(number_of_students):
    reg_no=input("Enter student registration number: ")
    name=input("Enter student name: ")
    marks_str=input("Enter sem1 marks seperated by spaces: ")
    sem1_marks=list(map(int,marks_str.split()))
    add_student(reg_no,name,sem1_marks)

display_option=input("How to display student details(ALL/SPECIFIC): ")
if display_option.upper()=='ALL':
    display_student()
else:
    specific_reg_no=int(input("Enter the registration number: "))
    display_student(specific_reg_no)
