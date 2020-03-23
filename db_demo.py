import sqlite3
import pandas as pd
from pandas import DataFrame
from Student import Student



#make connection to StudentDB database
conn = sqlite3.connect('StudentDB.sqlite')

#allows to python code to execute SQL statements
c = conn.cursor()

#create the Student table if it hasn't been created
StudentDB = """CREATE TABLE IF NOT EXISTS Students(
StudentId INTEGER PRIMARY KEY, FirstName VARCHAR(32), LastName VARCHAR(32), GPA NUMERIC, Major VARCHAR(16), FacultyAdvisor VARCHAR(32), isDeleted INTEGER
)"""

#populating StudentDB.sqlite with Student table
c.execute(StudentDB)

#function to print menu
def printMenu():
    print("welcome to the Student database app. Below are the following options. ")
    print("(a) Display all students and their attributes")
    print("(b) Create students")
    print("(c) Update Students")
    print("(d) Delete Students by StudentId")
    print("(e) Search/Display students by Major, GPA, and Advisor")


#function to print the table
def optionA():
    print("Displaying all students: ")
    #SQLite query to select all attributes from all students
    c.execute("SELECT * FROM Students")

    #commiting changes to the table
    conn.commit()

    #store data from table as tuples in variable all_rows
    all_rows = c.fetchall()
    #for each tuple in list, print tuple
    #each tuple has the attributes for each student
    for row in all_rows:
        print(row)


#function to create a new student
def optionB():
    #ask user for first name, last name, gpa, major, and facuty advisor of new student
    First = input("Enter first name of Student: ")
    Last = input("Enter last name of Student: ")
    gpa = float(input("Enter the GPA of the student"))
    major = input("Enter major of Student: ")
    advisor = input("Enter the Student's of advisor ")
    deleted = int(input("Enter '1' if student is deleted or '0' if student is not deleted"))
    print("creating student...")

    #executing SQLite query of inserting new student with the attributes the user entered
    c.execute("INSERT INTO Students('FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'isDeleted')"
              "VALUES (?,?,?,?,?,?)", (First, Last, gpa, major, advisor, deleted))

    #commit changes
    conn.commit()

#function to update a student's  major and advisor
def optionC():
    #ask user for the Student ID of the student they want to update
    stud = int(input("Enter the ID of the student whose information you want to update."))
    print("you can update the student's major and faculty advisor.")

    #user enters new major and new faculty advisor
    maj = input("Enter the student's new major: ")
    faculty = input("Enter the student's new faculty advisor: ")

    #query updates major and faculty advisor of the studentId which the user entered
    #update keyword makes sure that not every student record in table is updated
    c.execute("UPDATE Students SET Major = ? WHERE StudentId = ?", (maj, stud,))
    c.execute("UPDATE Students SET FacultyAdvisor = ? WHERE StudentId = ?", (faculty, stud,))

    # commit changes
    conn.commit()

#function to delete a student from table, soft delete
def optionD():
    # ask user for the Student ID of the student they want to delete
    studToDelete = int(input("Enter the ID of the student who you want to delete from the table"))

    #query will change isDeleted status to 1, which is considered to be true for if the student is deleted
    #this is a soft delete, the student record is still in the table
    c.execute("UPDATE Students SET isDeleted = ? WHERE StudentId = ?", (1, studToDelete,))

    #to show that student is deleted, execute query where isDeleted is 0, which will return students that are not deleted
    c.execute("SELECT * FROM Students WHERE isDeleted = 0")

    #commit changes
    conn.commit()

    # store data from table as tuples in variable data
    data = c.fetchall()
    # for each tuple in list, print tuple
    for row in data:
        print(row)

#function to search students by either major, gpa, or faculty advisor
def optionE():
    #ask user what they want to enter to search for a student
    queryChoice = input("would you like to search for students depending on 'major', 'gpa', or 'advisor'?")
    if queryChoice == "major":
        majorQuery = input("Enter the major you want to search ")

        #selects all student records that have the major which the user entered
        c.execute("SELECT * FROM Students WHERE Major = ?", (majorQuery,))

        #commit changes
        conn.commit()

        # store data from table as tuples in variable data
        data = c.fetchall()
        # for each tuple in list, print tuple
        for row in data:
            print(row)
    elif queryChoice == "gpa":
        #cast gpa as a float so that the GPA in the sqlite table will be a numeric
        qpaQuery = float(input("Enter the gpa you want to search "))

        # selects all student records that have the GPA which the user entered
        c.execute("SELECT * FROM Students WHERE GPA = ?", (qpaQuery,))

        #commit changes
        conn.commit()

        # store data from table as tuples in variable data
        data = c.fetchall()
        # for each tuple in list, print tuple
        for row in data:
            print(row)
    elif queryChoice == "advisor":
        advisorQuery = input("Enter the advisor you want to search ")

        # selects all student records that have the faculty advisor which the user entered
        c.execute("SELECT * FROM Students WHERE FacultyAdvisor = ?", (advisorQuery,))

        #commit changes
        conn.commit()

        # store data from table as tuples in variable data
        data = c.fetchall()
        # for each tuple in list, print tuple
        for row in data:
            print(row)




#starting program
printMenu()

#set choice to null value to entire while loop
choice = None

#keep asking user what to do until they enter 'exit'
while (choice!="exit"):
    choice = input("what would you like to do? To choose an option, enter 'a', 'b', 'c', 'd', or 'e'. To exit, enter 'exit' ")
    if choice == "a":
        #show all students and their attributes
        optionA()
    elif choice == "b":
        #create new student
        optionB()
    elif choice == "c":
        #update student information
        optionC()
    elif choice == "d":
        #delete students - soft delete
        optionD()
    elif choice == "e":
        #search/display results by major, gpa, advisor
        optionE()



