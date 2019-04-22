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
    creds = pickle.load(open('token.pickle', 'rb'))
    service = build('gmail', 'v1', credentials=creds)

    response = service.users().messages().list(userId='me', labelIds='INBOX').execute()
    cnt = 0
    for msg in response["messages"]:
        cnt = cnt + 1
        print(cnt, msg)
         
        message = service.users().messages().get(userId='me', id=msg["id"]).execute()

        subject = ""
        for header in message["payload"]["headers"]:
            if header["name"] == 'Subject':
                subject = header['value']
        
        snippet = message["snippet"]
            
        print("主旨：", subject)    
        if subject.startswith("預約取書到館通知"):
            snippet = message["snippet"]
            snippet = snippet[snippet.index("保留日期")+5:]
            print(snippet)

if __name__ == '__main__':
    main()