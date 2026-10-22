from dotenv import load_dotenv
import os
import requests
import json

#call the API key
load_dotenv()
SAM_API_KEY = os.getenv("SAM_API_KEY")

### API Params ###
url="https://api.sam.gov/opportunities/v2/search"
params={
    "api_key":SAM_API_KEY,
    "limit": 1000,
    "ptype":"o",
    "postedFrom":"09/01/2026",
    "postedTo":"10/21/2026",
    "ncode": ["541715"],
} 

response=requests.get(url, params=params)
data=response.json()
### Write the data to file response.json ###
with open("response.json", "w") as f:
    json.dump(data, f, indent=2)

#Write now we have 58 data for ncode 541715

