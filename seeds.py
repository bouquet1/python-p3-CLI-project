from models import Company
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sales.db")

Session = sessionmaker(bind=engine)
session = Session()

session.query(Company).delete()

print("Start Seeding!")

companies = [
    Company(company_name="BedroomLand"),
    Company(company_name="REM Kings")
]
print(companies)

session.bulk_save_objects(companies)
session.commit()

print("Done Seeding!")

