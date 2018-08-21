# Rpi SpeedTest
This is a simple script to get data from speedtest.net and send it to Zapier

## Required packages
See requirments.txt for versions

```
python-dotenv
speedtest-cli
```
## Setup instructions

Install required packages

`pip install -r requirements.txt`

create `.env` file in the rpi-speedtest directory with the following values

```
ZAPIER_ENDPOINT=[your zapier endpoint url]
```

## Run

Call from command line:
`python ./run.py`
