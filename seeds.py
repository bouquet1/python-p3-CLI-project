from models import Company, Store, Salesperson, Sale, sale_salesperson
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker

fake = Faker()


engine = create_engine("sqlite:///sales.db")
Session = sessionmaker(bind=engine)
session = Session()

def delete_data():
    session.query(Company).delete()
    session.query(Store).delete()
    session.query(Salesperson).delete()
    session.query(Sale).delete()
    session.query(sale_salesperson).delete()
    session.commit()


print("Start Seeding!")

companies = [
    Company(company_name="BedroomLand"),
    Company(company_name="REM Kings")
]
session.bulk_save_objects(companies)
session.commit()
print(companies)

#seed stores db
def populate_stores():
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
    
    session.add_all(stores)
    session.commit()
    return stores


def populate_salespersons():
    salespersons = []
    for _ in range(20):
        salesperson = Salesperson(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.ascii_company_email(),
            phone = fake.phone_number()
        )
        session.add(salesperson)
        session.commit()
        salespersons.append(salesperson)
    return salespersons


def populate_sales():
    sales = [
        Sale(
        set_sold = 1, 
        set_price = 16700, 
        only_mattress_sold = 0, 
        mattress_price = 0
        ),
        Sale(
        set_sold = 0, 
        set_price = 0, 
        only_mattress_sold = 1, 
        mattress_price = 6200
        ),
        Sale(
        set_sold = 1, 
        set_price = 16700, 
        only_mattress_sold = 0, 
        mattress_price = 0
        ),
        Sale(
        set_sold = 0, 
        set_price = 0, 
        only_mattress_sold = 1, 
        mattress_price = 5800
        ),
    ]
    
    session.add_all(sales)
    session.commit()
    return sales

print("Done Seeding!")

import ipdb; ipdb.set_trace()
# Dont forget to add ipdb as a dependency pipenv install ipdb
