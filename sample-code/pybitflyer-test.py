import pybitflyer
import json

api = pybitflyer.API()

board = api.board()
print(board['mid_price'])