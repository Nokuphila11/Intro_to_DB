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

    # Create the database (ignoring any errors if it already exists)
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    cnx.commit()
    print(f"Database '{db_name}' created successfully!")
  except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
  finally:
    if cnx:
      cnx.close()

if __name__ == "__main__":
  create_database("alx_book_store")
