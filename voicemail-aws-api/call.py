#! /usr/bin/env python3
from ringcentral import SDK
from dotenv import load_dotenv
import os

# Configurations
load_dotenv() # Load .env file

RECIPIENT = '4086766571'

RINGCENTRAL_CLIENTID = os.getenv("CLIENT_ID")
RINGCENTRAL_CLIENTSECRET = os.getenv("CLIENT_SECRET")
RINGCENTRAL_SERVER = 'https://platform.devtest.ringcentral.com'

RINGCENTRAL_USERNAME = os.getenv("RING_USER")
RINGCENTRAL_PASSWORD = os.getenv("RING_PW")
RINGCENTRAL_EXTENSION = os.getenv("RING_EXT")

rcsdk = SDK( RINGCENTRAL_CLIENTID, RINGCENTRAL_CLIENTSECRET, RINGCENTRAL_SERVER)
platform = rcsdk.platform()
platform.login(RINGCENTRAL_USERNAME, RINGCENTRAL_EXTENSION, RINGCENTRAL_PASSWORD)

resp = platform.post('/restapi/v1.0/account/~/extension/~/ring-out',
              {
                  'from' : { 'phoneNumber': RINGCENTRAL_USERNAME },
                  'to'   : {'phoneNumber': RECIPIENT},
                  'playPrompt' : False
              })
print(f'Call placed. Call status: {resp.json().status.callStatus}')
