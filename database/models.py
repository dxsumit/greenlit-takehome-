from typing import List, Optional
from sqlalchemy import ForeignKey, Text, Integer, Table, Column, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key = True)
    first_name:Mapped[str] = mapped_column(nullable = False)
    last_name:Mapped[str] = mapped_column(nullable = False)
    email:Mapped[str] = mapped_column(nullable = False, unique = True)
    minimum_fee:Mapped[int] = mapped_column(nullable = False)

    def __repr__(self) -> str:
        return f"<USER name = {self.first_name} {self.last_name}>"


class Film(Base):
    __tablename__ = "films"
    id:Mapped[int] = mapped_column(primary_key = True)
    title:Mapped[str] = mapped_column(Text, nullable = False, unique = True)
    description:Mapped[str] = mapped_column(Text)
    budget:Mapped[int] = mapped_column(nullable = False)
    release_year:Mapped[int]
    genres:Mapped[str] = mapped_column(Text, nullable = False)

    company_id:Mapped[str] = mapped_column(ForeignKey('companies.id', ondelete='CASCADE'), nullable = False)
    
    company:Mapped["Company"] = relationship(back_populates = 'films')

    def __repr__(self) -> str:  
        return f"<FILM title = {self.title}>"


class user_film_table(Base):
    __tablename__ = "user_film_table"
    id:Mapped[int] = mapped_column(primary_key = True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    film_id:Mapped[int] = mapped_column(ForeignKey('films.id', ondelete='CASCADE'))
    role:Mapped[str] = mapped_column(nullable = False)
    
    def __repr__(self) -> str:
        return f"<User_film_association role = {self.role}>"
    


class user_company_table(Base):
    __tablename__ = "user_company_table"
    id:Mapped[int] = mapped_column(primary_key = True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    company_id:Mapped[int] = mapped_column(ForeignKey('companies.id', ondelete='CASCADE'))
    role:Mapped[str] = mapped_column(nullable = False)
    
    def __repr__(self) -> str:
        return f"<User_film_association role = {self.role}>"


class Company(Base):
    __tablename__ = "companies"
    id:Mapped[int] = mapped_column(primary_key = True)
    name:Mapped[str] = mapped_column(Text, nullable = False)
    contact_email:Mapped[str] = mapped_column(nullable = False, unique = True)
    phone_number:Mapped[str]

    films:Mapped[List["Film"]] = relationship(back_populates = 'company')

    def __repr__(self) -> str:
        return f"<COMPANY name = {self.name}>"



