# Как запустить проект: 
1) скачать репозиторий: `git clone <ссылка проекта>` 
2) `перейти к папке проекта: `cd <путь к папке проекта>`
3) создать виртуальное окружение: `python -m venv venv`
4) активировать окружение: `venv\Scripts\activate`
5) установить зависимости: `pip install -r requirements.txt`
6) перейти в db/db_init, добавить данные своей бд в переменные USER = '', PASSWORD = '',DB_NAME = '', в if __name__ == "__main__"разкомментить функцию create_db() чтобы создать таблицу, обратно закомментить
7) перейти в generate_records.py и запустить 1 раз файл чтобы добавить 1000000 записей
8) обратно перейти в db/db_init разкомментить create_indexes(), это создат индексы
9) Я оставил файлы transactions_pb2.py, transactions_pb2_grpc.py, но если вдруг их не будет нужно прописать: `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. transactions.proto` в консоль, это их создаст (я всетаки советую удалить эти файлы и создать заново командой)
10) запустить server.py и протестировать в postman

Статься как тестировать gRPC в postman: https://habr.com/ru/companies/otus/articles/699616/