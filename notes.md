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
- In models.py, imported declarative_base and variable Base. I created Company class which will be my companies table. Defined attributes(columns). Now I need to turn this schema into DB. => through alembic. -alembic revision --autogenerate -m "message" - then 'alembic upgrade head' after those commands I see companies table is created but it is empty cuz I didn't seed any info in seeds.py yet. I created seeds.py and add some data to populate my db.(I need instanes for rows kinda)
- then run python3 seeds.py to execute seeds.py so populate db
- Done for today
- Another day for migrations
- start w pipenv shell
-

NOTES FOR BLOG: schema and migrations
schema is a blueprint (recipe you noted down)
base class is a sensor
migrations are python instructions that specify how to construct and modify a DB.
changes and modifications in a recipe f.e Tom's lecture is great for inspiration.
