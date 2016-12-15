import os
import pyfttt
import subprocess
import json

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# speedtest-cli only runs from the cli so we'll capture the json output
result, err = subprocess.Popen(["speedtest-cli", "--json"], stdout=subprocess.PIPE).communicate()

if(not err):
  # result will be a list with one item in it. 
  data = json.loads(result.decode('utf-8'))
  # send data to ifttt
  pyfttt.send_event(
    api_key=os.environ.get('IFTTT_KEY'),
    event=os.environ.get('IFTTT_EVENT_NAME'),
    value1=data['download'],
    value2=data['upload'],
    value3=data['server']['name'] # This is the location of where the test was taken
  )
