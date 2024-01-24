# Створіть тритабличну базу даних Sales (Продажі). У цій
# базі даних мають бути таблиці: Sales (інформація про конкретні
# продажі), Salesmen (інформація про продавців), Customers (інформація про покупців). Створіть додаток для відображення
# даних з таблиць. Меню додатку має містити такий мінімальний набір звітів

from connection import Base, engine, Session
from sqlalchemy.orm import joinedload
import models
from sqlalchemy import func, desc, asc

import sys

sys.path.append('../../Libraries')
from Menu import Menu

Base.metadata.create_all(engine)
session = Session()


def show_salesmen():
    salesmen = session.query(models.Salesman).all()
    for salesman in salesmen:
        print(f"ID: {salesman.id}, Name: {salesman.first_name} {salesman.last_name}")


def add_salesman():
    salesman = models.Salesman(first_name=input("Enter first name: "), last_name=input("Enter the last name: "))

    session.add(salesman)
    session.commit()


def update_salesman():
    salesman_id = int(input("Enter the ID of the salesman to update: "))

    salesman = session.query(models.Salesman).filter(models.Salesman.id == salesman_id).first()

    if salesman:
        salesman.first_name = input("Enter new first name: ")
        salesman.last_name = input("Enter new last name: ")

        session.commit()
        print("Salesman updated successfully.")
    else:
        print("Salesman not found.")


def delete_salesman():
    salesman_id = int(input("Enter the ID of the salesman to delete: "))

    salesman = session.query(models.Salesman).filter(models.Salesman.id == salesman_id).first()

    if salesman:
        session.delete(salesman)

        session.commit()
        print("Salesman deleted successfully.")
    else:
        print("Salesman not found.")


def show_customers():
    customers = session.query(models.Customer).all()
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")


def add_customer():
    customer = models.Customer(first_name=input("Enter first name: "), last_name=input("Enter the last name: "))

    session.add(customer)
    session.commit()


def update_customer():
    customer_id = int(input("Enter the ID of the customer to update: "))

    customer = session.query(models.Customer).filter(models.Customer.id == customer_id).first()

    if customer:
        customer.first_name = input("Enter new first name: ")
        customer.last_name = input("Enter new last name: ")

        session.commit()
        print("Customer updated successfully.")
    else:
        print("Customer not found.")


def delete_customer():
    customer_id = int(input("Enter the ID of the customer to delete: "))

    customer = session.query(models.Customer).filter(models.Customer.id == customer_id).first()

    if customer:
        session.delete(customer)

        session.commit()
        print("Customer deleted successfully.")
    else:
        print("Customer not found.")


def show_sales():
    sales = session.query(models.Sale).options(joinedload(models.Sale.salesman), joinedload(models.Sale.customer)).all()

    sales_list(sales)


def sales_entity(sale):
    salesman = sale.salesman
    customer = sale.customer

    if sale:
        print(f"Sale ID: {sale.id}, Amount: {sale.amount}")
        print(f"Salesman: {salesman.first_name} {salesman.last_name}")
        print(f"Customer: {customer.first_name} {customer.last_name}")
        print("-" * 30)
    else:
        print("No sales found.")


def sales_list(sales):
    for sale in sales:
        sales_entity(sale)


def add_sale():
    customer = models.Sale(salesman_id=int(input("Enter the ID of salesman: ")),
                           customer_id=int(input("Enter the ID of customer: ")),
                           amount=float(input("Enter the amount: ")))

    session.add(customer)
    session.commit()


def update_sale():
    sale_id = int(input("Enter the ID of the sale to update: "))

    sale = session.query(models.Sale).filter(models.Sale.id == sale_id).first()

    if sale:
        sale.amount = float(input("Enter new amount: "))
        sale.customer_id = input("Enter new customer id: ")
        sale.salesman_id = input("Enter new salesman id: ")

        session.commit()
        print("Sale updated successfully.")
    else:
        print("Sale not found.")


def show_statistics():
    # customer_id = int(input("Enter the customer ID: "))
    # salesman_id = int(input("Enter the salesman ID: "))
    #
    customer_id = 1
    salesman_id = 1

    # ---------------
    print("Відображення угод конкретного продавця:")
    sales_list(session.query(models.Sale).filter(models.Sale.salesman_id == salesman_id).all())

    # ---------------
    print('Запит на знаходження угоди (продажу) з цією максимальною сумою')
    max_sale = session.query(models.Sale).order_by(desc(models.Sale.amount)).first()
    sales_entity(max_sale)

    # ---------------
    print('Відображення мінімальної за сумою угоди;')
    min_sale = session.query(models.Sale).order_by(asc(models.Sale.amount)).first()
    sales_entity(min_sale)

    # ---------------
    print("Відображення максимальної суми угоди для конкретного продавця;")
    max_sale = session.query(models.Sale).filter(models.Sale.salesman_id == salesman_id).order_by(
        desc(models.Sale.amount)).first()
    sales_entity(max_sale)
    # ---------------
    print("Відображення мінімальної за сумою угоди для конкретного продавця;")
    min_sale = session.query(models.Sale).filter(models.Sale.salesman_id == salesman_id).order_by(
        asc(models.Sale.amount)).first()
    sales_entity(min_sale)

    # ---------------
    print("Відображення максимальної суми угоди для конкретного покупця;")
    max_sale = session.query(models.Sale).filter(models.Sale.customer_id == customer_id).order_by(
        desc(models.Sale.amount)).first()
    sales_entity(max_sale)
    # ---------------
    print("Відображення мінімальної за сумою угоди для конкретного покупця;")
    min_sale = session.query(models.Sale).filter(models.Sale.customer_id == customer_id).order_by(
        asc(models.Sale.amount)).first()
    sales_entity(min_sale)
    # ---------------
    print("Відображення продавця з максимальною сумою продажів за всіма угодами;")
    top_salesman = session.query(
        models.Sale.salesman_id,
        func.sum(models.Sale.amount).label('total_sales')
    ).group_by(models.Sale.salesman_id).order_by(func.sum(models.Sale.amount).desc()).first()

    if top_salesman:
        salesman = session.query(models.Salesman).filter(models.Salesman.id == top_salesman.salesman_id).first()
        print(
            f"Top Selling Salesman: {salesman.first_name} {salesman.last_name}, Total Sales: {top_salesman.total_sales}")
    else:
        print("No sales records found.")
    # ---------------
    print("Відображення продавця з мінімальною сумою продажів за всіма угодами;")
    top_salesman = session.query(
        models.Sale.salesman_id,
        func.sum(models.Sale.amount).label('total_sales')
    ).group_by(models.Sale.salesman_id).order_by(func.sum(models.Sale.amount).asc()).first()

    if top_salesman:
        salesman = session.query(models.Salesman).filter(models.Salesman.id == top_salesman.salesman_id).first()
        print(
            f"Smallest Selling Salesman: {salesman.first_name} {salesman.last_name}, Total Sales: {top_salesman.total_sales}")
    else:
        print("No sales records found.")

    # ---------------
    print("Відображення покупця з максимальною сумою покупок за всіма угодами")
    top_salesman = session.query(
        models.Sale.customer_id,
        func.sum(models.Sale.amount).label('total_sales')
    ).group_by(models.Sale.customer_id).order_by(func.sum(models.Sale.amount).desc()).first()

    if top_salesman:
        customer = session.query(models.Customer).filter(models.Customer.id == top_salesman.customer_id).first()
        print(
            f"Top Customer: {customer.first_name} {customer.last_name}, Total Sales: {top_salesman.total_sales}")
    else:
        print("No sales records found.")

    # -------------
    print('Відображення середньої суми покупки для конкретного покупця;')

    average_sale_amount = session.query(
        func.avg(models.Sale.amount).label('average_amount')
    ).filter(models.Sale.customer_id == customer_id).scalar()

    if average_sale_amount is not None:
        print(f"Average sale amount for customer ID {customer_id}: {average_sale_amount:.2f}")
    else:
        print(f"No sales records found for customer ID {customer_id}.")

    # -------------
    print('Відображення середньої суми покупки для конкретного продавця.')

    average_sale_amount = session.query(
        func.avg(models.Sale.amount).label('average_amount')
    ).filter(models.Sale.salesman_id == salesman_id).scalar()

    if average_sale_amount is not None:
        print(f"Average sale amount for salesman ID {salesman_id}: {average_sale_amount:.2f}")
    else:
        print(f"No sales records found for salesman ID {salesman_id}.")


def delete_sale():
    sale_id = int(input("Enter the ID of the sale to delete: "))

    sale = session.query(models.Sale).filter(models.Sale.id == sale_id).first()

    if sale:
        session.delete(sale)

        session.commit()
        print("Sale deleted successfully.")
    else:
        print("Sale not found.")


menu = Menu()

menu.append("Show statistics", show_statistics)
menu.append("Show salesmen", show_salesmen)
menu.append("Add salesman", add_salesman)
menu.append("Update salesman", update_salesman)
menu.append("Delete salesman", delete_salesman)
menu.append("Show customers", show_customers)
menu.append("Add customer", add_customer)
menu.append("Update customer", update_customer)
menu.append("Delete customer", delete_customer)
menu.append("Show sales", show_sales)
menu.append("Add sale", add_sale)
menu.append("Update sale", update_sale)
menu.append("Delete sale", delete_sale)

menu.start()

session.close()
