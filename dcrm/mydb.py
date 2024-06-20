import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@255Rukia',

)

#prepare a cursor object 
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crmproject")

print("All Done!")


