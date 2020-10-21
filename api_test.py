import requests
import json

url = "http://127.0.0.1:5000/aadhaar_upload"

apikey = input("Enter API-Key: ")
org_id = input("Enter Org. ID: ")
headers = {"api-key":apikey,
          "org-id":org_id}

aadhaar = input("Enter Aadhaar: ")
share_code = input("Enter Share Code: ")
file = input("Enter File Path: ")

payload = {'aadhaar':aadhaar, 'share_code': share_code, 'file': file}
payload = json.dumps(payload)
print(payload)

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
