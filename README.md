<br/>
<p align="center">

  <h3 align="center">Movie Database App</h3>

  <p align="center">
    Welcome to the Movie Database App, a web application for managing and exploring your favorite movies! This project allows users to view, add, update, and delete movie entries in a user-friendly interface.
    <br/>
    <br/>
    <a href="https://github.com/ayuninotayutu/Movie-Database-App"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/ayuninotayutu/Movie-Database-App">View Demo</a>
    .
    <a href="https://github.com/ayuninotayutu/Movie-Database-App/issues">Report Bug</a>
    .
    <a href="https://github.com/ayuninotayutu/Movie-Database-App/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/ayuninotayutu/Movie-Database-App/total) ![Forks](https://img.shields.io/github/forks/ayuninotayutu/Movie-Database-App?style=social) ![License](https://img.shields.io/github/license/ayuninotayutu/Movie-Database-App) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project



This project is my second CRUD app but my first CRUD app that involves a database. 

The purpose of this project is to learn how to connect backend to frontend with a database involved. 

This project serves as my template for my future CRUD apps. 

## Built With

This project was built with:

* [Python]()
* [Flask]()
* [MySQL]()
* [Javascript]()
* [HTML]()
* [CSS]()

## Getting Started

Before you start, make sure you have the following installed:

### Prerequisites

* [Python]()
* [Flask]()
* [MySQL]()

### Installation

1. Clone the repository to your local machine:
`
git clone https://github.com/ayuninotayutu/Movie-Database-App.git
`


2. Navigate to the project directory:
`
cd Movie-Database-App
`


3. Create a virtual environment (optional but recommended):
`
python -m venv venv
`


4. Activate the virtual environment:
- Windows
`
venv\Scripts\activate
`

- Linux/macOS
`
source venv/bin/activate
`


5. Install project dependencies:
`
pip install -r requirements.txt
`

6. Set up your MySQL database by creating a .env file in the project directory with the following environment variables:
`
MYSQL_HOST=localhost
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DB=movie_database
`

7. Run the Flask application:
`
flask run
`

8. Open your web browser and navigate to `http://localhost:5000` to access the Movie Database App.

## Usage

<b>Creating a Movie</b><br>
To create a new movie to the database:
- Fill in the movie details, including the title and genre.
- Click the "Create" button to save the movie.<br>

<b>Reading a Movie</b><br>
To check if a movie exists in a database:
- Search for the movie that you are looking for.
- Click the "Search" button.<br>

<b>Updating a Movie</b><br>
To update an existing movie:
- Go to localhost/search. Take note of the ID.
- Go to localhost/update. Enter the movie ID you want to update.
- Modify the movie title and genre.
- Click the "Update" button to apply the changes.<br>


<b>Deleting a Movie</b><br>
To delete a movie:
- Go to localhost/search. Take note of the ID.
- Enter the ID in the form. 
- Click "Delete" button.<br>

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/ayuninotayutu/Movie-Database-App/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/ayuninotayutu/Movie-Database-App/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Ayuni Z** - *Software Developer* - [Ayuni Z](https://github.com/ayuninotayutu) - **

## Acknowledgements

* [Martin Blore](https://github.com/mblore)
