# -*- coding: utf-8 -*-

import requests, ssl
from http.client import HTTPSConnection
import json

url = "wxh5.nplusgroup.net/luckdrawtest/gdty/Exam/randQuerstion.json"

ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
conn = HTTPSConnection(host=url, context=ctx)
# s = requests.Session()


token = {"authToken ": "b3NvMzcwVEgxQnZ4bjZMeG1sNVRVWi1HVDRqND1fPS0xPV89LTE1MzE5MDQzMjU="}
body = {"questionId": "1",
        "userOperationId": "1",
        "rightFlag": "1",
        }
# s.headers.update(token)
response = requests.post("https://wxh5.nplusgroup.net/luckdrawtest/gdty/Exam/randQuerstion.json",
                         data=body,
                         headers={"authToken ": "b3NvMzcwVEgxQnZ4bjZMeG1sNVRVWi1HVDRqND1fPS0xPV89LTE1MzE5MDQzMjU="})

# 返回信息
print(response.text)
# 返回响应头
print(response.status_code)
