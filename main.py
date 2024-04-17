# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends, Request
import urllib.parse
import requests
from datetime import datetime, timedelta
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
import json

app = FastAPI()
SERVICE_KEY = 'IRIyY0JPZa84xQT1zGNnN3lnQ3zu7iuMgnOfdJUmdN6VgDzCCYP8PKzQTm09LRuFKs7mdN3bf9xBVPACVqD2xw=='
BASE_URL = f'http://api.odcloud.kr/api/nts-businessman/v1/validate?'

@app.get('/')
async def status():
    req_body = {
        "businesses": [
          {
            "b_no": "2208202160",
            "start_dt": "20020531",
            "corp_no": "1146220020839",
            "p_nm": "김기남"

            
          }
        ]
    }
    #req_body = requests.get(uri)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    Params = {
        'serviceKey': SERVICE_KEY,
        'return_type' : 'JSON'
    }
    req_body_json = json.dumps(req_body)
    response = requests.post(BASE_URL, data = req_body_json, headers = headers, params = urllib.parse.urlencode(Params))
    response = response.json()
    return JSONResponse(response)


    