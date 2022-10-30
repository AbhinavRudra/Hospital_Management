import mysql.connector as sql
from sys import exit
#from colorama import Fore, Style, init
#from termcolor import colored
conn = sql.connect(
    host='localhost',
    user='root',
    password='root',
    database='Hospital_Database',
    auth_plugin='mysql_native_password'
)
# Cheking if the Database is connected
if conn.is_connected():
    print('SUCCESSFULLY CONNECTED!!')
c1 = conn.cursor()

print('''
---------------------------------------------
      WELCOME TO <HOSP.NAME> HOSPITAL
---------------------------------------------
''')
print('"MAY GOD BELESS YOU!!"')
usernames = passwords = names = []

#Mske a new signin and use the same UserID & Password to login 
#To use a new UserID & Password:- Exit and Create new singin
def sign_up(): 
    global usernames
    global passwords
    # Appending User's:- name, username & password to the list
    names.append(input("Enter Your Name: "))
    usernames.append(input("Choose Your Username: "))
    passwords.append(input("Choose Your Password: "))


def login():
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    # Checking if the username and password provided are corect or not
    if username in usernames and password in passwords:
        print('SUCCESSFULLY LOGGED IN')
        available_functions()
        choices()
    else:
        print("INCORRECT USERNAME OR PASSWORD!")


def available_functions():  # list of all functions
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print('(1)Registering Patient Details')
    print('(2)Registering Doctor Details')
    print('(3)Registering Worker Details')
    print('(4)Total Patient Details')
    print('(5)Total Doctor Details')
    print('(6)Total Worker Details')
    print('(7)Search For Individual Patient Detail')
    print('(8)Search For Individual Doctor Detail')
    print('(9)Search For Individual Worker Detail')
    print('(10)Exit')
    global choice_lst
    choice_lst = int(input('ENTER YOUR CHOICE:'))


def choices():
    if choice_lst == 1: 
        Patient_Name = input('Enter Patient Name:')
        Patient_Age = int(input('Enter Age:'))
        Patient_Disease_Illness = input('Enter The Problem/Disease:')
        Phone_no = int(input('Enter Phone Number:'))
        sql_insert = 'INSERT into Patient_details VALUES (%s, %s, %s, %s)'
        P_Details = (Patient_Name, Patient_Age,
                     Patient_Disease_Illness, Phone_no)
        c1.execute(sql_insert, P_Details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif choice_lst == 2: 
        Doctor_Name = input('Enter Doctor Name:')
        Doctor_Age = int(input('Enter Age:'))
        Doctor_Department = input('Enter the Department:')
        Phone_no = int(input('Enter Phone number:'))
        sql_insert = 'INSERT into Doctor_details (Doctor_Name,Doctor_Age,Doctor_Department,Phone_no) VALUES (%s, %s, %s, %s)'
        d_details = (Doctor_Name, Doctor_Age, Doctor_Department, Phone_no)
        c1.execute(sql_insert, d_details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif choice_lst == 3:  
        Worker_Name = input('Enter Worker Name:')
        Worker_Age = int(input('Enter Age:'))
        Work_Description = input('Enter Your Area Of Work:')
        Phone_no = int(input('Enter Phone number:'))
        sql_insert = 'INSERT into Doctor_details (Doctor_Name,Doctor_Age,Doctor_Department,Phone_no) VALUES (%s, %s, %s, %s)'
        w_details = (Worker_Name, Worker_Age,
                     Work_Description, Phone_no)
        c1.execute(sql_insert, w_details)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
    elif choice_lst == 4: 
        sql_patient = 'SELECT * FROM Patient_details '
        c1.execute(sql_patient)
        pfile = c1.fetchall()
        for i in pfile:
            print(i)
    elif choice_lst == 5: 
        sql_doctor = 'SELECT * FROM Doctor_details '
        c1.execute(sql_doctor)
        dfile = c1.fetchall()
        for i in dfile:
            print(i)

    elif choice_lst == 6: 
        sql_worker = 'SELECT * FROM Worker_details '
        c1.execute(sql_worker)
        Staff = c1.fetchall()
        for i in Staff:
            print(i)
    elif choice_lst == 7:  
        sql_specific_patient = input("Enter Patient Name:")
        patient = 'SELECT * FROM Patient_details WHERE Patient_Name =("{}")'.format(
            sql_specific_patient)
        c1.execute(patient)
        pfile = c1.fetchall()
        for p in pfile:
            print(p)
    elif choice_lst == 8: 
        sql_specific_doctor = input("Enter Doctor Name: ")
        doc = 'SELECT * FROM Doctor_details WHERE Doctor_Name=("{}")'.format(
            sql_specific_doctor)
        c1.execute(doc)
        dfile = c1.fetchall()
        for d in dfile:
            print(i)
    elif choice_lst == 9: 
        sql_specific_worker = input("Enter Worker Name:")
        worker = 'SELECT * FROM Worker_details WHERE Worker_Name=("{}")'.format(
            sql_specific_worker)
        c1.execute(worker)
        wfile = c1.fetchall()
        for w in wfile:
            print(i)
    elif choice_lst == 10:
        print("End of program.")
        exit()


entries_available_functions = 0  # No. of times available_functions are opened
while True: 
    choice = input("""CHOOSE:
    =>(1)Sign Up[Enter 1]
    =>(2)Login[Enter 2]
    =>(3)Display_list_of_available_functions?[Enter 3]
    =>(4)Quit[Enter 4]
    => """)
    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        entries_available_functions += 1
        if entries_available_functions == 1:
            login()  # Password is asked here(as the no of use of available_functions is=1)
            available_functions()
            choices()
        elif entries_available_functions != 1:
            available_functions()  # Password already entered
            choices()
    elif choice == "4":
        print("End of program.")
        exit()  # using from sys method
