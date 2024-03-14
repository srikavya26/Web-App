## Web App Documentation

### Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction
This is an basic web application that allows users to input data, validate it, store it in a
database, retrieve it, and display it in a table format.
This web application is built using Python with Flask framework.
SQLite is used as the database management system.
It utilizes HTML and CSS for structure and styling respectively. 

## Prerequisites

Before you begin, ensure you have met the following requirements:

### Python

- Python is a prerequisite for running Flask applications.
- You can download Python from the [official Python website](https://www.python.org/downloads/).
- Make sure to install Python according to your operating system.
- Verify the installation by opening a terminal or command prompt and typing:
    ```bash
    python --version
    ```
    You should see the installed Python version.

### Flask

- Flask is a lightweight WSGI web application framework for Python.
- You can install Flask using pip, Python's package installer.
- To install Flask, run the following command in your terminal or command prompt:
    ```bash
    pip install Flask
    ```

### SQLite

- SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- Flask supports SQLite out of the box for small to medium-sized applications.
- You can interact with SQLite databases using the built-in `sqlite3` module in Python.
  ```bash
   npm install sqlite3
    ```

## Technologies Used
- Python
- SQLite
- Flask
- HTML
- CSS

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/srikavya26/Web-App.git
    ```

2. Navigate into the project directory:
    ```bash
    cd Web-App
    ```

3. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
## File and Folder structure 
| File/Folder          | Description                                     |
|----------------------|-------------------------------------------------|
| `app`               | Main application directory.                     |
| `app.py`          | Main file for the application. |
| `data_users.db`        | SQLite database file for the application.       |
| `static/`            | Directory for static files.                     |
| `static/css/`        | Directory for CSS stylesheets.                  |
| `static/css/style.css` | CSS stylesheet for the application.          |
| `templates/`         | Directory for HTML templates.                   |
| `templates/index.html` | HTML file for the main page of the application. |

## Usage
1. Ensure you have Python installed on your system.
2. Navigate to the project directory in your terminal.
3. Run the Flask application:
    ```bash
    python app.py
    ```
    or
   
    ```bash
    flask run
    ```
5. Open your web browser and navigate to `http://localhost:5000` to view the application.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the contribution guidelines.

## License
This project is licensed under the [MIT License](LICENSE).
