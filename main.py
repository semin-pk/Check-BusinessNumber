# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends, Request
import urllib.parse
import requests
from fastapi.responses import JSONResponse
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()
SERVICE_KEY = 'IRIyY0JPZa84xQT1zGNnN3lnQ3zu7iuMgnOfdJUmdN6VgDzCCYP8PKzQTm09LRuFKs7mdN3bf9xBVPACVqD2xw=='
BASE_URL = f'http://api.odcloud.kr/api/nts-businessman/v1/status?'
class b_no(BaseModel):
    'b_no'
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 오리진 허용, 필요에 따라 변경 가능
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # 허용할 메서드 목록
    allow_headers=["*"],  # 모든 헤더 허용, 필요에 따라 변경 가능
)
@app.post('/store/status')
async def status(request: Request):
    data = await request.json()
    query = data.get('b_no', '')
    req_body = {
      "b_no": [
        query
      ]
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    Params = {
        'serviceKey': SERVICE_KEY,
        'return_type' : 'JSON'
    }
    result = {
        'b_status' : ''
    }
    req_body_json = json.dumps(req_body)
    response = requests.post(BASE_URL, data = req_body_json, headers = headers, params = urllib.parse.urlencode(Params))
    responseData = response.json()
    check = responseData['data'][0]['tax_type']
    if check == '국세청에 등록되지 않은 사업자등록번호입니다.':
        result['b_status'] = '0'
    else:
        result['b_status'] = '1'

    return JSONResponse(result)


    