# Blog API with Django REST Framework

This project is a full-featured Blog API built with Python, Django, and Django REST Framework. It provides a complete set of CRUD (Create, Read, Update, Delete) endpoints for managing blog posts, complete with user authentication and permissions.

This API serves as a robust backend, ready to be consumed by any front-end client (like React, Vue, or a mobile application).

## Features

-   **Full CRUD Functionality:** Create, retrieve, update, and delete blog posts via the API.
-   **Authentication & Permissions:** Utilizes Django REST Framework's `IsAuthenticatedOrReadOnly` permission class.
    -   `GET` requests (reading posts) are open to the public.
    -   `POST`, `PUT`, `PATCH`, and `DELETE` requests require user authentication.
-   **User-Post Relationship:** Each post is directly associated with an author (a Django `User` model), ensuring clear ownership of content.
-   **Browsable API:** Includes the user-friendly browsable API provided by DRF for easy interaction and testing directly in your browser.
-   **Admin Integration:** The `Post` model is fully integrated with the Django admin panel for easy content management.
-   **Unit Tests:** Comes with a basic test suite to ensure the reliability of the `Post` model.

## Technologies Used

-   **Backend:** Python, Django
-   **API Framework:** Django REST Framework
-   **Database:** SQLite (default)

## API Endpoints

The API is versioned and available under the base URL: `/api/v1/`.

| Endpoint             | HTTP Method | Description                                  | Authentication Required |
| -------------------- | ----------- | -------------------------------------------- | ----------------------- |
| `/api/v1/`           | `GET`       | Retrieves a list of all blog posts.          | No                      |
| `/api/v1/`           | `POST`      | Creates a new blog post.                     | Yes                     |
| `/api/v1/<int:pk>/`  | `GET`       | Retrieves a single blog post by its ID.      | No                      |
| `/api/v1/<int:pk>/`  | `PUT`       | Updates a blog post.                         | Yes                     |
| `/api/v1/<int:pk>/`  | `PATCH`     | Partially updates a blog post.               | Yes                     |
| `/api/v1/<int:pk>/`  | `DELETE`    | Deletes a blog post.                         | Yes                     |

## Setup and Installation

Follow these instructions to get the backend server running on your local machine.

### Prerequisites

-   Python 3.8 or higher
-   pip (Python package installer)
-   Git

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/drf-blog-api.git
cd drf-blog-api
```

### 2. Set Up the Environment

Navigate into the directory where the project code is located (in this case, it seems to be a `backend` folder, but adjust if needed).

```bash
# If your project is inside a 'backend' folder
cd backend
```

Create and activate a Python virtual environment:

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python packages.

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Create the database schema based on the models.

```bash
python manage.py migrate
```

### 5. Create a Superuser

This is required to access the Django admin panel and to create posts via the API.

```bash
python manage.py createsuperuser
```
Follow the prompts to create a username and password.

## Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

The API server will now be running at `http://127.0.0.1:8000/`.

## How to Use the API

1.  **Read Posts (No Auth Needed):**
    -   Navigate to `http://127.0.0.1:8000/api/v1/` in your browser to see the list of all posts.
    -   Navigate to `http://127.0.0.1:8000/api/v1/1/` to see the detail view for the post with ID 1.

2.  **Create/Update/Delete Posts (Auth Required):**
    -   Go to `http://127.0.0.1:8000/api/v1/` and log in to the browsable API using the superuser credentials you created.
    -   Once logged in, you will see a form at the bottom of the page that allows you to `POST` (create) a new blog post.
    -   In the detail view (e.g., `/api/v1/1/`), you will see options to `PUT`, `PATCH`, and `DELETE` the post.
```