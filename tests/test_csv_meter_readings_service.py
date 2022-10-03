from services.meter_readings import MeterReadingsFromCSV
from datetime import datetime

def test_csv_file_is_retrieved_by_checking_data_types():
    readings = MeterReadingsFromCSV(file_name="meterusage.1663137955.csv").fetch()
    assert (readings) != None
    assert (type(readings[0].meter_usage)) == float
    assert (type(readings[0].time.ToDatetime())) == datetime
