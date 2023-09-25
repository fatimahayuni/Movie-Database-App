function fetchMovie() {
  // Validate the input. Grab the value of the input box and put it in the console.
  const searchBar = document.getElementById("keyword");
  const inputValue = searchBar.value;
  console.log(inputValue);

  // The Flask endpoint URL is "/api/movies?". The '?' means the beginning of the parameter.
  // Assign a variable called 'url' that creates the link in the browser when the search bar is input with values.

  const searchMovieURL =
    "/api/movies?" +
    new URLSearchParams({
      keyword: inputValue,
    });

  // This is a GET request to the Flask endpoint (2ND ENDPOINT) in app.py
  fetch(searchMovieURL)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // Handle the response data here
      const searchResult = document.getElementById("search-results");
      searchResult.innerHTML = "";
      data.forEach((movie) => {
        const newElement = document.createElement("p");
        newElement.setAttribute("data-id", movie[0]); //representing columns in the db, movie[0] is an id. This one is invisible to the browser but you can see it in the console because you've stuffed it in the attribute.
        newElement.innerText = movie[0] + ", " + movie[1] + ", " + movie[2]; // This is the movie title
        searchResult.appendChild(newElement);
      });
    })
    .catch((error) => {
      // Handle errors here
      console.error("Error:", error);
    });
}

function createMovie() {
  // Validate the input
  const createMovieValue = document.getElementById("movie-title").value;
  const createGenreValue = document.getElementById("genre").value;

  if (createMovieValue.trim() === "" || createGenreValue.trim() === "") {
    // Display an error message for empty input in either field
    alert("You must enter both a movie title and genre.");
    return;
  }

  // Define the URL for the POST request.
  const createMovieURL = "/api/movies/create"; // Endpoint for adding movies. #todo ask martin why don't we use this in the address

  // Create a JavaScript object with both movie title and genre to be sent as JSON later
  const movieData = {
    "movie-title": createMovieValue,
    genre: createGenreValue,
  };

  // This is Fetch API. Configure the fetch request for a POST method and JSON data

  const movieDataJSON = JSON.stringify(movieData);
  // This is the point where JS connect to Python by createMovieURL which is present in both JS and Python file.
  fetch(createMovieURL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: movieDataJSON,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); //todo ask martin. didn't this get converted to JSON already in app.py line 81.
    })
    .then((newMovieData) => {
      console.log(newMovieData, typeof newMovieData);
      // Handle the response data here
      const createResult = document.getElementById("create-result");
      createResult.innerHTML = "";

      if (typeof newMovieData === "object") {
        const entries = Object.entries(newMovieData);
        console.log(entries);

        for (const [key, value] of entries) {
          const newElement = document.createElement("p");

          // Include the ID in the innerText
          newElement.innerText = `You have inserted a movie called ${key} with the genre ${value} successfully!`;

          createResult.appendChild(newElement);
        }
      } else {
        console.error("Response data is not an object."); //todo ask martin what is an example of response data not being an object cos my code always converts the data into an object anyway?
      }
    })
    .catch((error) => {
      // Handle errors here
      console.error("Error:", error); //todo when will this ever be triggered?
    });
}

// Validate that inputValueInt is a positive integer
function isPositiveInteger(inputValueInt) {
  return Number.isInteger(inputValueInt) && inputValueInt > 0;
}

function deleteMovieById() {
  // Capture the input value from the delete form
  const deleteBar = document.getElementById("movie-id");
  const inputValueStr = deleteBar.value;
  const inputValueInt = parseInt(inputValueStr);

  // Validate that inputValueInt is a positive integer
  if (!isPositiveInteger(inputValueInt)) {
    alert("Invalid movie ID. Please enter a positive integer.");
    return;
  }

  // Define the URL for the DELETE request.
  const deleteMovieURL = `/api/movies/delete/${inputValueInt}`;

  // Configure the fetch request for a DELETE method
  fetch(deleteMovieURL, { method: "DELETE" })
    .then((response) => {
      // The first then block is like a report. Did the response come back okay?
      console.log(response);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // The second then block does: We have a proper data sent from the server. Do what you need to do with it here.
      // Check if the 'message' property exists in the response data
      console.log("Data with message:", data);
      console.log("Message:", data.result);
      const deleteResult = document.getElementById("delete-result");
      if (data.result == true) {
        deleteResult.innerHTML = "Movie deleted successfully.";
      } else {
        deleteResult.innerHTML = "Movie not deleted successfully.";
        console.log("Success: Movie deleted successfully");
      }
    })
    .catch((error) => {
      // Handle errors here
      console.error("Error", error);
    });
}

function updateMovieById() {
  // Capture input values from the update form
  const movieIdStr = document.getElementById("update-movie-id").value;
  const newTitleInput = document.getElementById("new-movie-name").value;
  const newGenreInput = document.getElementById("new-movie-genre").value;

  // Parse movieIdStr as an integer
  const movieIdInt = parseInt(movieIdStr);
  // Validate that movieIdInt is a positive integer
  if (!isPositiveInteger(movieIdInt)) {
    alert("Invalid movie ID. Please enter a positive integer. ");
    return;
  }

  // Define the URL for the POST request.
  const updateMovieURL = `/api/movies/update/${movieIdInt}`;

  // Create a Javascript object with the new title and genre to be sent as JSON.
  const movieData = {
    "new-title": newTitleInput,
    "new-genre": newGenreInput,
  };

  // Convert the data to JSON format.
  const movieDataJSON = JSON.stringify(movieData);

  // Configure the fetch request for a POST method and JSON data.
  fetch(updateMovieURL, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json", // todo what is this for? why doesn't delete have it?
    },
    body: movieDataJSON,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((result) => {
      // Handle the response data here. //todo what is result.result again? True or False. Check app.py line 136.
      if (result && result.result) {
        const updateResult = document.getElementById("update-result-message");
        updateResult.innerHTML =
          "The movie and genre was updated successfully.";
        console.log("Success: Movie updated successfully.");
      } else {
        console.log("Error: Movie update failed");
      }
    })
    .catch((error) => {
      // Handle errors here
      console.log("Error", error);
    });
}
