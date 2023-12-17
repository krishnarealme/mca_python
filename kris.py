students_list=[]

def add_student(reg_no,name,marks):
    student_directory={'Reg. No.':reg_no,'Name':name,'Marks':marks}
    students_list.append(student_directory)
    print(f"{name} added to the list.")

def calculate_marks(student_marks):
    tot=sum(student_marks)
    average=tot/len(student_marks)
    if average >= 90:
        grade = 'A' 
    elif 80 <= average <= 89:
        grade = 'B'
    elif 70 <= average <= 79:
        grade = 'C'
    elif 60 <= average <= 69:
        grade = 'D'
    else:
        grade = 'NG'
    return tot,average,grade

def display_student(reg_no='ALL'):
    if reg_no=='ALL':
        for student in students_list:
            tot,average,grade=calculate_marks(student['Marks'])
            print(f"Reg No: {student['Reg. No.']},Name: {student['Name']},Total: {tot},Average: {average},Grade: {grade}")
    else:
        for student in students_list:
            if student['Reg. No.']==reg_no:
                tot,average,grade=calculate_marks(student['Marks'])
                print(f"Reg No: {student['Reg. No.']}")
                print(f"Name: {student['Name']}")
                print(f"Total: {tot}")
                print(f"Average: {average}")
                print(f"Grade: {grade}")
                break
            
