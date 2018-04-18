# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import sum_pb2 as proto_dot_sum__pb2


class VectorServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Info = channel.unary_unary(
        '/sum.VectorService/Info',
        request_serializer=proto_dot_sum__pb2.Empty.SerializeToString,
        response_deserializer=proto_dot_sum__pb2.ServerInfo.FromString,
        )
    self.Create = channel.unary_unary(
        '/sum.VectorService/Create',
        request_serializer=proto_dot_sum__pb2.Record.SerializeToString,
        response_deserializer=proto_dot_sum__pb2.Response.FromString,
        )
    self.Update = channel.unary_unary(
        '/sum.VectorService/Update',
        request_serializer=proto_dot_sum__pb2.Record.SerializeToString,
        response_deserializer=proto_dot_sum__pb2.Response.FromString,
        )
    self.Read = channel.unary_unary(
        '/sum.VectorService/Read',
        request_serializer=proto_dot_sum__pb2.Query.SerializeToString,
        response_deserializer=proto_dot_sum__pb2.Response.FromString,
        )
    self.Delete = channel.unary_unary(
        '/sum.VectorService/Delete',
        request_serializer=proto_dot_sum__pb2.Query.SerializeToString,
        response_deserializer=proto_dot_sum__pb2.Response.FromString,
        )


class VectorServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Info(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Read(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_VectorServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Info': grpc.unary_unary_rpc_method_handler(
          servicer.Info,
          request_deserializer=proto_dot_sum__pb2.Empty.FromString,
          response_serializer=proto_dot_sum__pb2.ServerInfo.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=proto_dot_sum__pb2.Record.FromString,
          response_serializer=proto_dot_sum__pb2.Response.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=proto_dot_sum__pb2.Record.FromString,
          response_serializer=proto_dot_sum__pb2.Response.SerializeToString,
      ),
      'Read': grpc.unary_unary_rpc_method_handler(
          servicer.Read,
          request_deserializer=proto_dot_sum__pb2.Query.FromString,
          response_serializer=proto_dot_sum__pb2.Response.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=proto_dot_sum__pb2.Query.FromString,
          response_serializer=proto_dot_sum__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sum.VectorService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
