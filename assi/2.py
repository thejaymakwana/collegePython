import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='bvcnotcmxfqufnqrub9q-mysql.services.clever-cloud.com',
        port= 3306,
        user='umxo0tmrqjv0mxpl',
        password='fVFfMeU89Q7MddE2IR0c',
        database='bvcnotcmxfqufnqrub9q')
    cursor = mydb.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("You are connected to Jay MySQL server, version: ", db_version)
    mydb.close()
except (Exception, mysql.connector.Error) as error:
    print("Error while getting data", error)