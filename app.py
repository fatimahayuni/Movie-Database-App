# This is a private file where the logic of our program is contained.
# if we are in this file, we ARE the SERVER. How we are handling requests from the CLIENT.
# We don't want to open to others as they can get private information about our program, like how we are handling the data.
# Cos it is our Intellectual Property.
# and thus making our system vulnerable.

from flask import Flask, request, jsonify, render_template
from movie_app_module import *
import traceback


# Initialise flask
app = Flask(__name__)

# 1ST ENDPOINT
# Route to fetch search.html. When the user types the local host and then /search in the browser, it will bring us to search.html
# The method is GET because we are GETTING or requesting the data from the server.


@app.route('/search', methods=['GET'])
# This function renders the search.html to the web browser
def search_page():
    return render_template('read.html')

# 2ND ENDPOINT
# Route to perform the search query. This will contain MYSQL queries.


# '/api/pieceofdatathatyoureaccessinginthatapi' <--the convention.
@app.route('/api/movies', methods=['GET'])
def perform_sql_query():
    # This has nothing to do with user input
    # This is validating that the CLIENT has sent the SERVER the right stuff. We are making sure this matches with the input element in search.html where there is an id called 'keyword'
    # Valid url: "http://127.0.0.1:5000/search?keyword=shawshank" <--we are testing the 'keyword' part.
    # hacker URL: "/api/movies?eggplant=i_wonder_if_i_can_break_your_server_by_sending_stupid_arguements_to_the_endpoint"
    # the hacker URL, he used 'eggplant' instead of keyword. That's not valid. So this function will capture that.
    # The instances where the CLIENT/BROWSER is sending us the wrong stuff is when a hacker sends us back a something that breaks the code and worse, messes up our DB.
    # It is making sure that the browser has in fact sent us the correct key in the URL.
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify("Invalid form submission. Call your backend developer."), 400

    # results is the variable for the function call called search_movie(keyword). This is in search_movie_module.py.
    # This function searches for the movies in the db with the keyword given
    search_result = search_movie(keyword)

    if not search_result:
        # 404 is an HTTP code. Easier for devs to understand.
        return jsonify("Movies not found"), 404

    return jsonify(search_result)

# 3RD ENDPOINT: Route to render create.html


@app.route('/create', methods=['GET'])
def create_page():
    return render_template('create.html')

# 4TH ENDPOINT
# Route to receive the new movie details from the browser and insert a new movie record in the database table.
# We use create_movie_route function in the module here


@app.route('/api/movies/create', methods=['POST'])
def create_movie_route():
    try:
        # Get JSON data from the request
        data = request.get_json()
        # We are validating that the POST method has indeed sent us the 'movie-title'.
        movie_title = data.get('movie-title')
        genre = data.get('genre')

        if not movie_title or not genre:
            return jsonify({"error": "Please provide both movie title and genre"}), 400

        # create_movie_results is the variable for the function call called create_movie(keyword). This is in movie_app_module.py. Question.
        # What does create_movie_results() do? It puts movie in the the database
        create_movie_results = create_movie(movie_title, genre)

        return jsonify(create_movie_results)

    except Exception as e:
        print(traceback.print_exc())
        return jsonify({"error": str(e)}), 400

# 5TH ENDPOINT
# Route to render delete.html


@app.route('/delete', methods=['GET'])
def delete_page():
    return render_template('delete.html')

# 6TH ENDPOINT
# Route to receive the new POST request on URL "api/movies/delete"


@app.route('/api/movies/delete/<int:movie_id>', methods=['DELETE'])
def delete_movie_route(movie_id):
    # Use movie_id from the URL path directly
    try:
        # Attempt to delete the movie by ID
        delete_result = delete_movie_by_id(movie_id)
        return jsonify({"result": delete_result})
    except Exception as e:
        # Handle any errors and return an appropriate response
        # return jsonify({"error": str(e)}), 400
        return jsonify({"result": False})

# 7TH ENDPOINT
# Route to render delete.html


@app.route('/update', methods=['GET'])
def update_page():
    return render_template('update.html')

# 8TH ENDPOINT
# Route to receive the new POST request on URL "api/movies/delete"


@app.route('/api/movies/update/<int:movie_id>', methods=['PUT'])
def update_movie_route(movie_id):
    # Use movie_id from the URL path directly
    try:
        # Get new title and genre from the request JSON data
        data = request.get_json()
        new_title = data.get("new-title")
        new_genre = data.get("new-genre")

        # Attempt to update the movie by ID
        update_result = update_movie_by_id(movie_id, new_title, new_genre)

        if update_result:
            return jsonify({"result": True, "message": "Movie updated successfully"})
        else:
            return jsonify({"result": False, "message": "Movie update failed"}), 400

    except Exception as e:
        return jsonify({"result": False, "error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
