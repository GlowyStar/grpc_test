# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transactions_pb2 as transactions__pb2


class TransactionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SumAmount = channel.unary_unary(
                '/Transactions/SumAmount',
                request_serializer=transactions__pb2.SumAmountRequest.SerializeToString,
                response_deserializer=transactions__pb2.SumAmountResponse.FromString,
                )


class TransactionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SumAmount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SumAmount': grpc.unary_unary_rpc_method_handler(
                    servicer.SumAmount,
                    request_deserializer=transactions__pb2.SumAmountRequest.FromString,
                    response_serializer=transactions__pb2.SumAmountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Transactions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Transactions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SumAmount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Transactions/SumAmount',
            transactions__pb2.SumAmountRequest.SerializeToString,
            transactions__pb2.SumAmountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
