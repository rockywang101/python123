'''
Created on 2019年3月3日

@author: rocky
'''
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
import json
import base64

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
#         for label in labels:
#             print(label['name'])
            
#     url = "https://www.googleapis.com/gmail/v1/users/me/messages"
#     r = requests.get(url)


#     response = service.users().messages().list(userId='me', labelIds='INBOX').execute()
#     cnt = 0
#     for msg in response["messages"]:
#         cnt = cnt + 1
#         print(cnt, msg)
#         
#         message = service.users().messages().get(userId='me', id=msg["id"]).execute()
#         for header in message["payload"]["headers"]:
#             if header["name"] == 'Subject':
#                 subject = header['value']
#                 if subject.startswith("預約取書到館通知"):
#                     print(subject)
#          
#         if cnt >= 100:
#             break;
        
        message = service.users().messages().get(userId='me', id="1693ae87e9dd5944").execute()
        for header in message["payload"]["headers"]:
            if header["name"] == 'Subject':
                subject = header['value']
                print(subject)
        
        snippet = message["snippet"]
        snippet = snippet[snippet.index("保留日期")+5:]
        print(snippet)
        
        # real html content
        print("process parts")
        for part in message["payload"]["parts"]:
            data = part["body"]["data"]
            print(data)    
            mm = base64.urlsafe_b64decode(data.encode('ASCII'))
            print(mm)
    
#         message = service.users().messages().get(userId='me', id="1693ae87e9dd5944", format='raw').execute()
#         mm = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
#         print(mm)

if __name__ == '__main__':
    main()