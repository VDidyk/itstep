from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from connection import Base


class Salesman(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    sales = relationship("Sale", back_populates="salesman")


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    sales = relationship("Sale", back_populates="customer")

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    amount = Column(Float)

    salesman = relationship("Salesman", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
