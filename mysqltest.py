import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="password",
  database="CEN434"

)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students_table (firstname VARCHAR(255), matric_no VARCHAR(255), lastname VARCHAR(255))")
mycursor.execute("""INSERT into students  (firstname, matric_no,lastname) VALUES ("abundance", "20cj027424","anyanwu");""")

                 

print(mydb) 
