from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData


# convention = {
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# }

# metadata = MetaData(naming_convention=convention)

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"
    
    id = Column(Integer(), primary_key=True)
    company_name = Column(String())

    stores = relationship('Store', backref='company')
    salespersons = relationship('Salesperson', backref='company')

    def __repr__(self):
        return f"<Company "\
            + f"id={self.id}," \
            + f"company_name={self.company_name}>"
            
    
class Store(Base):
    __tablename__ = "stores"
    
    id = Column(Integer(), primary_key=True)
    address_line_1 = Column(String())
    address_line_2 = Column(String())
    apt_or_suite = Column(String())
    city = Column(String())
    state = Column(String())
    zip_code = Column(String())
    company_id = Column(Integer(), ForeignKey('companies.id'))

    salespersons = relationship('Salesperson', backref='store')

    def __repr__(self):
        return f"<Store "\
            + f"id={self.id}," \
            + f"company_address={self.address_line_1}, {self.address_line_2},{self.apt_or_suite}, {self.city}, {self.state}, {self.zip_code}>"
    
class Salesperson(Base):
    __tablename__ = "salespersons"
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    email = Column(String())
    phone = Column(String())
    store_id = Column(Integer(), ForeignKey('stores.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))


    def __repr__(self):
        return f"<Company "\
            + f"id={self.id}," \
            + f"company_name={self.company_name}>"

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer(), primary_key=True)
    set_sold = Column(Integer())
    set_price = Column(Integer())
    mattress_sold = Column(Integer())
    mattress_price = Column(Integer())
    
    # company_id = Column(Integer(), ForeignKey('companies.id'))
    # store_id = Column(Integer(), ForeignKey('stores.id'))

    def __repr__(self):
        return f"<Company "\
            + f"id={self.id}," \
            + f"company_name={self.company_name}>"

