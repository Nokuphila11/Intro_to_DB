    # Create the database using CREATE DATABASE IF NOT EXISTS
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

