from client.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_run_endpoint():
    response = client.get("/meter-readings")
    data=response.json()
    readings=data["readings"]
    readings_length=len(readings)
    assert readings_length > 0

def test_data_is_fetched():
    response = client.get("/meter-readings")
    data=response.json()
    readings=data["readings"]
    readings_length=len(readings)
    assert readings_length > 0

def test_data_types():
    response = client.get("/meter-readings")
    data=response.json()
    readings=data["readings"]
    assert type(readings[0]["time"])==str
    assert type(readings[0]["meterUsage"])==float