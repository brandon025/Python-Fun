#! /usr/bin/env python3
from ringcentral import SDK
import mimetypes
from datetime import datetime
import os

def fetch_vm(temp_dir, RING_CLIENT_ID, RING_CLIENT_SECRET, RING_USER, RING_EXT, RING_PW):
    # Initiate RingCentral
    sdk = SDK(RING_CLIENT_ID, RING_CLIENT_SECRET, "https://platform.devtest.ringcentral.com" )
    platform = sdk.platform()
    platform.login(RING_USER, RING_EXT, RING_PW)

    # Get messages of type VoiceMail
    response = platform.get('/restapi/v1.0/account/~/extension/~/message-store',
        {
            'messageType': ['VoiceMail']
        })

    # Get last voicemail date that was parsed
    try:
        runfile = open("lastvm.txt","r+")
        lastvmdate = datetime.strptime(runfile.readline(), "%Y-%m-%d %H:%M:%S")
        runfile.seek(0)
        runfile.truncate()
    except EnvironmentError:
        runfile = open("lastvm.txt","w+")
        lastvmdate = datetime(1900, 1, 1, 0, 0, 0) # Set old date

    # Get voicemail files
    vmfiles = []
    latestvm = lastvmdate
    for record in response.json().records:
        filedate = datetime.strptime(record.creationTime, "%Y-%m-%dT%H:%M:%S.%fZ")
        if record.attachments != None and filedate > lastvmdate:
            for attachment in record.attachments:
                # Set filename
                if attachment.type == "AudioRecording":
                    ext = mimetypes.guess_extension(attachment.contentType)
                    filepath = temp_dir.name + "/" + filedate.strftime('%Y-%m-%d_%H-%M-%S_VM') + ext
                    vmfiles.append(filepath)
                    # Save file
                    try:
                        res = platform.get(attachment.uri)
                        with open(filepath, "wb") as file:
                            file.write(res.body())
                            # Set latest voicemail date
                            if latestvm < filedate:
                                latestvm = filedate
                    except ApiException as err:
                        print(err.message)
    # Write and cleanup lastrun file
    runfile.write(str(latestvm))
    runfile.close()
    return vmfiles
