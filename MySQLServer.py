import mysql.connector

def create_database(db_name, host="localhost", user="your_username", password="your_password"):
  """
  Creates the specified database in the MySQL server.

  Args:
      db_name (str): The name of the database to create.
      host (str, optional): The hostname of the MySQL server. Defaults to "localhost".
      user (str, optional): The username for connecting to the MySQL server. Defaults to "your_username".
      password (str, optional): The password for connecting to the MySQL server. Defaults to "your_password".
  """
  try:
    # Create a connection to the MySQL server (without specifying a database)
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()

    # Create the database using CREATE DATABASE IF NOT EXISTS
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {alx_book_store}")

    cnx.commit()
    print(f"Database '{alx_book_store}' created successfully!")
  except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
  finally:
    if cnx:
      cnx.close()

if __name__ == "__main__":
  create_database("alx_book_store")

import mysql.connector

def create_database(db_name, host="localhost", user="your_username", password="your_password"):
  """
  Creates the specified database in the MySQL server.

  Args:
      db_name (str): The name of the database to create.
      host (str, optional): The hostname of the MySQL server. Defaults to "localhost".
      user (str, optional): The username for connecting to the MySQL server. Defaults to "your_username".
      password (str, optional): The password for connecting to the MySQL server. Defaults to "your_password".
  """
  try:
    # Create a connection to the MySQL server (without specifying a database)
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()

    # Attempt database creation (handling potential existence)
    sql = f"CREATE DATABASE IF NOT EXISTS {db_name}"
    cursor.execute(sql)
    cnx.commit()

    # Print success message if creation succeeded
    if cursor.rowcount > 0:  # Check if any rows were affected (i.e., database created)
      print(f"Database '{db_name}' created successfully!")
    else:
      print(f"Database '{db_name}' likely already exists. Skipping creation.")

  except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
  finally:
    if cnx:
      cnx.close()

if __name__ == "__main__":
  create_database("alx_book_store")


