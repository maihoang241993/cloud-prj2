import grpc
import locations_pb2
import locations_pb2_grpc

# example create location
channel = grpc.insecure_channel("localhost:30002")
stub = locations_pb2_grpc.LocationServiceStub(channel)
def create_location(stub):
    new_location = locations_pb2.LocationMessage(
        person_id="001",
        creation_time="2020-08-15 10:37:06.000000",
        latitude="001",
        longitude="100"
    )
    response = stub.LocationCreate(new_location)

create_location(stub)
