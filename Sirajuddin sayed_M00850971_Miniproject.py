# Student management System
'''
This is a student management system in which the user will have multiple options including adding multiple student
records. Records can be searched using the MISIS number(also known as 'roll') and viewed in a tabular form. Using the
menu we can delete any student record. The user can exit the program once he/she is done using it. The program
consists of arrays to store student details. The program also includes loops(if/else/elif) that continues to run until
 the end of the array.
  '''
# Function for adding the student details
#using 'roll' as a replacement for MISIS in code
def addNew(roll, name, marks1, marks2, marks3):
    # Taking input of student details
    rollNo = int(input("Please Enter MISIS M00  : "))  #student MISIS/roll number
    stuName = str(input("Please Enter Your Name : "))
    mks1 = int(input("Please Enter Marks 1   : "))
    mks2 = int(input("Please Enter Marks 2   : "))
    mks3 = int(input("Please Enter Marks 3   : "))
    # Appending the details in the arrays
    roll.append(rollNo)
    name.append(stuName)
    marks1.append(mks1)
    marks2.append(mks2)
    marks3.append(mks3)
    # Displaying message after adding the details
    print("Data Added Successfully")

# Function for searching the student details
def searchStu(roll, name, marks1, marks2, marks3):
    # Taking input for the MISIS number
    no = int(input("Please Enter the MISIS of the Student : "))
    # Taking temporary variable for checking if the MISIS number exists or not
    flag = 0
    # Running for loop till the end of the MISIS number array
    for i in range(0, len(roll)):
        # Checking if the MISIS number exists or not
        if (roll[i] == no):
            # Incrementing the flag if the MISIS number found
            flag = flag + 1
            # Printing the details of the student
            print("MISIS Of Student : ", roll[i])
            print("Name Of Student : ", name[i])
            print("Marks 1 Of Student : ", marks1[i])
            print("Marks 2 Of Student : ", marks2[i])
            print("Marks 3 Of Student : ", marks3[i])
            print("==============================")
            print("Total Marks        : ", (marks1[i] + marks2[i] + marks3[i]))
    # If flag is 0 then it means that the student is not found
    if (flag == 0):
        print("MISIS Number Not Found.")   #error message for not finding the correct record
    # Else student is found
    else:
        print("Data Of Student Displayed.")
    print()


# Function for deleting the student details
def deleteStu(roll, name, marks1, marks2, marks3):
    # Taking input for the roll number
    no = int(input("Please Enter the roll number of the Student : "))
    # Taking temporary variable for checking if the roll number exists or not
    flag = 0
    # Running for loop till the end of the MISIS number array
    for i in range(0, len(roll)):
        # Checking if the MISIS number exists or not
        if (roll[i] == no):
            # Incrementing  the flag if the MISIS number found
            flag = flag + 1
            # Printing the details of the student
            print("MISIS No Of Student M00 : ", roll[i])
            print("Name Of Student : ", name[i])
            print("Marks 1 Of Student : ", marks1[i])
            print("Marks 2 Of Student : ", marks2[i])
            print("Marks 3 Of Student : ", marks3[i])
            print("==============================")
            print("Total Marks        : ", (marks1[i] + marks2[i] + marks3[i]))
            print()
            # Confirming from user to delete student details
            s = str(input("Are you sure you want to delete(y/n) : "))
            # If the user says yes then deleteing the details from the array and breaking the loop
            if (s == "y"):
                roll.pop(i)
                name.pop(i)
                marks1.pop(i)
                marks2.pop(i)
                marks3.pop(i)
                break
            # If the user says no then exiting the loop
            else:
                flag = 2
                break
    if (flag == 0):
        print("MISIS Number Not Found.")
    elif (flag == 1):
        print("Data Of Student Deleted Successfully.")
    print()

# Function for displaying the menu
def menu():
    print("*******************************")
    print("** Student Management System **")
    print("*******************************")
    print("** 0. Exit                   **")
    print("** 1. Add New Student        **")
    print("** 2. Search Student         **")
    print("** 3. Delete Student         **")
    print("*******************************")

# Project function to call menu function and decide which function to call
def project(roll, name, marks1, marks2, marks3):
    # Running infinite loop so that user can use options multiple times
    while (True):
        print()
        print()
        # Calling the menu function from which user can choose
        menu()
        # Taking the input of user choice
        ch = int(input("Please Enter Your Choice : "))
        # If the user chooses 0 then we will exit the program
        if (ch == 0):
            print("Thank you for using")
            break
        # If the user chooses 1 then we will call the add function
        elif (ch == 1):
            addNew(roll, name, marks1, marks2, marks3)
        # If the user chooses 2 then we will call search function
        elif (ch == 2):
            searchStu(roll, name, marks1, marks2, marks3)
        # If the user chooses 3 then we will delete function
        elif (ch == 3):
            deleteStu(roll, name, marks1, marks2, marks3)
        # If the user enters something else, displaying the message
        else:
            print("Wrong Input!")

# Creating the arrays for storing the data
roll = list()
name = list()
marks1 = list()
marks2 = list()
marks3 = list()

# Calling the main function and passing arrays as parameters
project(roll, name, marks1, marks2, marks3)
