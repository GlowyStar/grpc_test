import grpc
import transactions_pb2
import transactions_pb2_grpc
from concurrent import futures
import time
from sqlalchemy import create_engine, select, text
from datetime import datetime

class TransactionsService(transactions_pb2_grpc.TransactionsServicer):
    def SumAmount(self, request, context):
        start_time_execution = time.time()

        start_time_request = datetime.fromtimestamp(request.start_time.seconds)
        end_time_request = datetime.fromtimestamp(request.end_time.seconds)

        engine = create_engine('postgresql://postgres:root@localhost:5432/testdb')
        with engine.connect() as connection:
            query = text("""
                WITH 
                sum1 AS (SELECT SUM(amount) FROM public.transactions WHERE user_id = 109 AND timestamp BETWEEN '2020-01-01' AND '2022-12-31'),
                sum2 AS (SELECT SUM(amount) FROM public.transactions WHERE user_id = 109 AND timestamp BETWEEN '2020-01-01' AND '2022-12-31'),
                sum3 AS (SELECT SUM(amount) FROM public.transactions WHERE user_id = 109 AND timestamp BETWEEN '2020-01-01' AND '2022-12-31'),
                sum4 AS (SELECT SUM(amount) FROM public.transactions WHERE user_id = 109 AND timestamp BETWEEN '2020-01-01' AND '2022-12-31'),
                sum5 AS (SELECT SUM(amount) FROM public.transactions WHERE user_id = 109 AND timestamp BETWEEN '2020-01-01' AND '2022-12-31')
                SELECT * FROM sum1, sum2, sum3, sum4, sum5;
            """)
            params = {'user_id': request.user_id, 'start_time': start_time_request, 'end_time': end_time_request}
            result = connection.execute(query, params)
            sum_amount = result.scalar()

        execution_time = time.time() - start_time_execution

        return transactions_pb2.SumAmountResponse(sum=sum_amount, execution_time=execution_time)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transactions_pb2_grpc.add_TransactionsServicer_to_server(TransactionsService(), server)
    server.add_insecure_port('localhost:50051')  # localhost:50051 or [::]:50051
    server.start()
    print('Server started, listening on port 50051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
