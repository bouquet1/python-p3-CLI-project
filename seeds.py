from models import Company, Store, Salesperson, Sale, sale_salesperson
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random

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

delete_data()

print("Start Seeding!")

companies = [
    Company(company_name="BedroomLand"),
    Company(company_name="REM Kings")
]
session.bulk_save_objects(companies)
session.commit()



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
   
    session.bulk_save_objects(stores)
    session.commit()
    return stores

populate_stores()



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

populate_salespersons()

def populate_sales():
    sales = [
        Sale(
            queen_sold=1,
            queen_price=16700,
            king_sold=0,
            king_price=0,
            full_sold=0,
            full_price=0,
            twin_sold=0,
            twin_price=0,
            company_id=1,
            store_id=1,
        ),
        Sale(
            queen_sold=1,
            queen_price=16700,
            king_sold=0,
            king_price=0,
            full_sold=0,
            full_price=0,
            twin_sold=0,
            twin_price=0,
            company_id=1,
            store_id=1,
        ),
        Sale(
            queen_sold=1,
            queen_price=16700,
            king_sold=0,
            king_price=0,
            full_sold=0,
            full_price=0,
            twin_sold=0,
            twin_price=0,
            company_id=1,
            store_id=1,
        ),
        Sale(
            queen_sold=1,
            queen_price=16700,
            king_sold=0,
            king_price=0,
            full_sold=0,
            full_price=0,
            twin_sold=0,
            twin_price=0,
            company_id=1,
            store_id=1,
        ),
        Sale(
            queen_sold=1,
            queen_price=16700,
            king_sold=0,
            king_price=0,
            full_sold=0,
            full_price=0,
            twin_sold=0,
            twin_price=0,
            company_id=1,
            store_id=1,
        ),
    ]

    session.bulk_save_objects(sales)
    session.commit()

    #associate sales with a random salesperson
    for sale in sales:
        numb_salesperson = len(session.query(Salesperson).all())
        salesperson_id = random.randint(1, numb_salesperson)
        salesperson = session.query(Salesperson).filter(Salesperson.id == salesperson_id).first()
        sale.salespersons.append(salesperson)

        session.add(salesperson)
        session.commit()
        # print(numb_salesperson)

    return sales

sales= populate_sales()

query_salespersons = session.query(Salesperson.first_name).all()
print(query_salespersons)


print("Done Seeding!")

import ipdb; ipdb.set_trace()

