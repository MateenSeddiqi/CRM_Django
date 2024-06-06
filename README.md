# Customer Relationship Management Website

This is a CRM (Customer Relationship Management) website developed using HTML, CSS, Bootstrap, and Django. This project is intended as a learning resource for those who want to explore Django and the fundamentals of web development.

## Features

1. **User Authentication**:
   - Users can create an account and log in to the website.
   - Users can update their profile information.

2. **Records Management**:
   - Authenticated users can view a list of all records.
   - Users can add new records.
   - Users can view details of a specific record.
   - Users can update and delete their own records.

3. **Responsive Design**:
   - The website is designed to be mobile-friendly and responsive using Bootstrap.

## Learning Objectives

This project is designed to be a learning resource for those who want to explore Django and the fundamentals of web development. By working on this project, you can learn the following:

1. **Django Framework**:
   - Understanding the Model-View-Template (MVT) architecture of Django.
   - Implementing user authentication and authorization.
   - Working with Django forms and models.
   - Handling database operations (create, read, update, delete).

2. **Web Development Fundamentals**:
   - HTML, CSS, and Bootstrap for building responsive and visually appealing user interfaces.
   - Integrating frontend and backend components.
   - Implementing CRUD (Create, Read, Update, Delete) functionality.
   - Deploying the application to a production environment.

3. **Coding Best Practices**:
   - Writing clean, maintainable, and well-documented code.
   - Applying software engineering principles, such as modularization and separation of concerns.
   - Incorporating version control and collaboration workflows using Git.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/MateenSeddiqi/CRM_Django.git
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required dependencies:

   - Django
   - psycopg2 (if using PostgreSQL)
   - mysql-connector-python (if using MySQL)

   You can install these dependencies using pip:

   ```
   pip install django django-crispy-forms psycopg2
   ```

   or, if you're using MySQL:

   ```
   pip install django django-crispy-forms mysql-connector-python
   ```

4. Apply the database migrations:

   ```
   python manage.py migrate
   ```

5. Start the development server:

   ```
   python manage.py runserver
   ```

   The website should now be accessible at `http://127.0.0.1:8000/`.

## Usage

1. **Registration and Login**:
   - Visit the website and click on the "Signup" link to create a new account.
   - After registration, you can log in to the website using your credentials.

2. **Records Management**:
   - Once logged in, you can view the list of all records on the dashboard.
   - Click on the "Add Record" button to create a new record.
   - Click on a specific record to view its details, and use the "Edit" or "Delete" buttons to update or delete the record.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request, describing the changes you've made.

Your contributions are greatly appreciated!
