

import requests
YOUR_RAPIDAPI_HOST = "maytapi-whatsapp.p.rapidapi.com"
YOUR_RAPIDAPI_KEY = "<YOUR_RAPIDAPI_KEY>"
YOUR_PHONE_ID = "<YOUR_MAYTAPI_PHONE_ID>"
QUARANTINE_MONITORED_PHONE = "<YOUR_DESTINATION_NUMBER>"

url = "https://maytapi-whatsapp.p.rapidapi.com/" + YOUR_PHONE_ID + "/sendMessage"
broadcast_message = "REMINDER: Please send your self captured picture every one hour, for the next 12 hours. Make sure that you enable location tagging & capture time on your camera setting so that we can verify your quarantine location. Stay safe and stay indoors. Thank You."
payload = "{ "to_number": " "  + QUARANTINE_MONITORED_PHONE + "","type":"text","message":"" + broadcast_message + ""}"
headers = {
    'x-rapidapi-host': YOUR_RAPIDAPI_HOST,
    'x-rapidapi-key': YOUR_RAPIDAPI_KEY,
    'content-type': "application/json",
    'accept': "application/json"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)