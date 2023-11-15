import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="CEN434"
)
mycursor = mydb.cursor()

# Create (C) - Create Table
mycursor.execute("CREATE TABLE IF NOT EXISTS students_table (firstname VARCHAR(255), matric_no VARCHAR(255), lastname VARCHAR(255))")

# Create (C) - Insert Data
sql_insert = "INSERT INTO students_table (firstname, matric_no, lastname) VALUES (%s, %s, %s)"
student_data = ("Abundance", "20cj027424", "Anyanwu")
mycursor.execute(sql_insert, student_data)
mydb.commit()

# Read (R) - Retrieve Data
mycursor.execute("SELECT * FROM students_table")
result = mycursor.fetchall()
print("Retrieved Data:")
for row in result:
    print(row)

# Update (U) - Update Data
sql_update = "UPDATE students_table SET firstname = %s WHERE matric_no = %s"
new_firstname = "Updated Abundance"
matric_no = "20cj027424"
mycursor.execute(sql_update, (new_firstname, matric_no))
mydb.commit()

# Read (R) - Retrieve Updated Data
mycursor.execute("SELECT * FROM students_table")
updated_result = mycursor.fetchall()
print("\nUpdated Data:")
for row in updated_result:
    print(row)

# Delete (D) - Delete Data
sql_delete = "DELETE FROM students_table WHERE matric_no = %s"
matric_to_delete = "20cj027424"
mycursor.execute(sql_delete, (matric_to_delete,))
mydb.commit()

# Read (R) - Retrieve Data after deletion
mycursor.execute("SELECT * FROM students_table")
remaining_result = mycursor.fetchall()
print("\nRemaining Data after Deletion:")
for row in remaining_result:
    print(row)

mycursor.close()
