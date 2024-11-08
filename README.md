# The Gist: Capturing thoughts, Sharing stories



"The Gist" is a web application implemented using Flask, designed as a blog sharing platform where users can create accounts, post, edit, and delete their posts.

## Technologies Used

- **Flask** (version 3.0.0): Flask is a lightweight WSGI web application framework in Python. It provides tools and libraries for building web applications.
- **Flask-Bcrypt** (version 1.0.1): Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your Flask application.
- **Flask-Login** (version 0.6.3): Flask-Login provides user session management for Flask applications.
- **Flask-Mail** (version 0.9.1): Flask-Mail is an extension to Flask that adds email sending capabilities to your application.
- **Flask-SQLAlchemy** (version 3.1.1): Flask-SQLAlchemy is a Flask extension that adds support for SQLAlchemy to your Flask application.
- **Flask-WTF** (version 1.2.1): Flask-WTF is a Flask extension that integrates Flask with WTForms, a flexible forms validation and rendering library.
- **bcrypt** (version 4.1.2): bcrypt is a password hashing function designed to be resistant to brute-force attacks.
- **blinker** (version 1.7.0): Blinker is a fast Python in-process signal/event dispatching library.
- **certifi** (version 2023.11.17): Certifi provides Mozilla’s carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates.
- **charset-normalizer** (version 3.3.2): Charset Normalizer is a library to handle charset in HTTP header and content.
- **click** (version 8.1.7): Click is a Python package for creating beautiful command-line interfaces.
- **idna** (version 3.6): IDNA provides support for the Internationalized Domain Names in Applications (IDNA) protocol.
- **itsdangerous** (version 2.0.1): ItsDangerous is a library for signing data with a key and serializing it with a timestamp.
- **Jinja2** (version 3.1.2): Jinja2 is a full-featured template engine for Python.
- **MarkupSafe** (version 2.1.3): MarkupSafe is a library for XML/HTML/XHTML markup safe string handling.
- **pillow** (version 10.2.0): Pillow is the friendly Python Imaging Library fork for PIL (Python Imaging Library).
- **pycodestyle** (version 2.11.1): pycodestyle is a tool to check Python code against style conventions.
- **requests** (version 2.31.0): Requests is an elegant and simple HTTP library for Python.
- **SQLAlchemy** (version 2.0.27): SQLAlchemy is the Python SQL toolkit and Object Relational Mapper (ORM).
- **typing_extensions** (version 4.10.0): Typing extensions for Python.
- **urllib3** (version 2.1.0): urllib3 is a powerful, sanity-friendly HTTP client for Python.
- **Werkzeug** (version 3.0.1): Werkzeug is a comprehensive WSGI web application library.

## Setup

1. Clone the repository: `git clone <repository_url>`
2. Install the dependencies: `pip install -r requirements.txt`
3. Change the version of itsdangerous by `pip install itsdangerous==2.0.1` 
4. Set up your database connection string and other configurations in `config.py`.
4. Run the Flask application: `flask run`

## Usage

- Visit the application in your browser and create an account.
- Once logged in, you can create, edit, and delete your posts.
- Explore other features of the application as per your requirements.

## Contributing

I am going to continue implementing additional features, so contributions are welcome! Feel free to open issues or submit pull requests to contribute to the project or send ideas of new features to add. 

## License

This project is licensed under the [MIT License](LICENSE).