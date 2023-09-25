from app import *
import pymysql

# Establish connection with MySQL
# We put this function in a different file because app.py should only contain Flask routes.


def create_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="MovieAppDB"
    )
# This function is to search for the movies in the db. That's why it contains SQL commands.


def search_movie(keyword):
    # This variable is assigned the function of create_db_connection.
    db = create_db_connection()
    # e Shawsh Then this variable now is an object variable db.cursor. This is assigned with the variable cursor.
    cursor = db.cursor()
    '''
    WHERE Name LIKE %s: This is the conditional clause of the query. It filters the rows from the "Movies_Table" based on a condition involving the "Name" column. The LIKE keyword is used to perform a partial string match. The %s is a placeholder that will be replaced with a specific value when the query is executed. Eg: 'Shawshank' is a partial string match to "Thank Redemption"

    %s in a LIKE clause is typically used with wildcard characters. In SQL, % represents a wildcard that matches any sequence of characters, and s indicates that the value to match will be provided as a string parameter.

    Martin said %s is a string parameter. That's it. 

    Another type of SQL query. Think about recipes website and you want to look for recipes that DO NOT contain milk. So the sql query would be like this: "SELECT * FROM Movies_Table WHERE Name NOT LIKE %s"
    '''
    search_query = "SELECT MovieID, Name, Genre FROM Movies_Table WHERE Name LIKE %s"

    """
    cursor.execute(query, (f"%{keyword}%",)): In this line, you execute the SQL query using a database cursor (represented by the cursor object). The execute method takes two arguments:

    The first argument is the SQL query to execute, which is stored in the query variable.

    The second argument is a tuple or list containing the values to replace the placeholders in the query. In this case, (f"%{keyword}%",) is a tuple containing a single value, which is a string created using an f-string. The f-string substitutes the %s placeholder with the value of keyword, surrounded by % wildcards. This allows you to perform a partial string match based on the value of keyword.
    """
    cursor.execute(search_query, (f"%{keyword}%",)
                   )  # we use tuple here not bcos we chose to but cos mysql said so.

    # retrieve all the rows returned by a previously executed SQL query and store them in the result variable.
    result = cursor.fetchall()
    print(result)
    cursor.close()
    db.close()
    return result


def create_movie(movie_title, genre):
    try:  # What's gonna run if no problem occurs
        db = create_db_connection()
        cursor = db.cursor()
        create_query = "INSERT INTO Movies_Table (Name, Genre) VALUES (%s, %s)"

        # Execute the query with the provided movie title.
        cursor.execute(create_query, (movie_title, genre))
        # Commit the changes to the database
        db.commit()
        # To check if the entry is inserted successfully.
        affected_rows = cursor.rowcount
        # Close the cursor and the database connection
        cursor.close()
        db.close()

        if affected_rows == 1:
            return {movie_title: genre}
        else:
            return {"message": "Oh no....movie creation failed..."}

    except Exception as e:
        # Handle any exceptions that may occur (eg: database errors. eg: not connecting)
        print(str(e))
        return {"error": "An error occured while adding the movie."}


# Delete movie by id
def delete_movie_by_id(movie_id):
    try:  # What's gonna run if no problem occurs
        db = create_db_connection()
        cursor = db.cursor()

        # SQL query to delete a movie by title
        delete_query = "DELETE FROM Movies_Table WHERE MovieID = %s"

        # Execute the query with the provided movie title.
        cursor.execute(delete_query, (movie_id,))

        # Commit the changes to the database
        db.commit()

        # To check if any rows were affected (movie deleted)
        affected_rows = cursor.rowcount

        # Close the cursor and the database connection
        cursor.close()
        db.close()

        if affected_rows == 1:
            return True
        else:
            return False

    except Exception as e:
        # Handle any exceptions that may occur (eg: database)
        print(str(e))
        return False

# Update movie


def update_movie_by_id(movie_id, new_title, new_genre):
    try:
        db = create_db_connection()
        cursor = db.cursor()

        # SQL query to update a movie by MovieId
        update_query = "UPDATE Movies_Table SET Name = %s, Genre = %s WHERE MovieID = %s"

        # Execute the query with the provided parameters
        cursor.execute(update_query, (new_title, new_genre, movie_id))

        # Commit the changes to the database
        db.commit()

        # To check if any rows were affected (movie updated)
        affected_rows = cursor.rowcount

        cursor.close()
        db.close()

        if affected_rows == 1:
            return True
        else:
            return False

    except Exception as e:
        print("Error", str(e))
        return False
