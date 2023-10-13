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

### Information

While this application functions, it falls short of typical expectations for a retail Sales Tracker. I purposefully created this project to showcase my ability to craft Python classes and skillfully map them to a database using SQLAlchemy. Moreover, I adeptly oversaw database migrations with Alembic to establish connections between these classes. I'm fully aware of the need for enhancements, and in the 'Improvements' section below, I provide my self-reflection on how I plan to elevate the project.

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

## Improvements / Roadmap

Delete the old database and create a new database with a better ERD to build relationships between a Mattress, Sale, Salesperson, and Customer.

My schema plan:

- My app should allow user to track sales transactions, associate them with specific products (mattresses), and identify the salesperson and customer involved in each transaction.
- Each Sale record associates a specific Mattress with a Salesperson and a Customer.
- Should have a login with User Password.
- My app should expand and customize the schema based on specific requirements, such as adding more attributes to each table or incorporating additional entities.

### Resources

https://docs.sqlalchemy.org/en/14/index.html -- This source was my main source after the lectures, class notes, and articles that are provided to me by Flatiron School and my instructors/coaches. I repeadetly checked the SQLAlchemy docs while building out my classes and relationships.

To see the full list of packages that is used, please check pipfile
