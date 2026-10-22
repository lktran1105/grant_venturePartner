import pandas as pd
import json 

### Put into DataFrame ###
with open("response.json", "r") as f:
    data=json.load(f)

records=data["opportunitiesData"]
grant_data=pd.json_normalize(records) #processed Grant Data from json into dataframe

### New Dataframe with selected columns ###
chosen_cols = ["noticeId", "title", "naicsCode", "solicitationNumber", "postedDate", "responseDeadLine", "uiLink"]
grant_data_small=grant_data[chosen_cols].copy()

### Convert date columns to datetime format ###
grant_data_small["postedDate"] = pd.to_datetime(grant_data_small["postedDate"], format="ISO8601", utc=True)
grant_data_small["responseDeadLine"] = pd.to_datetime(grant_data_small["responseDeadLine"], format="ISO8601", utc=True)

grant_data_small.to_csv("data/processed/grant_data_102126.csv", index=False)

'''
1. Check to see if there is any N/A - good practice
'''



