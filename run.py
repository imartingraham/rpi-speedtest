import os
import subprocess
import json
import requests
import datetime
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Get WiFi connection
cmd = "iw dev wlan0 link | grep SSID | awk '{print $2}'"
wifi_name = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
# speedtest-cli only runs from the cli so we'll capture the json output
result, err = subprocess.Popen(["speedtest-cli", "--json"], stdout=subprocess.PIPE).communicate()

if(not err):
  # result will be a list with one item in it. 
  data = json.loads(result.decode('utf-8'))
  zapier_data = {
    'date': str(datetime.datetime.utcnow()),
    'wifi_name': wifi_name.rstrip('\n'),
    'location': data['server']['name'],
    'upload': data['upload'],
    'download': data['download']
  }
  r = requests.post(os.environ.get('ZAPIER_ENDPOINT'), data=zapier_data)
