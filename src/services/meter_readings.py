from abc import ABC, abstractmethod
import os
import protos.getMeterReadings_pb2 as getMeterReadings_pb2
import pandas as pd
from typing import List

class MeterReadings(ABC):
    @abstractmethod
    def fetch(self,start_time:str = None, end_time:str = None) -> List:
        pass


class MeterReadingsFromCSV(MeterReadings):
    def __init__(self,file_name):
        self.file_name=file_name
    
    def fetch(self,start_time:str = None, end_time:str = None) -> List :
        if type(self.file_name) == str :
            df=pd.read_csv(os.getcwd()+"/src/csv_datasets/"+self.file_name)
        
        elif type(self.file_name == list) :
            file_names=self.file_name
            append_data=pd.DataFrame()
            for file_name in file_names:
                df = pd.read_csv(os.getcwd()+"/src/csv_datasets/"+file_name)
                append_data = pd.concat((append_data, df))
            df=append_data.reset_index(drop=True)
            
        df.columns=['time','meter_usage']
        meter_usage_array=list(df['meter_usage'])
        time_array=list(df['time'])
        readings=[]
        for i in range(len(df)):
            reading=getMeterReadings_pb2.reading(meter_usage=meter_usage_array[i])
            reading.time.FromDatetime(pd.to_datetime(time_array[i]))
            readings.append(reading)
        return readings