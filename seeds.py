from models import Company
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sales.db")

Session = sessionmaker(bind=engine)
session = Session()

session.query(Company).delete()

print("testing seeds.py to populate DB")

companies = [
    Company(company_name="BedroomLand"),
    Company(company_name="REM Kings")
]

session.bulk_save_objects(companies)
session.commit()

print("Done Seeding!")
