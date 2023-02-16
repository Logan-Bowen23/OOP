import StudentClass as sc

def main():
    student_id = 1001
    name = 'John'
    dob = '10/11/2001'
    classification = 'junior'

    student1 = sc.Student(student_id, name, dob, classification)

    student1.calc_age()
    student1.calc_register()

    print(f'Student age is: {student1.get_age()}')
    print(f'Student can register between {student1.get_register}')
main()
