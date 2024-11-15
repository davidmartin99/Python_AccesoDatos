import mysql.connector as bd

# Attempting to connect to the MySQL database 'hospital'
try:
    bd_conexion = bd.connect(
        host='localhost',  # Replace with '127.0.0.1' if localhost doesn't work
        port='3306',       # Default MySQL port
        user='root',       # Your MySQL username (default is 'root')
        password='1234',       # Your MySQL password (empty by default)
        database='hospital'  # The database you're trying to connect to
    )

    # Check if the connection was successful
    if bd_conexion.is_connected():
        print("Connection to the 'hospital' database was successful!")

        # Create a cursor object to interact with the database
        cursor = bd_conexion.cursor()

        # Executing the SQL query to retrieve the data
        cursor.execute("SELECT apellido, oficio, salario FROM emp")

        # Printing the results of the query
        for ape, ofi, sal in cursor:
            print("Apellido: " + ape)
            print("Oficio: " + ofi)
            print("Salario: " + str(sal))
            print("---------------")

except bd.Error as error:  # Error handling for MySQL connection or execution issues
    if error.errno == 1049:
        print("Error: Database 'hospital' not found. Please make sure the database exists.")
    else:
        print("Error: ", error)

finally:
    # Ensuring that the connection is properly closed
    if 'bd_conexion' in locals() and bd_conexion.is_connected():
        cursor.close()
        bd_conexion.close()
        print("Connection closed.")
