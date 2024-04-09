from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, DateTime, Float, Index

USER = ''
PASSWORD = ''
DB_NAME = ''

engine = create_engine(f'postgresql://{USER}:{PASSWORD}@localhost:5432/{DB_NAME}')

metadata = MetaData()


def create_db():
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@localhost:5432/{DB_NAME}')
    metadata = MetaData()

    transactions = Table('transactions', metadata,
        Column('id', Integer, primary_key=True),
        Column('amount', Float),
        Column('timestamp', DateTime),
        Column('user_id', Integer)
    )
    metadata.create_all(engine)

def create_indexes():
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@localhost:5432/{DB_NAME}')
    metadata = MetaData()

    transactions = Table('transactions', metadata, autoload_with=engine)
    Index('idx_transactions_user_id', transactions.c.user_id).create(bind=engine)
    Index('idx_transactions_user_id_timestamp', transactions.c.user_id, transactions.c.timestamp).create(bind=engine)

if __name__ == "__main__":
    # create_db()  # Создание таблицы
    # create_indexes()  # Перед созданием индексов советую перейти в файл generate_records.py и создать сначала записи
    pass


# Сразу скажу что понимаю, что такое количество индексов очень сильно может замедлить процесс записи в бд,
# но по тз было сказано что мы работаем исключительно с READ data поэтому представим что
# в нашем случае записи в бд не делаются, либо делаются очень редко.
# Так-же в самой реализации gRPC будет нелепо громоздкий запрос, это сделано опять-же для исключительно для теста

