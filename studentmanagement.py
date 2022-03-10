import sqlite3
from prettytable import PrettyTable
connection = sqlite3.connect("student.db")
listoftable = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='STUDENTDATA' ").fetchall()
if listoftable != []:
    print("Table already exist")
else:
    connection.execute('''CREATE TABLE STUDENTDATA(
                          ID INTEGER PRIMARY KEY AUTOINCREMENT,
                          NAME TEXT,
                          ROLLNO INTEGER,
                          ADMNO INTEGER,
                          EXAMNAME TEXT,
                          ENGLISHMARK INTEGER,
                          MATHSMARK INTEGER,
                          PHYSICSMARK INTEGER,
                          CHEMISTRYMARK INTEGER,
                          BIOLOGYMARK INTEGER
);''')
    print("table created successfully")
while True:
    print("select an option from the menu ")
    print("1. Add student data ")
    print("2. view all students")
    print("3. search a student using partial name")
    print("4. search a student using either admno or rollno")
    print("5. update the student data with admno")
    print("6. delete the student data with admno")
    print("7. display the topper student details of the physics")
    print("8. display the count of total no of student in class")
    print("9. display the average mark of a student scored in english")
    print("10. display the details of all student who scored below average marks in maths")
    print("11. diaplay the details of above average students in chemistry")
    print("12. EXIT")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        getName = input("Enter the Name: ")
        getRollNO = input("Enter the RollNo: ")
        getAdmNo = input("Enter the AdmNo: ")
        getExamName = input("Enter the ExamName: ")
        getEnglishMark = input("Enter the EnglishMark: ")
        getMathsMark = input("Enter the MathsMark: ")
        getPhysicsMark = input("Enter the PhysicsMark: ")
        getChemistryMark = input("Enter the ChemistryMark: ")
        getBiologyMark = input("Enter the BiologyMark: ")

        connection.execute("INSERT INTO STUDENTDATA(Name,RollNo,AdmNo,ExamName,EnglishMark,MathsMark,PhysicsMark,ChemistryMark,BiologyMark)\
                            VALUES('"+getName+"',"+getRollNO+","+getAdmNo+",'"+getExamName+"',"+getEnglishMark+","+getMathsMark+","+getPhysicsMark+","+getChemistryMark+","+getBiologyMark+")")
        connection.commit()
        print("added successfully")
    elif choice == 2:
        result = connection.execute("SELECT * FROM STUDENTDATA")
        table = PrettyTable(["ID","NAME","ROLLNO","ADMNO","EXAMNAME","ENGLISHMARK","MATHSMARK","PHYSICSMARK","CHEMISTRYMARK","BIOLOGYMARK"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
        print(table)
    elif choice == 3:
        getName = input("Enter the partialname to be search: ")
        result = connection.execute("SELECT * FROM STUDENTDATA WHERE name LIKE '%"+getName+"%'")
        table = PrettyTable(["ID", "NAME", "ROLLNO", "ADMNO", "EXAMNAME", "ENGLISHMARK", "MATHSMARK", "PHYSICSMARK", "CHEMISTRYMARK","BIOLOGYMARK"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)
    elif choice == 4:
        getRollNO = input("Enter the rollno to be seaarch: ")
        getAdmNo = input("Enter the admno to be seaarch: ")
        result = connection.execute("SELECT * FROM STUDENTDATA WHERE ROLLNO="+getRollNO+" OR ADMNO="+getAdmNo+"")
        table = PrettyTable(["ID", "NAME", "ROLLNO", "ADMNO", "EXAMNAME", "ENGLISHMARK", "MATHSMARK", "PHYSICSMARK", "CHEMISTRYMARK",
             "BIOLOGYMARK"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)
    elif choice == 5:
        getAdmNo = input("Enter the admno: ")

        getName = input("Enter the Name: ")
        getRollNO = input("Enter the RollNo: ")
        getExamName = input("Enter the ExamName: ")
        getEnglishMark = input("Enter the EnglishMark: ")
        getMathsMark = input("Enter the MathsMark: ")
        getPhysicsMark = input("Enter the PhysicsMark: ")
        getChemistryMark = input("Enter the ChemistryMark: ")
        getBiologyMark = input("Enter the BiologyMark: ")
        result = connection.execute("UPDATE STUDENTDATA SET Name='"+getName+"',RollNo="+getRollNO+",ExamName='"+getExamName+"',EnglishMark="+getEnglishMark+",MathsMark="+getMathsMark+",PhysicsMark="+getPhysicsMark+",ChemistryMark="+getChemistryMark+",BiologyMark="+getBiologyMark+" WHERE admno="+getAdmNo+"")
        connection.commit()
        print("student data updated successfully")
        result = connection.execute("SELECT * FROM STUDENTDATA")
        print("Data Updated")
        table = PrettyTable(["ID", "NAME", "ROLLNO","ADMNO", "EXAMNAME", "ENGLISHMARK", "MATHSMARK", "PHYSICSMARK", "CHEMISTRYMARK",
             "BIOLOGYMARK"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)
    elif choice == 6:
        getAdmNo = input("Enter the admno: ")
        connection.execute("DELETE FROM STUDENTDATA WHERE ADMNO="+getAdmNo)
        connection.commit()
        print("student data deleted successfully")
        result = connection.execute("SELECT * FROM STUDENTDATA")
        print("student data updated")
        table = PrettyTable(["ID", "NAME", "ROLLNO", "ADMNO", "EXAMNAME", "ENGLISHMARK", "MATHSMARK", "PHYSICSMARK", "CHEMISTRYMARK",
             "BIOLOGYMARK"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)
    elif choice == 7:
        result = connection.execute("SELECT * FROM STUDENTDATA WHERE PHYSICSMARK=(SELECT max(PHYSICSMARK) FROM STUDENTDATA)")
        table = PrettyTable(["ID", "NAME", "ROLLNO", "ADMNO", "EXAMNAME", "ENGLISHMARK", "MATHSMARK", "PHYSICSMARK", "CHEMISTRYMARK",
             "BIOLOGYMARK"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)
    elif choice == 8:
        result = connection.execute("SELECT COUNT(*) AS NAME FROM STUDENTDATA")
        for i in result:
            print("Total student count: ",i[0])
    elif choice == 9:
        result = connection.execute("SELECT avg(ENGLISHMARK) as ENGLISHMARK FROM STUDENTDATA")
        for i in result:
            print("Average mark in EnglishMark: ",i[0])
    elif choice == 10:
        result = connection.execute("SELECT * FROM STUDENTDATA WHERE MATHSMARK<(SELECT avg(MATHSMARK) as MATHSMARK FROM STUDENTDATA)")
        table = PrettyTable(["ID", "NAME", "ROLLNO", "ADMNO", "EXAMNAME", "ENGLISHMARK", "MATHSMARK", "PHYSICSMARK", "CHEMISTRYMARK",
             "BIOLOGYMARK"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)
    elif choice == 11:
        result = connection.execute("SELECT * FROM STUDENTDATA WHERE CHEMISTRYMARK>(SELECT avg(CHEMISTRYMARK) as CHEMISTRYMARK FROM STUDENTDATA)")
        table = PrettyTable(["ID", "NAME", "ROLLNO", "ADMNO", "EXAMNAME", "ENGLISHMARK", "MATHSMARK", "PHYSICSMARK", "CHEMISTRYMARK",
             "BIOLOGYMARK"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)
    elif choice == 12:
        connection.close()
        break
    else:
        print("INVALID CHOICE")

