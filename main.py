#import relevant library
import mysql.connector

# Login details for MySQL Workbench
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Zainab2012?',
    'database': 'stores'
}

#This function will carry out the backup
def CarryOut_backup():
    connection = None  # configure connection variable
    db_cursor = None  # configure  cursor variable

    try:
        # Connection to MySQL server
        connection = mysql.connector.connect(**mysql_config)

        # Create a cursor object
        db_cursor = connection.cursor()

        #This is an sql command which selects all data from the business table.
        command = "SELECT * FROM Business"

        # Execute the command
        db_cursor.execute(command)

        # Fetch all rows
        rows = db_cursor.fetchall()

        # input data to the text file
        with open('backup.txt', 'w') as file:
            for row in rows:
                file.write(str(row) + '\n')

        print("Backup has been successfully created!")

    except mysql.connector.Error as error:
        print("Error. Back up has failed:", error)

    finally:
        # End cursor and connection
        if db_cursor:
            db_cursor.close()
        if connection:
            connection.close()

# carry out  backup
CarryOut_backup()

