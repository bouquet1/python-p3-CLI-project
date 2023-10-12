from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Table


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

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
    address = Column(String())
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
    

sale_salesperson = Table(
    "sale_salespersons",
    Base.metadata,
    Column("id", Integer(), primary_key=True),
    Column("salesperson_id", ForeignKey("salespersons.id")),
    Column("sale_id", ForeignKey("sales.id"))  
)
    
class Salesperson(Base):
    __tablename__ = "salespersons"
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    email = Column(String())
    phone = Column(String())
    store_id = Column(Integer(), ForeignKey('stores.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))
    # to make it easier for user

    sales = relationship('Sale', secondary=sale_salesperson, back_populates='salespersons')

    def __repr__(self):
        return f"<Company "\
            + f"id={self.id}," \
            + f"company_name={self.company_name}>"

class Mattress(Base):
    __tablename__ = "matresses"
    
    id = Column(Integer(), primary_key=True)
    queen_sold = Column(Integer(), default=0) 
    king_sold = Column(Integer(), default=0) 
    full_sold = Column(Integer(), default=0) 
    twin_sold = Column(Integer(), default=0)
    queen_price = Column(Integer())
    king_price = Column(Integer()) 
    full_price = Column(Integer()) 
    twin_price = Column(Integer()) 
    company_id = Column(Integer(), ForeignKey('companies.id'))
    store_id = Column(Integer(), ForeignKey('stores.id'))
    
    salespersons = relationship('Salesperson', secondary=sale_salesperson, back_populates='sales')


    def __repr__(self):
        return f"<Company "\
            + f"id={self.id}," \
            + f"company_name={self.company_name}>"

