import mysql.connector as sql
conn = sql.connect(
    host='localhost',
    user='root',
    password='root',
    database='Hospital_Database',
    auth_plugin='mysql_native_password'
)
c1 = conn.cursor()

c1.execute('''CREATE TABLE Patient_Details(
    Patient_Name varchar(20) Primary Key, 
    Patient_Age int(10), 
    Patient_Disease_Illness varchar(100), 
    Phone_no int(10))
    ''')

c1.execute('''CREATE TABLE Doctor_Details(
    Doctor_Name varchar(20) Primary Key,
    Doctor_Age int,
    Doctor_Department varchar(100),
    Phone_no int(10))
    ''')

c1.execute('''CREATE TABLE Worker_Details(
    Worker_Name varchar(20) Primary Key,
    Worker_Age int,
    Work_Description varchar(100),
    Phone_no int(10))
    ''')
