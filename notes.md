Steps I did, notes I need etc

### Creating virtualenv and installing packages

- python3 - checks the version => Python 3.8.13
- pipenv --python 3.8.13 - creates virtual environment
- pipenv install alembic sqlalchemy==1.4.41 - install alembic abd sqlalchemy (specifically the version we use at curriculum)
- git add . - git commit -m "message" - git push origin main - Commits the changes

### Initializing Migrations

- alembic init migrations - generates migration env (alembic init 'name of the file for migration')
- alembic ini conf - establish a connection to DB - line 58 or so 'sqlalchemy.url = sqlite:///sales.db' we can check alembic init file to see the connection string for the SQLAlchemy engine to talk with db
- env.py to set target metadata to the Base metadata. Our base is kinda sensor that detects changes. go around line 20ish. adjust strings there to target metadata Base class.
- created file models.py to create models and Base that we configured in env.py file
- In models.py, imported declarative_base and variable Base.
