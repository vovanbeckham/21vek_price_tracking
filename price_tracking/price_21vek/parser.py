import requests
from bs4 import BeautifulSoup
import json


"""
retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"],
)

adapter = HTTPAdapter(max_retries=retry_strategy)
"""

# response = requests.get('https://www.21vek.by/mobile/', timeout=3)
url_site_category = []
url_list = []
url_cat = []



def pars_json():
    with open("data_test/electronics/electronics.json") as file:
        json_string = file.read()
        parsed_json0 = json.loads(json_string)
#       print(parsed_json0)
    return parsed_json0

for js in parsed_json0:
    print(js["name"])

#print(parsed_json0[1]["data"])
