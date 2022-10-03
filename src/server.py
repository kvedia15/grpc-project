from concurrent import futures
import logging
import os

from services.meter_readings import MeterReadingsFromCSV
import grpc
import protos.getMeterReadings_pb2 as getMeterReadings_pb2
import protos.getMeterReadings_pb2_grpc as getMeterReadings_pb2_grpc
import pandas as pd

class GetMeterReadings(getMeterReadings_pb2_grpc.GetMeterReadingsServicer):
    def GetData(self, request, context):
        data=MeterReadingsFromCSV(file_name="meterusage.1663137955.csv")
        readings=data.fetch()
        return getMeterReadings_pb2.GetMeterReadingsResponse(readings=readings)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    getMeterReadings_pb2_grpc.add_GetMeterReadingsServicer_to_server(GetMeterReadings(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at https://localhost:50051. Awaiting jobs...")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
