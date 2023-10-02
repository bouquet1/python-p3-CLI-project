from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"
    
    id = Column(Integer(), primary_key=True)
    company_name = Column(String())

    stores = relationship('Store', backref='company')

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

    def __repr__(self):
        return f"<Store "\
            + f"id={self.id}," \
            + f"company_address={self.address_line_1}, {self.address_line_2},{self.apt_or_suite}, {self.city}, {self.state}, {self.zip_code}>"
    
    

