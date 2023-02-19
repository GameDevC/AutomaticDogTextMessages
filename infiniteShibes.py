import requests
from twilio.rest import Client
import time

account_sid = #put in your account sid
auth_token = #put in your auth token

james_Cordon_url = 'https://static.standard.co.uk/s3fs-public/thumbnails/image/2015/05/07/11/jamescorden.jpg?width=990&auto=webp&quality=75&crop=968:645%2Csmart'
shibes_url = 'http://shibe.online/api/shibes'

# Create the Twilio client
client = Client(account_sid, auth_token)

while True:
    # Get a shibe picture from the API
    response = requests.get(shibes_url)

    data = []

    if response.status_code == 200:
        data.append(response.json())
        print(data[0])  #gives the url 
    else:
        print('Failed to get a shibe')

    # This sends the content of your image
    message = client.messages.create(
        media_url=shibes_url, 
        body=#text you want,
        from_=#your given twilio number,
        to=#number you want to send to
    )

    # Print the message SID
    print(message.sid)

    # Pause for 1 minute
    time.sleep(60)