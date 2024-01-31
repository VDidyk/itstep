from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = 'Departments'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Financing = Column(Float, nullable=False, default=0)
    Name = Column(String(100), nullable=False, unique=True)


class Faculty(Base):
    __tablename__ = 'Faculties'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Dean = Column(String(255), nullable=False)
    Name = Column(String(100), nullable=False, unique=True)

    DepartmentId = Column(Integer, ForeignKey('Departments.Id'))
    department = relationship('Department', back_populates='faculties')


class Group(Base):
    __tablename__ = 'Groups'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(10), nullable=False, unique=True)
    Rating = Column(Integer, nullable=False)
    Year = Column(Integer, nullable=False)

    teachers = relationship('Teacher', secondary='GroupTeacher')


class Teacher(Base):
    __tablename__ = 'Teachers'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    EmploymentDate = Column(Date, nullable=False)
    IsAssistant = Column(Boolean, nullable=False, default=False)
    IsProfessor = Column(Boolean, nullable=False, default=False)
    Name = Column(String, nullable=False)
    Position = Column(String, nullable=False)
    Premium = Column(Float, nullable=False, default=0)
    Salary = Column(Float, nullable=False)
    Surname = Column(String, nullable=False)

    groups = relationship('Group', secondary='GroupTeacher')


class GroupTeacher(Base):
    __tablename__ = 'GroupTeacher'

    GroupId = Column(Integer, ForeignKey('Groups.Id'), primary_key=True)
    TeacherId = Column(Integer, ForeignKey('Teachers.Id'), primary_key=True)
