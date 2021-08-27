# Objective
Automate the process of uploading new voicemails from RingCentral into Amazon S3 Bucket through AWS API.

# Background
Ringcentral has a retention policy on voicemails and will be deleted after X amount of days. As per our legal department, its a requirement to preserve voicemails for at least 5 years. These voicemails must be handled securely throughout the whole process. 

# Overview
The script will utilize a text file to determine when the voicemail was created and then uploaded. Only new voicemails will be uploaded to reduce API usage. The dotenv module will store all secrets including usernames, passwords, API secrets, etc. Also, the tempfile module is used to securely store the voicemail data in a temporary directory which is then cleaned out at the end of the script execution. 

For the purpose of this project, we will be opening the S3 buckets and objects to the public for downloading. In production, we will only provide access that is required and not anymore (IE: Legal team only will have read access to the files). 

# Detailed Design
![voicemail-aws (2)](https://user-images.githubusercontent.com/14297774/131064772-48db2be0-df2e-45e2-953d-ac0a02c2570a.png)
## Use Case
The following demonstrates how a user will setup and use this script:
- User will clone this repositorary into a folder or download contents into a folder
- User installs dependencies
  - boto3
  - python-dotenv
  - ringcentral
- User grants run permissions to the scripts (IE: chmod +x auto_upload_vm.py)
- User creates a ".env" file where the script will be located with the following configurations (Add details in quotes ""):

>RING_CLIENT_ID = "<RingCentral Client ID>"
>
>RING_CLIENT_SECRET = ""
>
>RING_USER = ""
>
>RING_PW = ""
>
>RING_EXT = ""
>
>AWS_ACCESS_KEY = ''
>
>AWS_SECRET_ACCESS_KEY = ''

- User runs the script "auto_upload_vm.py"
- BONUS: Run this script once a day at 8:00am (Unix/Linux)
>crontab.e
>
>0 8 * * * \<absolute path\>
  
## Datapoints Captured
* API keys, secrets, passwords, and user information which is securely stored inside your running enviornment (not hardcoded)
* RingCentral messages and voicemails
* S3 buckets and objects

# Alternative Designs
I was going to tempoarily store voicemails in /tmp/ folder. However, this folder is easily accessible by any user and is not secured. I decided to not parse the AWS bucket for a list of files to determine what voicemails weren't uploaded to it yet. This method can be costly on the API as the bucket grows. 
  
# Testing plan
Unit testing was done on a lab environment. Any new updates would first be tested in lab before pushing onto production. 
  
In the future, we could create continuous integration to automate testing to ensure that our code builds and passes all requirements. 

# Security Considerations
- API secrets, user information, and passwords are securely stored in the running environment
  - Used dotenv module to load config file into the environment
- Dependencies
  - Used the latest modules
- File handling
  - Downloaded voicemails are stored inside a temp directory using tempfile module. The directory and all of its files are deleted after the code is finished executing
-Vulnerability scans
  - Github integrates "Dependabot" to scan for vulnerabilities in my dependencies.
  
In the future, we can integrate vulnerability testing and scans on the servers that we host this on.

# Privacy Considerations
This script should consider locking down the AWS API permissions more granularly.
