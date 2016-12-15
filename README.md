# Rpi SpeedTest
This is a simple script to get data from speedtest.net and send it to IFTTT

## Required packages
See requirments.txt for versions

```
python-dotenv
speedtest-cli
pyfttt
```
## Setup instructions

Install required packages

`pip install -r requirements.txt`

create `.env` file in the rpi-speedtest directory with the following values

```
IFTTT_KEY=[your api key from IFTTT]
IFTTT_EVENT_NAME=[The name of your configured event]
```

## Run

Call from command line:
`python ./run.py`
