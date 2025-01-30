# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import src.grpc_adapter_one.api_pb2 as api__pb2


class ApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sayHello = channel.unary_unary(
                '/api.Api/sayHello',
                request_serializer=api__pb2.HelloRequest.SerializeToString,
                response_deserializer=api__pb2.Hello.FromString,
                )
        self.getAll = channel.unary_unary(
                '/api.Api/getAll',
                request_serializer=api__pb2.ApiRequest.SerializeToString,
                response_deserializer=api__pb2.Items.FromString,
                )
        self.getStream = channel.unary_stream(
                '/api.Api/getStream',
                request_serializer=api__pb2.ApiRequest.SerializeToString,
                response_deserializer=api__pb2.Item.FromString,
                )


class ApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.sayHello,
                    request_deserializer=api__pb2.HelloRequest.FromString,
                    response_serializer=api__pb2.Hello.SerializeToString,
            ),
            'getAll': grpc.unary_unary_rpc_method_handler(
                    servicer.getAll,
                    request_deserializer=api__pb2.ApiRequest.FromString,
                    response_serializer=api__pb2.Items.SerializeToString,
            ),
            'getStream': grpc.unary_stream_rpc_method_handler(
                    servicer.getStream,
                    request_deserializer=api__pb2.ApiRequest.FromString,
                    response_serializer=api__pb2.Item.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.Api', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Api(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Api/sayHello',
            api__pb2.HelloRequest.SerializeToString,
            api__pb2.Hello.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Api/getAll',
            api__pb2.ApiRequest.SerializeToString,
            api__pb2.Items.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.Api/getStream',
            api__pb2.ApiRequest.SerializeToString,
            api__pb2.Item.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
