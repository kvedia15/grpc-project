import json
from fastapi import FastAPI
import uvicorn
import grpc
from google.protobuf.json_format import MessageToJson
from protos.getMeterReadings_pb2_grpc import GetMeterReadingsStub
from protos.getMeterReadings_pb2 import GetMeterReadingsRequest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/meter-readings")
def get_meter_readings_from_grpc_server():
    channel = grpc.insecure_channel("localhost:50051")
    client = GetMeterReadingsStub(channel)
    response = client.GetData(GetMeterReadingsRequest())
    return json.loads(MessageToJson(response))

if __name__ == "__main__":
    uvicorn.run("app:app", port=8200, reload=True)
    
    
    
    