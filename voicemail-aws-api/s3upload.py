#! /usr/bin/env python3
import boto3
import os

# Configuration
def upload_vm(vm_files, vm_bucket, access_key, secret_access_key):
	s3 = boto3.client('s3',
		aws_access_key_id = access_key,
		aws_secret_access_key = secret_access_key)

	# Upload new voicemails if not uploaded yet
	for vmfile in vm_files:
		try:
			with open(vmfile, "rb") as file:
				s3.upload_fileobj(file, vm_bucket, os.path.basename(vmfile))
				print(os.path.basename(vmfile) + " was added!")
		except EnvironmentError:
			print("Error! Unable to open " + vmfile)
