import requests

url = "https://gatewayapi.com/rest/mtsms"
api_token = "YOUR_API_TOKEN"
sender_id = "YOUR_SENDER_ID"
message = "Hello, world!"
recipients = ["1234567890", "0987654321"]

headers = {
    "Content-Type": "application/json",
    "X-Gateway-APIKey": api_token
}


response = requests.post(url, headers=headers, json=data)
