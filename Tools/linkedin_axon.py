import requests
import os
from dotenv import load_dotenv

load_dotenv()

url_listconv = "https://svc.sandbox.anon.com/actions/linkedin/listConversations"

headers1 = {
    "X-Anon-App-User-Id": os.getenv('X-Anon-App-User-Id'),
    "Authorization": f"Bearer {os.getenv('Anon_API_key')}"
}
print(headers1)

response1 = requests.request("GET", url_listconv, headers=headers1)

print(response1.text)

# url_sendmsg = "https://svc.sandbox.anon.com/actions/linkedin/sendMessage"

# message = "Hello Cyril this is a test"

# payload = {
#     "message": message,
#     "conversationId": conversationId
# }
# headers = {
#     "X-Anon-App-User-Id": os.getenv("X-Anon-App-User-Id"),
#     "Authorization": f"Bearer {os.getenv("Anon_API_key")}",
#     "Content-Type": "application/json"
# }

# response = requests.request("POST", url_sendmsg, json=payload, headers=headers)

# print(response.text)