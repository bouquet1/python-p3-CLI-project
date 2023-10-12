# python-p3-CLI-project

### Creating virtualenv and installing packages

- python3 - checks the version => Python 3.8.13
- pipenv --python 3.8.13 - creates virtual environment
- pipenv install alembic sqlalchemy==1.4.41 - install alembic abd sqlalchemy (specifically the version we use at curriculum)
- git add . - git commit -m "message" - git push origin main - Commits the changes

### Initializing Migrations

- alembic init migrations

# SALES RECORDS - Phase 3 CLI project

Description
This CLI Application uses SQLAlchemy, Python, and Alembic to show what I have learned.

App has Classes/Tables:

- Companies,
- Stores that belong to that Companies,
- Salespersons that belong to Companies and the Stores,
- Sales that belong to Salespersons, Stores, and Companies.

App reflects relationships:

- A company has multiple stores, salespersons, and sales.
- A store has one company, many salespersons, and sales.
- A salesperson has one company, one store, and many sales.
- A sale is belong to one company, one store, many salespersons.

So, salespersons and sales has many-to-many relationship while other has one-to-many relationship.

My repository includes a built-in seeding file for populating the database with test data. This functionality facilitates comprehensive testing of the application's features.

### Installation

In your teminal fork and copy the SSH, navigate to the folder you wish to clone the repo into and use this syntax to clone it to uour local environment.

git clone copied SSH URL

Then, open it with your code editor.

### Usage

Inside your code editor's teminal run

pipenv install && pipenv shell

Executing 'pipenv shell' will guide us into the virtual environment, within which the application will operate.

To seed the database with some fake data to test out the features of the app run the following (optional) command:

python seeds.py
Then to start the app run the following command:

python run.py

WRITE THIS PAERT AGAIN it is from canvas

Information
This application while functional, does not include many aspects one might expect an Event planner to have. This project was built with the goal of displaying the ability to create python classes and successfully map them to a database using SQLAlchemy. Then manage proper database migrations using Alembic when creating the relationships between said classes.

Improvements / Roadmap
Add method to edit owned event name.
Add method to edit username
Add more attributes to the Event Class so that it feels more like a real event (due to time constraints, left some of these out in favor of building out the CLI application)
Add more secure login with User Password. Would probably only add this to 1, show that i'm capable and 2, if I was going to expand this into a fully fledged application
Resources
https://pypi.org/ -- Used this site to find the CLI text color changer, as well as a package to create the banner message
Check pipfile for full list of packages used

https://docs.sqlalchemy.org/en/14/index.html -- Constantly had to check and recheck the SQLAlchemy docs while building out my classes and ensuring the relationships were working as intended

Huge thanks to the Flatiron instructors. Everything that went into creating this project felt extremely overwhelming trying to learn at once. Thru watching and rewatching some of the demonstrations and lectures, I was able to work my way through this project and create a proper CLI application!!! Thank you!
