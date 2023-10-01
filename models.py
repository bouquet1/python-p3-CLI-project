from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"
    
    id = Column(Integer(), primary_key=True)
    company_name = Column(String())

    def __repr__(self):
        return f"\n <Company "\
            + f"id={self.id}," \
            + f"company_name={self.company_name}>"
