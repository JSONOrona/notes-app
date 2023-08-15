# Notes App

The Notes App is a simple demo web application used for educational purposes only. It allows users to store and retrieve notes. This application is built using the Flask web framework for the backend and SQLite for database storage. Users can add notes via a web interface and view the list of stored notes. Additionally, the app exposes RESTful API endpoints to manage notes.

## Features

- Store and retrieve notes via a web interface.
- Expose RESTful API endpoints to interact with notes data.
- Simple and clean user interface.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/notes-app.git
    cd notes-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000` to access the Notes App.

3. Use the provided web interface to add and view notes. You can also make API calls to manage notes data.

## API Endpoints

- `GET /api/notes`: Retrieve a list of all notes.
- `POST /api/notes`: Add a new note.

## Technologies Used

- Flask: Web framework for the backend.
- SQLite: Lightweight database for notes storage.
- HTML, CSS, JavaScript: Frontend components.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
