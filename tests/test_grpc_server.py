from unittest.mock import MagicMock
from protos.getMeterReadings_pb2 import GetMeterReadingsRequest,GetMeterReadingsResponse
import server


class TestServer:
    def test_retrieve_1_csv_file(self):
        request = GetMeterReadingsRequest()
        context=MagicMock()
        csv_data=server.GetMeterReadings()
        resp=csv_data.GetData(request,context)
        assert len(resp.readings) > 0
        assert resp.readings[0].meter_usage != None

