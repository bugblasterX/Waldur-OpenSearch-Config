import requests
import json
import math
from datetime import datetime, timedelta
import os

#API KEY
api_key = os.environ.get("API_KEY")

#Here we get the timestamps for the requests. Get the timestamp for an hour ago. 
hour_ago = datetime.now() - timedelta(hours = 1)
to_timestamp = int(datetime.timestamp(datetime.now()))
from_timestamp = int(datetime.timestamp(hour_ago))

def fetch_events(url):
    headers = {
        'Authorization': f'Token {api_key}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        raise Exception(f"HTTP request failed: {response.status_code} {response.reason}")


def send_events(events, url):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url,data=json.dumps(events), headers=headers)
    if response.status_code != 200:
        raise Exception(f"HTTP request failed: {response.status_code} {response.reason}")

url = os.environ.get("API_URL")
logstash_url = 'http://localhost:5044'
limit = 100
all_events = []

# Initial fetch to geth the event count
initial_url = f"{url}?page=1&page_size={limit}&created_from={from_timestamp}&created_to={to_timestamp}"
initial_response = fetch_events(initial_url)

if 'X-Result-Count' in initial_response.headers:
    result_count = int(initial_response.headers['X-Result-Count'])
else:
    raise Exception(f"Failed to retreive result count. X-Result-Count not found in response headers.")
#Check if we have any results, whether to proceed or not.
if result_count == 0:
    exit()
num_pages = math.ceil(result_count / limit)

for page in range(1, num_pages + 1):
    url_with_next_page = f"{url}?page={page}&page_size={limit}&created_from={from_timestamp}&created_to={to_timestamp}"
    new_events = fetch_events(url_with_next_page)
    send_events(new_events.json(), logstash_url)


