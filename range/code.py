
'''
write a simple python program tht register the name of student and their score'''
#add
#delete
#show
#exit
#is should be able to print out their grade in scores
total_students = dict()
choice = None

while choice != '0':
    print('''
                    student and score

                    0 - Exit
                    1 - list Students and their score
                    2 - Add student using their score
                    3 - Remove a
        ''')

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye")

    # list students and their score
    elif choice == "1":
        print("List of Students")
        for student in total_students:
            print(student, total_students[student], sep="\t")
    # add students to the existing table
    elif choice == "2":
        student = (input("Give me the student name? "))
        score = (input("Give me the student score? "))
        total_students[student] = score
        if int(score) in range(70, 100):
            print(student, 'Result is A')

        elif int(score) in range(60, 69):
            print (student, 'Result is B')
        elif int(score) in range(50, 59):
            print(student, 'Result is C')
        elif int(score) in range(45, 49):
            print (student, 'Result is D')
        elif int(score) in range(40, 45):
            print(student, 'Result is E')
        elif int(score) in range(0, 39):
            print(student, 'Result is F, very Bad')
        else:
            print('You failed Woefully', student)

    # remove student using their score
    elif choice == "3":
        student = (input("Remove which state student? "))
        if student in total_students:
            del total_students[student]
        else:
            print(student, "isnt in your student list.")
    else:
        print("sorry, buy", choice, "isnt a valid choice")
