from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Store, Salesperson, Sale

engine = create_engine("sqlite:///sales.db")
Session = sessionmaker(bind=engine)
session = Session()


def run():
    print("Welcome to the mattress sales tracker!\n")
    print("1.List of stores")
    print("2.List of salespersons")
    print("3.List of sales")

    #while loop to prompt user until a valid selection
    while True:
        user_input = input("Please make a selection (1-3): ")
        if user_input.isdigit():
            user_selection = int(user_input)
            if 1 <= user_selection <= 3:
                handle_user_selection(user_selection)
                #exit loop when walid selection is made
                break
            else:
                print("Incorrect selection. Please choose a selection 1-3.\n")
        else:
            print("Incorrect input. Please enter a number between 1 and 3.\n")


def list_stores(session):
    stores = session.query(Store).all()
    store_list =[]
    for store in stores:
        store_info = (
            f"<Store "
            f"id={store.id},\n"
            f"Company address={store.address}, {store.apt_or_suite}, "
            f"{store.city}, {store.state}, {store.zip_code}>"
        )
        store_list.append(store_info)

    return store_list

def list_salespersons(session):
    salespersons = session.query(Salesperson).all()
    salesperson_list =[]
    for salesperson in salespersons:
        salesperson_info = (
            f"<Salesperson "\
            + f"Id={salesperson.id}," 
            + f"Salesperson Information ={salesperson.first_name}, {salesperson.last_name}, {salesperson.email}, {salesperson.phone}>"
        )
        salesperson_list.append(salesperson_info)

    return salesperson_list


def list_sales(session):
    sales = session.query(Sale).all()
    sales_list = []
    for sale in sales:
        sale_info = (
            f"ID: {sale.id}, "
            f"Queen Sold: {sale.queen_sold}, "
            f"King Sold: {sale.king_sold}, "
            f"Full Sold: {sale.full_sold}, "
            f"Twin Sold: {sale.twin_sold}, "
            f"Company ID: {sale.company_id}, "
            f"Store ID: {sale.store_id}"
        )
        sales_list.append(sale_info)

    return sales_list


def handle_user_selection(selection):
    if selection == 1:
        print("You selected the List of the stores")
        stores = list_stores(session)
        for store in stores:
            print(store)
    elif selection == 2:
        print("You selected the List of the salespersons")
        salespersons = list_salespersons(session)
        for salesperson in salespersons:
            print(salesperson)
    elif selection == 3:
        print("You selected the List of the stores")
        sales = list_sales(session)
        for sale in sales:
            print(sale)

    # import ipdb; ipdb.set_trace()

run()
