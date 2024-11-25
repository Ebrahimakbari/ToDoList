# ToDoList Project

## Overview

This is a simple ToDo List application built using Django, a high-level Python web framework. The project consists of a base application with models, views, templates, and static files, as well as settings and URLs configurations.

## Directory Structure

The project is organized into several directories:

- `base`: Contains the main application files.
- `ToDoList`: Contains the project-level settings, URLs, and WSGI/ASGI configurations.
- `static`: Contains static files like CSS stylesheets.
- `templates`: Contains HTML templates used by the application.
- `utils`: Contains utility modules.

## Configuration

The project uses environment variables for configuration. You can set these variables in a `.env` file or directly in your environment.

- `SECRET_KEY`: This is a secret key used by Django for security purposes. You should set this to a unique value in your `.env` file.
- `DEBUG`: This is a boolean value that determines whether the application is in debug mode. Set this to `True` for development and `False` for production.

## Running the Application

To run the application, you need to install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

Then, you can start the application by running:

```bash
python manage.py runserver
```

This will start the development server on `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please feel free to submit a pull request or open an issue.