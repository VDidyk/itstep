from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Numeric, Text
from connection import Base
from sqlalchemy.orm import relationship


class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    phone = Column(String(50))
    salary = Column(Float(50))

    specializations = relationship('Specialization', secondary='doctors_specialization', back_populates='doctors')
    vacations = relationship('Vacation', back_populates='doctor')

    def __repr__(self):
        return f"<Doctor(name='{self.name}', surname='{self.surname}', phone='{self.phone}', salary={self.salary})>"


class Specialization(Base):
    __tablename__ = 'specializations'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    doctors = relationship('Doctor', secondary='doctors_specialization', back_populates='specializations')


class DoctorSpecialization(Base):
    __tablename__ = 'doctors_specialization'
    doctor_id = Column(Integer, ForeignKey('doctors.id'), primary_key=True)
    specialization_id = Column(Integer, ForeignKey('specializations.id'), primary_key=True)


class Vacation(Base):
    __tablename__ = 'vacations'
    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))

    doctor = relationship('Doctor', back_populates='vacations')


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    building = Column(Integer)
    financing = Column(Numeric(10, 2))
    name = Column(String(100))

    wards = relationship('Ward', back_populates='department')


class Ward(Base):
    __tablename__ = 'wards'
    id = Column(Integer, primary_key=True)
    building = Column(Integer)
    floor = Column(Integer)
    name = Column(String(20))
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship('Department', back_populates='wards')


class Sponsor(Base):
    __tablename__ = 'sponsors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    information = Column(Text)

    donations = relationship('Donation', back_populates='sponsor')


class Donation(Base):
    __tablename__ = 'donations'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    amount = Column(Numeric(10, 2))
    department_id = Column(Integer, ForeignKey('departments.id'))
    sponsor_id = Column(Integer, ForeignKey('sponsors.id'))

    sponsor = relationship('Sponsor', back_populates='donations')
