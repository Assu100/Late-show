# Late Night Show API

## Setup

1. Clone the repository.
2. Create a `.env` file with your database credentials.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run migrations:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
5. Seed the database:
    ```bash
    python seed.py
6. Run the app
    ```bash
    python app.py

# API Endpoints
### GET /episodes: Retrieve all episodes.
### GET /episodes/<id>: Retrieve a specific episode by ID
### GET /guests: Retrieve all guests.
### POST /appearances: Create a new appearance.

# Validation

## Final Steps

1. **Adjust Database Connection**: Ensure your `.env` file has the correct database connection string.
2. **Run the Application**: Start the Flask application using:
   ```bash
   python app.py

# Test with postman
