import fileinput

choice = raw_input("What do you want to do? (add, update, delete, or search): ")

if choice == 'Add' or choice == 'add':
    f = open("information.txt", "a+")

    idNum = raw_input("Enter ID Number: ")
    course = raw_input("Enter Course: ")
    first = raw_input("Enter First Name: ")
    middle = raw_input("Enter Middle Name: ")
    last = raw_input("Enter Last Name: ")

    f.write(idNum + " " + course + " " + last + ", " + first + " " + middle + "\n")
    f.close()

elif choice == 'Delete' or choice == 'delete':
    idNum = raw_input("Enter ID Number: ")
    for line in fileinput.input("information.txt", inplace=1):
        line = line.strip()
        if not idNum in line:
            print line

elif choice == 'Search' or choice == 'search':
    f = open("information.txt", "r")
    idNum = raw_input("Enter ID Number: ")
    arr = []
    for line in f:
        arr = line.split()
        if idNum == arr[0]:
            print line

    f.close()

elif choice == 'Update' or choice == 'update':

    idnum = raw_input("Enter current ID Number: ")
    newidnum = raw_input("Enter new ID Number: ")
    course = raw_input("Enter new Course: ")
    first = raw_input("Enter new First Name: ")
    middle = raw_input("Enter new Middle Name: ")
    last = raw_input("Enter new Last Name: ")

    for line in fileinput.input("information.txt", inplace=1):
        if idnum in line:
            line = line.replace(line, idnum + " " + course + " " + last + ", " + first + " " + middle + "\n")
        print line,

