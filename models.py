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
        return f"<Salesperson "\
            + f"id={self.id}," \
            + f"salesperson_name={self.first_name}>"

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer(), primary_key=True)
    queen_sold = Column(Integer(), default=0) 
    queen_price = Column(Integer())
    queen_amount = Column(Integer(), default=0)
    king_sold = Column(Integer(), default=0) 
    king_price = Column(Integer()) 
    king_amount = Column(Integer(), default=0)
    full_sold = Column(Integer(), default=0) 
    full_price = Column(Integer()) 
    full_amount = Column(Integer(), default=0)
    twin_sold = Column(Integer(), default=0)
    twin_price = Column(Integer()) 
    twin_amount = Column(Integer(), default=0) 
    company_id = Column(Integer(), ForeignKey('companies.id'))
    store_id = Column(Integer(), ForeignKey('stores.id'))
    
    salespersons = relationship('Salesperson', secondary=sale_salesperson, back_populates='sales')


    def __repr__(self):
        return f"<Sale (id={self.id},"\
        + f" queen_sold={self.queen_sold},\n"\
        + f" queen_price={self.queen_price},\n"\
        + f" queen_amount={self.queen_amount},\n"\
        + f" king_sold={self.king_sold},\n"\
        + f" king_price={self.king_price},\n"\
        + f" king_amount={self.king_amount},\n"\
        + f" full_sold={self.full_sold},\n"\
        + f" full_price={self.full_price},\n"\
        + f" full_amount={self.full_amount},\n"\
        + f" twin_sold={self.twin_sold},\n"\
        + f" twin_price={self.twin_price},\n"\
        + f" twin_amount={self.twin_amount})>"
    


