from fastapi import FastAPI, Depends, Request
import urllib.parse
import requests
from datetime import datetime, timedelta
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
import json

app = FastAPI()
SERVICE_KEY = 'IRIyY0JPZa84xQT1zGNnN3lnQ3zu7iuMgnOfdJUmdN6VgDzCCYP8PKzQTm09LRuFKs7mdN3bf9xBVPACVqD2xw=='
BASE_URL = f'http://api.odcloud.kr/api/nts-businessman/v1/status?'

@app.get('/')
async def status():
    req_body = {
        "b_no": ["6708700853"]
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    Params = {
        'serviceKey': SERVICE_KEY,
        'return_Type' : 'JSON'
    }
    req_body_json = json.dumps(req_body)
    response = requests.post(BASE_URL, data = req_body_json, headers = headers, params = urllib.parse.urlencode(Params))
    response = response.json()
    result = response['status_code']
    return JSONResponse(result)


    