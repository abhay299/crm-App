import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Abhay@78',
)

cursorObject = database.cursor()

# Create a Database
cursorObject.execute("CREATE DATABASE credentials")

print("It's Done!")
