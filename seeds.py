from models import Company, Store, Salesperson, Sale, sale_salesperson
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

fake = Faker()


engine = create_engine("sqlite:///sales.db")
Session = sessionmaker(bind=engine)
session = Session()

session.query(Company).delete()
session.query(Store).delete()
session.query(Salesperson).delete()
session.query(Sale).delete()

print("Start Seeding!")

companies = [
    Company(company_name="BedroomLand"),
    Company(company_name="REM Kings")
]
session.bulk_save_objects(companies)
session.commit()
print(companies)

#seed stores db
stores = [
    Store(
    address = "56474 Sclanoit Ave", 
    apt_or_suite  = "Apt 19", 
    city = "Los Angeles", 
    state = "CA", 
    zip_code = "900163"
    ),
    Store(
    address = "1234 Elm Street",
    apt_or_suite = "Suite 102",
    city = "New York",
    state = "NY",
    zip_code = "10001"
    ),
    Store(
    address = "789 Oak Avenue",
    apt_or_suite = "Unit B",
    city = "Chicago",
    state = "IL",
    zip_code = "60611"
    ),
    Store(
    address = "9876 Birch Road",
    apt_or_suite = "Apt 3C",
    city = "Houston",
    state = "TX",
    zip_code = "77036"
    )
]


#use faker to seed salespersons
for _ in range(15):
    salespersons = [
    Salesperson(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        email = fake.ascii_company_email(),
        phone = fake.phone_number()
    )
]

# sales = [
#     Sale(company_name="BedroomLand"),
#     Sale(company_name="REM Kings")
# ]
# sale_salespersons = [

# ]

session.bulk_save_objects(stores)
session.commit()

print("Done Seeding!")

import ipdb; ipdb.set_trace()
# Dont forget to add ipdb as a dependency pipenv install ipdb
