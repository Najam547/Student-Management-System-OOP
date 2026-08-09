import storage 
import validators 
import student
def add_student():
    Students = storage.load_students()  
    name = validators.get_valid_name()
    roll_no = validators.get_valid_roll(Students)
    age = validators.get_valid_age()
    marks = validators.get_valid_marks()
    student_obj= student.Student(name,roll_no,age,marks,)
    Students.append(student_obj)
    print("Student Added.")
    storage.save_students(Students)
def search_student() :
    Students = storage.load_students()
    print("1. Search by name.")
    print("2. Search by roll no.")
    while True :
        try :
            choose = int(input("Enter the choice :"))
            break
        except ValueError :
            print("Valid Choice")
    if choose == 1 :
        search = input("Enter the name of student : ")
        search = search.title()
        i = 0
        for student in Students :
            if student.get_name() == search:
                formated_print(student)
                i+=1
        if i==0 :
            print("Nothing matches your search.")
    elif choose == 2 : 
        while True :
            try :
                search = int(input("Enter the roll no : "))
                break
            except ValueError :
                print("Enter the valid Roll number.")
        j=0
        for student in Students :
            if search == student.get_roll_no() :
                formated_print(student)
                j+=1
        if j == 0 :
            print("Nothing matches your search.")
def delete_student():
    Students = storage.load_students()
    if len(Students) == 0:
        print("No student Added.")
    else :
        found=False
        print("1.Delete by name.")
        print("2.Delete by roll no")
        while True :
            try :
                choice = int(input("Enter your choice :"))
                break
            except ValueError:
                print("Enter a valid Choice.")
        if choice == 1 :
            delete = input("Enter the name of student : ")
            delete = delete.title()
            for student in Students :
                if delete == student.get_name() :
                    Students.remove(student)
                    found = True
                    break            
            if found :
                storage.save_students(Students)
                print("Student deleted successfully.")
            else :
                print("Nothing matches the student you want to delete.")
        elif choice == 2 :
            while True :
                try :
                    delete = int(input("Enter the roll no of student : "))
                    break
                except ValueError :
                    print("Enter a valid roll number.")
            for student in Students :
                if delete == student.get_roll_no() :
                    Students.remove(student)
                    found = True
                    break          
            if found :
                storage.save_students(Students)
                print("Student deleted successfully.")
            else :
                print("Nothing matches the student you want to delete.")
        else :
            print("Invalid Input.")  
def display_students():
    Students = storage.load_students()
    if len(Students) == 0:
        print("No student Added.")
    else:
        for student in Students :
            formated_print(student)
def update_student():
    Students = storage.load_students()
    while True :
        try :
            roll_no = int(input("Enter roll no to update: "))
            break
        except ValueError :
            print("You entered an invalid roll number.")
    for student in Students:
        if student.get_roll_no() == roll_no:
            student.set_name(validators.get_valid_name())
            student.set_age(validators.get_valid_age())
            student.set_marks(validators.get_valid_marks())
            storage.save_students(Students)
            print("Student updated successfully.")
            return
    print("Student not found.")
def formated_print(student) :
    print("==========================================")
    print("      Name       :",student.get_name())
    print("      Roll No    :",student.get_roll_no())
    print("      Age        :",student.get_age())
    print("      Marks      :",student.get_marks())
    print("      Result     :",student.get_result())