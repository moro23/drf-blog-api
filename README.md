# DRF Blog API

A simple but robust RESTful API for a blog platform, built with Django and Django REST Framework. This project demonstrates core API principles including token-based authentication (JWT), custom permissions, and full CRUD (Create, Read, Update, Delete) functionality for blog posts.

## Features

*   **Full CRUD Operations:** Create, retrieve, update, and delete blog posts.
*   **Token-Based Authentication:** Secured endpoints using JSON Web Tokens (JWT) for stateless authentication.
*   **Custom Permissions:** Object-level permissions ensure that only the author of a post can edit or delete it.
*   **User Ownership:** Posts are automatically associated with the authenticated user who creates them.
*   **Clean and Organized Codebase:** Follows Django best practices for a scalable and maintainable project structure.

## Technologies Used

*   **Backend:** Python
*   **Framework:** Django
*   **API Toolkit:** Django REST Framework
*   **Authentication:** DRF Simple JWT

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

*   Python 3.8+
*   Pip (Python package installer)
*   Git

## Setup and Installation

Follow these steps to get a local copy of the project up and running.

1.  **Clone the Repository:**
    ```sh
    git clone https://github.com/your-username/drf-blog-api.git
    cd drf-blog-api
    ```

2.  **Create and Activate a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    All required packages are listed in the `requirements.txt` file.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations:**
    This will create the necessary database tables.
    ```sh
    python manage.py migrate
    ```

5.  **Create a Superuser:**
    This will allow you to access the Django admin panel.
    ```sh
    python manage.py createsuperuser
    ```
    You will be prompted to enter a username, email, and password.

6.  **Run the Development Server:**
    ```sh
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

The following are the main endpoints available in the API.

| Method | Endpoint | Description | Authentication Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/token/` | Obtain a new JWT access and refresh token. | No |
| `POST` | `/api/token/refresh/` | Obtain a new access token using a refresh token. | No |
| `GET` | `/api/v1/` | Retrieve a list of all blog posts. | No |
| `POST` | `/api/v1/` | Create a new blog post. | Yes (Bearer Token) |
| `GET` | `/api/v1/<id>/` | Retrieve a single blog post by its ID. | No |
| `PUT` | `/api/v1/<id>/` | Update a blog post. | Yes (Author only) |
| `DELETE` | `/api/v1/<id>/` | Delete a blog post. | Yes (Author only) |

## Usage Guide

To interact with the protected endpoints, you must first obtain an access token and then include it in the `Authorization` header for subsequent requests.

#### Step 1: Obtain an Access Token

Send a `POST` request to the `/api/token/` endpoint with your username and password in the request body.

**Request:**
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"username": "yourusername", "password": "yourpassword"}' \
http://127.0.0.1:8000/api/token/```

**Response:**
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl..."
}
```

#### Step 2: Make Authenticated Requests

Copy the `access` token from the response and use it as a Bearer token in the `Authorization` header for all requests to protected endpoints.

**Example: Create a New Post**

**Request:**
```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <PASTE_YOUR_ACCESS_TOKEN_HERE>" \
-d '{"title": "My First API Post", "body": "This is awesome!"}' \
http://127.0.0.1:8000/api/v1/
```

**Successful Response (201 Created):**
```json
{
    "id": 1,
    "author": "yourusername",
    "title": "My First API Post",
    "body": "This is awesome!",
    "created_at": "2025-11-12T10:30:00.123456Z"
}
```

---