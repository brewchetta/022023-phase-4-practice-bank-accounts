#!/usr/bin/env python3

from app import app
from models import db, Bank, Customer, Account
from faker import Faker
import random

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")


        print("Deleting old data...")

        Account.query.delete()
        Bank.query.delete()
        Customer.query.delete()


        print("Creating banks...")

        banks_list = []

        for _ in range(10):
            bank = Bank(name=faker.company())
            banks_list.append(bank)

        db.session.add_all(banks_list)
        db.session.commit()


        print("Creating customers...")

        customers_list = []

        for _ in range(100):
            customer = Customer(first_name=faker.first_name(), last_name=faker.last_name())
            customers_list.append(customer)

        db.session.add_all(customers_list)
        db.session.commit()


        print("Creating accounts...")

        accounts = []
        account_choices = ['checking', 'savings', 'business', 'crypto', 'brokerage', 'cd', 'retirement', 'money laundering']

        for _ in range(1000):
            account = Account(
                balance=random.randint(0,1000000), 
                account_type=random.choice(account_choices),
                bank=random.choice(banks_list),
                customer=random.choice(customers_list)
            )
            accounts.append(account)

        db.session.add_all(accounts)
        db.session.commit()


        print("Seeding complete!")
