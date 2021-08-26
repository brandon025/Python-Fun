#! /usr/bin/env python3
from ringcentral import SDK
import mimetypes
import datetime
import os
from dotenv import load_dotenv

# Configurations
load_dotenv() # Load .env file
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
RING_USER = os.getenv("RING_USER")
RING_EXT = os.getenv("RING_EXT")
RING_PW = os.getenv("RING_PW")

# Initiate RingCentral
sdk = SDK( CLIENT_ID, CLIENT_SECRET, "https://platform.devtest.ringcentral.com" )
platform = sdk.platform()
platform.login( RING_USER, RING_EXT, RING_PW )

# Get messages of type VoiceMail
response = platform.get('/restapi/v1.0/account/~/extension/~/message-store',
    {
        'messageType': ['VoiceMail']
    })

# Get records
for record in response.json().records:
    if record.attachments != None:
        for attachment in record.attachments:
            # Set filename
            if attachment.type == "AudioRecording":
                fileExt = mimetypes.guess_extension(attachment.contentType)
                fileName = datetime.datetime.strptime(record.creationTime, "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%Y-%m-%d_%H-%M-%S_VM') + fileExt
                # Save file
                try:
                    res = platform.get(attachment.uri)
                    with open(fileName, "wb") as file:
                        file.write(res.body())
                        print(fileName + " was added!")
                except ApiException as err:
                    print(err.message)
