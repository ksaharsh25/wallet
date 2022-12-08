import requests
import json

URL="https://www.sms4india.com/api/v1/sendCampaign"

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId,textMessage ):
    req_params={
    'apikey':apiKey,
    'secret':secretKey,
    'useType':useType,
    'phone':phoneNo,
    'message':textMessage,
    'senderid':senderId,

    }
    return requests.post(reqUrl,req_params)

