import pybitflyer
import json

api = pybitflyer.API()

status = api.getboardstate()
print(json.dumps(status, sort_keys=True, indent=4))