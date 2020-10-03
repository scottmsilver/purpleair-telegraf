#!/usr/bin/python3
import urllib.request
import sys
import json
from metric import Metric
from enum import Enum

# Return the file in fileName as string.
def fileToString(fileName):
  with open(fileName, 'r') as file:
    data = file.read().replace('\n', '')
    return data

# PurpleAir monitoring id  
monitorUrl = sys.argv[1]
rawContents = urllib.request.urlopen(monitorUrl).read()


# Load the JSON and create a proper dictionary with name values
# The actual JSON content looks like this, so I read the fields and data and put them in a dictionary.
'''
{'SensorId': '50:2:91:f2:3f:8f', 'DateTime': '2020/10/02T21:00:12z', 'Geo': 'PurpleAir-3f8f', 'Mem': 18656, 'memfrag': 29, 'memfb': 13216, 'memcs': 848, 'Id': 50217, 'lat': 37.360298, 'lon': -122.105698, 'Adc': 0.05, 'loggingrate': 15, 'place': 'outside', 'version': '6.01', 'uptime': 1654801, 'rssi': -82, 'period': 120, 'httpsuccess': 83108, 'httpsends': 83195, 'hardwareversion': '2.0', 'hardwarediscovered': '2.0+BME280+PMSX003-B+PMSX003-A', 'current_temp_f': 98, 'current_humidity': 26, 'current_dewpoint_f': 57, 'pressure': 1007.68, 'p25aqic_b': 'rgb(241,0,11)', 'pm2.5_aqi_b': 176, 'pm1_0_cf_1_b': 89.0, 'p_0_3_um_b': 16206.0, 'pm2_5_cf_1_b': 156.0, 'p_0_5_um_b': 4478.0, 'pm10_0_cf_1_b': 204.0, 'p_1_0_um_b': 1154.0, 'pm1_0_atm_b': 59.0, 'p_2_5_um_b': 162.0, 'pm2_5_atm_b': 103.0, 'p_5_0_um_b': 69.0, 'pm10_0_atm_b': 135.0, 'p_10_0_um_b': 14.0, 'p25aqic': 'rgb(241,0,11)', 'pm2.5_aqi': 176, 'pm1_0_cf_1': 88.0, 'p_0_3_um': 15801.0, 'pm2_5_cf_1': 158.0, 'p_0_5_um': 4522.0, 'pm10_0_cf_1': 179.0, 'p_1_0_um': 1117.0, 'pm1_0_atm': 58.0, 'p_2_5_um': 125.0, 'pm2_5_atm': 104.0, 'p_5_0_um': 32.0, 'pm10_0_atm': 118.0, 'p_10_0_um': 10.0, 'pa_latency': 310, 'response': 201, 'response_date': 1601672403, 'latency': 386, 'key1_response': 200, 'key1_response_date': 1601672396, 'key1_count': 17265, 'ts_latency': 620, 'key2_response': 200, 'key2_response_date': 1601672398, 'key2_count': 17269, 'ts_s_latency': 539, 'key1_response_b': 200, 'key1_response_date_b': 1601672399, 'key1_count_b': 17272, 'ts_latency_b': 535, 'key2_response_b': 200, 'key2_response_date_b': 1601672401, 'key2_count_b': 17268, 'ts_s_latency_b': 535, 'wlstate': 'Connected', 'status_0': 2, 'status_1': 2, 'status_2': 2, 'status_3': 2, 'status_4': 2, 'status_5': 2, 'status_6': 2, 'status_7': 0, 'status_8': 2, 'status_9': 2, 'ssid': 'silver-2011'}
'''
data = json.loads(rawContents)

# Enum for what field is what.
class FieldType(Enum):
  TAG = 1  
  VALUE = 2  
  IGNORE = 3 

# Data definition of the fields.
FIELD_CONFIG = {
  'pm2_5_cf_1_b': FieldType.VALUE,
  'loggingrate': FieldType.VALUE,
  'p_10_0_um': FieldType.VALUE,
  'key2_response': FieldType.VALUE,
  'key1_response': FieldType.VALUE,
  'key2_response_date_b': FieldType.VALUE,
  'period': FieldType.VALUE,
  'DateTime': FieldType.VALUE,
  'p_2_5_um': FieldType.VALUE,
  'status_7': FieldType.VALUE,
  'p_0_5_um': FieldType.VALUE,
  'wlstate': FieldType.VALUE,
  'Adc': FieldType.VALUE,
  'pm10_0_atm': FieldType.VALUE,
  'pm2.5_aqi': FieldType.VALUE,
  'ts_s_latency': FieldType.VALUE,
  'p_0_5_um_b': FieldType.VALUE,
  'status_5': FieldType.VALUE,
  'pm1_0_cf_1_b': FieldType.VALUE,
  'latency': FieldType.VALUE,
  'uptime': FieldType.VALUE,
  'pm10_0_cf_1_b': FieldType.VALUE,
  'ssid': FieldType.TAG,
  'key2_response_date': FieldType.VALUE,
  'response_date': FieldType.VALUE,
  'Mem': FieldType.VALUE,
  'current_humidity': FieldType.VALUE,
  'httpsuccess': FieldType.VALUE,
  'lon': FieldType.VALUE,
  'pm10_0_atm_b': FieldType.VALUE,
  'memcs': FieldType.VALUE,
  'pm2_5_atm': FieldType.VALUE,
  'version': FieldType.TAG,
  'status_4': FieldType.VALUE,
  'key1_count': FieldType.VALUE,
  'SensorId': FieldType.TAG,
  'p_5_0_um': FieldType.VALUE,
  'Geo': FieldType.VALUE,
  'key1_count_b': FieldType.VALUE,
  'pa_latency': FieldType.VALUE,
  'pm10_0_cf_1': FieldType.VALUE,
  'httpsends': FieldType.VALUE,
  'p_1_0_um_b': FieldType.VALUE,
  'status_2': FieldType.VALUE,
  'ts_s_latency_b': FieldType.VALUE,
  'pm2_5_atm_b': FieldType.VALUE,
  'pm1_0_atm_b': FieldType.VALUE,
  'pm1_0_cf_1': FieldType.VALUE,
  'pressure': FieldType.VALUE,
  'key1_response_b': FieldType.VALUE,
  'current_dewpoint_f': FieldType.VALUE,
  'status_9': FieldType.VALUE,
  'status_8': FieldType.VALUE,
  'lat': FieldType.TAG,
  'status_6': FieldType.VALUE,
  'key1_response_date_b': FieldType.VALUE,
  'pm1_0_atm': FieldType.VALUE,
  'memfrag': FieldType.VALUE,
  'response': FieldType.VALUE,
  'status_1': FieldType.VALUE,
  'status_0': FieldType.VALUE,
  'hardwarediscovered': FieldType.VALUE,
  'current_temp_f': FieldType.VALUE,
  'p25aqic': FieldType.VALUE,
  'hardwareversion': FieldType.VALUE,
  'pm2.5_aqi_b': FieldType.VALUE,
  'key2_response_b': FieldType.VALUE,
  'key2_count_b': FieldType.VALUE,
  'key2_count': FieldType.VALUE,
  'status_3': FieldType.VALUE,
  'ts_latency_b': FieldType.VALUE,
  'p_2_5_um_b': FieldType.VALUE,
  'p_10_0_um_b': FieldType.VALUE,
  'pm2_5_cf_1': FieldType.VALUE,
  'p_0_3_um': FieldType.VALUE,
  'memfb': FieldType.VALUE,
  'p_5_0_um_b': FieldType.VALUE,
  'place': FieldType.VALUE,
  'key1_response_date': FieldType.VALUE,
  'p_1_0_um': FieldType.VALUE,
  'rssi': FieldType.VALUE,
  'p25aqic_b': FieldType.VALUE,
  'Id': FieldType.TAG,
  'ts_latency': FieldType.VALUE,
  'p_0_3_um_b': FieldType.VALUE
}
  
# Uses pip3 install influx_line_protocol to build a metric
# Build the metric.
metric = Metric("purpleair")

for key in data:
  if key in FIELD_CONFIG:
    config = FIELD_CONFIG[key]
    if config == FieldType.TAG:
      metric.add_tag(key, data[key])
    elif config == FieldType.VALUE:
      metric.add_value(key, data[key])
    else:
      pass
      # IGNORE

print(metric)
