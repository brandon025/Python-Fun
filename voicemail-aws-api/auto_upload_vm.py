#! /usr/bin/env python3
from s3upload import upload_vm
from voicemail import fetch_vm
from dotenv import load_dotenv # storing secrets
import os
import tempfile # Secure temporary directories

# Configuration
load_dotenv()
RING_CLIENT_ID = os.getenv("RING_CLIENT_ID")
RING_CLIENT_SECRET = os.getenv("RING_CLIENT_SECRET")
RING_USER = os.getenv("RING_USER")
RING_EXT = os.getenv("RING_EXT")
RING_PW = os.getenv("RING_PW")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

vm_bucket = "ringcentral-s3-voicemail"

# Main function
if __name__ == "__main__":
    # Create temporary directory
    temp_dir = tempfile.TemporaryDirectory()
    vm_files= fetch_vm(temp_dir, RING_CLIENT_ID, RING_CLIENT_SECRET, RING_USER, RING_EXT, RING_PW)
    if vm_files:
        upload_vm(vm_files, vm_bucket, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)
    else:
        print("Everything is up to date already...")
    temp_dir.cleanup()
