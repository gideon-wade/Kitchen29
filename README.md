### Versionlist
Package | Python | Flask | Werkzeug
---     | ---    | ---   | ---
Version | 3.7.2  | 2.2.2 | 2.2.2


####To run program on localhost
Be under the projects directory and type in the terminal:

> python app.py

Open Link displayed in terminal.

###Database
To enable virtual mode

> python -m venv <PROJECT_NAME>

To install flask-sqlalchemy

> pip install flask-sqlalchemy

To create a new database (will overwrite existing database if used)
> flask shell 
> 
> db.create_all()
> 
> exit()

A new database as well as the old one can be created by using the comands above,
and changing the line: "'sqlite:///Kitchen29.db'" in app.py.
