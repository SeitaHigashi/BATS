import pybitflyer
import pandas as pd
import json

api = pybitflyer.API()

executions = api.executions(count=100000)
# print(json.dumps(executions, sort_keys=True, indent=4))
bids = json.dumps(executions)
df = pd.read_json(bids)
df.to_csv('executions.csv', encoding='utf-8')