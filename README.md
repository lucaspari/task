# TASK 

## About the Project

This project consists of a client-side application, a Flask backend, and a MongoDB database. The client-side application is available on port 3000, the Flask backend on port 8000, and the MongoDB database on port 27017.

## Prerequisites

- Docker
- Docker Compose

## Running the Project

To run the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Start the services using Docker Compose:
    ```sh
    docker-compose up
    ```

3. Access the client application at `http://localhost:3000`.

4. The Flask backend will be running at `http://localhost:8000`.

5. MongoDB will be available at `mongodb://localhost:27017`.

## Stopping the Project

To stop the project, run:
```sh
docker-compose down
```
