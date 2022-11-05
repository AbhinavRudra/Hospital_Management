import mysql.connector as sql
from sys import exit
conn = sql.connect(
    host='localhost',
    user='root',
    password='root',
    database='Aster_Database')
c1 = conn.cursor()
print('''
--------------------------------------------------
    WELCOME TO  ASTER-CARE  DATABASE
--------------------------------------------------
''')

def login():
    global choice
    global username
    global password
    choice = input("""CHOOSE:
    =>(1)Login[Enter 1]
    =>(2)Quit[Enter 2]
    => """)
    if choice == "1":
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        print('SUCCESSFULLY LOGGED IN')
    elif choice == "2":
        print("End of program.")
        exit()  # using from sys method

def available_functions():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print('(1)Registering Patient Details')
    print('(2)Registering Doctor Details')
    print('(3)Registering Staff Details')
    print('(4)Total Patient Details')
    print('(5)Total Doctor Details')
    print('(6)Total Staff Details')
    print('(7)Search For Individual Patient Detail')
    print('(8)Search For Individual Doctor Detail')
    print('(9)Search For Individual Staff Detail')
    print('(10)Do You Want to switch to another Account? ')
    print('(11)Exit.')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    global choice_lst
    choice_lst = int(input('ENTER YOUR CHOICE:'))


def chairmain_choices():
    global User_Post
    if choice_lst == 1:
        Patient_Name = input('Enter Patient Name:')
        Patient_Age = int(input('Enter Age:'))
        Patient_Disease_Illness = input('Enter The Problem/Disease:')
        Phone_no = int(input('Enter Phone Number:'))
        sql_patient = 'INSERT into Patient_Details VALUES (%s, %s, %s, %s)'
        P_Details = (Patient_Name, Patient_Disease_Illness, Phone_no)
        c1.execute(sql_patient, P_Details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif choice_lst == 2:
        Doctor_Name = input('Enter Doctor Name:')
        Doctor_Age = int(input('Enter Age:'))
        Doctor_Department = input('Enter the Department:')
        Phone_no = int(input('Enter Phone number:'))
        sql_doctor = 'INSERT into Doctor_Details (Doctor_Name,Doctor_Age,Doctor_Department,Phone_no) VALUES (%s, %s, %s, %s)'
        d_details = (Doctor_Name, Doctor_Age, Doctor_Department, Phone_no)
        c1.execute(sql_doctor, d_details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif choice_lst == 3:
        Staff_Name = input('Enter Staff Name:')
        Staff_Age = int(input('Enter Age:'))
        Work_Description = input('Enter Your Area Of Work:')
        Phone_no = int(input('Enter Phone number:'))
        sql_staff = 'INSERT into Doctor_Details (Doctor_Name,Doctor_Age,Doctor_Department,Phone_no) VALUES (%s, %s, %s, %s)'
        w_details = (Staff_Name, Work_Description, Phone_no)
        c1.execute(sql_staff, w_details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif choice_lst == 4:
        sql_patient = 'SELECT * FROM Patient_Details '
        c1.execute(sql_patient)
        pfile = c1.fetchall()
        for p in pfile:
            print(p)
    elif choice_lst == 5:
        sql_doctor = 'SELECT * FROM Doctor_Details '
        c1.execute(sql_doctor)
        dfile = c1.fetchall()
        for d in dfile:
            print(d)
    elif choice_lst == 6:
        sql_staff = 'SELECT * FROM Staff_Details '
        c1.execute(sql_staff)
        Staff = c1.fetchall()
        for s in Staff:
            print(s)
    elif choice_lst == 7:
        sql_specific_patient = input("Enter Patient Name:")
        patient = 'SELECT * FROM Patient_Details WHERE Patient_Name =("{}")'.format(
            sql_specific_patient)
        c1.execute(patient)
        pfile = c1.fetchall()
        for p in pfile:
            print(p)
    elif choice_lst == 8:
        sql_specific_doctor = input("Enter Doctor Name: ")
        doc = 'SELECT * FROM Doctor_Details WHERE Doctor_Name=("{}")'.format(sql_specific_doctor)
        c1.execute(doc)
        dfile = c1.fetchall()
        for d in dfile:
            print(d)
    elif choice_lst == 9:
        sql_specific_staff = input("Enter Staff Name:")
        staff = 'SELECT * FROM Staff_Details WHERE staff_Name=("{}")'.format(sql_specific_staff)
        c1.execute(staff)
        wfile = c1.fetchall()
        for w in wfile:
            print(w)
    elif choice_lst == 10:
        User_Post = input('''What Do you Work as In Aster Care? :
    =>(1)Chairman[Enter 1]
    =>(2)Doctor[Enter 2]
    =>(3)Staff[Enter 3]
    =>(4)Patient[Enter 4]
    => ''')
    elif choice_lst == 11:
        print("End of program.")
        exit()

def doctor_choices(): 
    option = int(input("""
    Enter Your Choice:
    =>(1)Do you want to Register doctors details[Enter 1]
    =>(2)Do you want to Register patient details[Enter 2]
    =>(3)Do you want to View All the doctors details[Enter 3]
    =>(4)Do you want to View individual doctors details[Enter 4]
    =>(4)Do you want to View All the Patient details[Enter 5]
    =>(6)Do you want to View individual Patient details[Enter 6]  
    =>(7)Exit[Enter 5]
    => """))
    if option == 1:
        Doctor_Name = input('Enter Doctor Name:')
        Doctor_Age = int(input('Enter Age:'))
        Doctor_Department = input('Enter the Department:')
        Phone_no = int(input('Enter Phone number:'))
        sql_doctor = 'INSERT into Doctor_Details (Doctor_Name,Doctor_Age,Doctor_Department,Phone_no) VALUES (%s, %s, %s, %s)'
        d_details = (Doctor_Name, Doctor_Age, Doctor_Department, Phone_no)
        c1.execute(sql_doctor, d_details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif option == 2:
        Patient_Name = input('Enter Patient Name:')
        Patient_Age = int(input('Enter Age:'))
        Patient_Disease_Illness = input('Enter The Problem/Disease:')
        Phone_no = int(input('Enter Phone Number:'))
        sql_patient = 'INSERT into Patient_Details VALUES (%s, %s, %s, %s)'
        P_Details = (Patient_Name, Patient_Disease_Illness, Phone_no)
        c1.execute(sql_patient, P_Details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif option == 3:
        sql_doctor = 'SELECT * FROM Doctor_Details '
        c1.execute(sql_doctor)
        dfile = c1.fetchall()
        for d in dfile:
            print(d)
    elif option == 4:
        sql_specific_doctor = input("Enter Doctor Name: ")
        doc = 'SELECT * FROM Doctor_Details WHERE Doctor_Name=("{}")'.format(sql_specific_doctor)
        c1.execute(doc)
        dfile = c1.fetchall()
        for d in dfile:
            print(d)
    elif option == 5:
        sql_patient = 'SELECT * FROM Patient_Details '
        c1.execute(sql_patient)
        pfile = c1.fetchall()
        for p in pfile:
            print(p)
    elif option == 6:
        sql_specific_patient = input("Enter Patient Name:")
        patient = 'SELECT * FROM Patient_Details WHERE Patient_Name =("{}")'.format(sql_specific_patient)
        c1.execute(patient)
        pfile = c1.fetchall()
        for p in pfile:
            print(p)
    elif option == 7:
        print("End of program.")
        exit()

def staff_choices():
    option = int(input("""
    Enter Your Choice:
    =>(2)Do you want to Register Staff details[Enter 1]
    =>(1)Do you want to View All the Staff details[Enter 2]
    =>(2)Do you want to View individual Staff details[Enter 3]
    =>(3)Exit[Enter 4]
    =>  """))
    if choice_lst == 1:
        Staff_Name = input('Enter Staff Name:')
        Staff_Age = int(input('Enter Age:'))
        Work_Description = input('Enter Your Area Of Work:')
        Phone_no = int(input('Enter Phone number:'))
        sql_staff = 'INSERT into Doctor_Details (Doctor_Name,Doctor_Age,Doctor_Department,Phone_no) VALUES (%s, %s, %s, %s)'
        w_details = (Staff_Name, Staff_Age,Work_Description, Phone_no)
        c1.execute(sql_staff, w_details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif option == 2:
        sql_staff = 'SELECT * FROM Staff_Details '
        c1.execute(sql_staff)
        Staff = c1.fetchall()
        for s in Staff:
            print(s)
    elif option == 3:
        sql_specific_staff = input("Enter staff Name:")
        staff = 'SELECT * FROM Staff_Details WHERE staff_Name=("{}")'.format(sql_specific_staff)
        c1.execute(staff)
        wfile = c1.fetchall()
        for w in wfile:
            print(w)
    elif option == 4:
        print("End of program.")
        exit()

def patient_choices():
    option = int(input("""
    Enter Your Choice:
    =>(1)Do you want to Register Patient details[Enter 1]
    =>(2)Do you want to View All the doctors details[Enter 2]
    =>(3)Do you want to View individual doctors details[Enter 3]
    =>(4)Exit[Enter 4]
    =>  """))
    if choice_lst == 1:
        Patient_Name = input('Enter Patient Name:')
        Patient_Age = int(input('Enter Age:'))
        Patient_Disease_Illness = input('Enter The Problem/Disease:')
        Phone_no = int(input('Enter Phone Number:'))
        sql_patient = 'INSERT into Patient_Details VALUES (%s, %s, %s, %s)'
        P_Details = (Patient_Name, Patient_Age,Patient_Disease_Illness, Phone_no)
        c1.execute(sql_patient, P_Details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif option == 2:
        sql_doctor = 'SELECT * FROM Doctor_Details '
        c1.execute(sql_doctor)
        dfile = c1.fetchall()
        for d in dfile:
            print(d)
    elif option == 3:
        sql_specific_doctor = input("Enter Doctor Name: ")
        doc = 'SELECT * FROM Doctor_Details WHERE Doctor_Name=("{}")'.format(sql_specific_doctor)
        c1.execute(doc)
        dfile = c1.fetchall()
        for d in dfile:
            print(d)
    elif option == 4:
        print("End of program.")
        exit()

User_Post = input('''What Do you Work as In Aster Care? :
    =>(1)Chairman[Enter 1]
    =>(2)Doctor[Enter 2]
    =>(3)Staff[Enter 3]
    =>(4)Patient[Enter 4]
    => ''')
login_count = 0
while True:  
    login_count += 1
    if User_Post == '1':
        if login_count == 1:
            login()
            available_functions()
            chairmain_choices()
        elif login_count > 1:
            available_functions()
            chairmain_choices()
    elif User_Post == '2':
        if login_count == 1:
            login() 
            doctor_choices()
        elif login_count > 1:
            doctor_choices()
    elif User_Post == '3':
        if login_count == 1:
            login()
            staff_choices()
        elif login_count > 1:
            staff_choices()
    elif User_Post == '4':
        if login_count == 1:
            login()
            patient_choices()
        elif login_count > 1:
            patient_choices()
