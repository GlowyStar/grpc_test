from sqlalchemy import create_engine, Table, MetaData
from datetime import datetime, timedelta
import random

USER = ''
PASSWORD = ''
DB_NAME = ''

def get_engine():
    return create_engine(f'postgresql://{USER}:{PASSWORD}@localhost:5432/{DB_NAME}')

def get_transactions_table(engine):
    metadata = MetaData()
    return Table('transactions', metadata, autoload_with=engine)

def generate_data(start_date, num_records):
    return [{
        "amount": random.uniform(1.0, 1000.0),  # Случайное значение от 1 до 1000
        "timestamp": start_date + timedelta(days=i),  # Каждый день с 01.01.2020
        "user_id": random.randint(1, 1000)  # Случайный пользователь от 1 до 1000
    } for i in range(num_records)]

def insert_data(engine, transactions, data):
    with engine.begin() as connection:
        for row in data:
            connection.execute(transactions.insert().values(**row))

if __name__ == "__main__":
    engine = get_engine()
    transactions = get_transactions_table(engine)
    data = generate_data(datetime(2020, 1, 1), 1000000)
    insert_data(engine, transactions, data)
