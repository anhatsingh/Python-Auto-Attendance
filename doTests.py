from output_logger import logging as logs
from sheets_api_v3 import googleAPI

log = logs()
api = googleAPI("1p4sZB2-usDCfTuqypvrXVgW5zyMKlzq0N-9dBQ2JRJE", log)

api.connectToGoogle()
api.getCoulumnToAddTo()
