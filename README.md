# Django Application

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Testing](#testing)
- [License](#license)

---

## Overview

This Django application is designed for django backend assignment for user authentication and profile management. The
app follows Django best practices for modularity and scalability.

---

## Features

- **User authentication and authorization**
- **User Dashboard and Profile**

---

## Technologies Used

- **Python**
- **Django**
- **SQLite**

---

## Setup and Installation

### Prerequisites

Ensure the following are installed:

- Python 3.9+
- Virtualenv
- A database server (e.g.,SQLite)

### Installation Steps

1. Clone the repository:
   ```bash
   git https://github.com/nenzi/whatbytes.git
   cd whatbytes
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Create a `.env` file in the project root with the following (replace placeholders):
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

---

## Running the Application

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Open the application in your browser at `http://127.0.0.1:8000`.

---

## Environment Variables

| Variable       | Description                | Example                             |
|----------------|----------------------------|-------------------------------------|
| `SECRET_KEY`   | Django secret key          | `your_secret_key`                   |
| `DEBUG`        | Enable debug mode          | `True` or `False`                   |
| `DATABASE_URL` | Database connection string | `postgres://user:pass@localhost/db` |

---

## Testing

Run tests with:

```bash
python manage.py test
```

---

## License

This project is licensed under the **[MIT License]**. See the `LICENSE` file for details.

---
