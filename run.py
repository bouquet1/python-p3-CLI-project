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
            user_selection = int(input)
            if 1 <= user_selection <= 3:
                handle_user_selection(user_selection)
                #exit loop when walid selection is amde
                break
            else:
                print("Incorrect selection. Please choose a selection 1-3.\n")
        else:
            print("Incorrect input. Please enter a number between 1 and 3.\n")


def list_stores(session):
    stores = session.query(Store).all()
    store_list =[]
    for store in stores:
        store_info = f"<Store "\
            + f"id={store.id}," \
            + f"company_address={store.address_line_1}, {store.address_line_2},{store.apt_or_suite}, {store.city}, {store.state}, {store.zip_code}>"
        store_list.append(store_info)

    return '\n'.join(store_list)


def handle_user_selection(selection):
    if selection == 1:
        print("You selected the List of the stores")
        list_stores(session)

        import ipdb; ipdb.set_trace()



run()
