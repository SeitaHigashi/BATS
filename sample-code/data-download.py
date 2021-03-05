import pybitflyer
import pandas as pd
import json

api = pybitflyer.API()

board = api.board()
print(json.dumps(board, sort_keys=True, indent=4))
print(board['mid_price'])
bids = json.dumps(board['bids'])
df = pd.read_json(bids)
df.to_csv('bids.csv', encoding='utf-8')