import other
import datetime
import time
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import undetected_chromedriver as uc
def upload(title,description,file,api=False,thubnail=False):   
    if (api == True): 
        CLIENT_SECRET_FILE = 'db/client_file.json'
        API_NAME = 'youtube'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
        
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        
        upload_date_time = datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'
        
        request_body = {
            'snippet': {
                'categoryI': 19,
                'title': title,
                'description': description,
                'tags': ['gaming', 'twitch', 'compilation']
            },
            'status': {
                'privacyStatus': 'private',
                'publishAt': upload_date_time,
                'selfDeclaredMadeForKids': False, 
            },
            'notifySubscribers': False
        }
        
        mediaFile = MediaFileUpload(file)
        
        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()
        
        if (thubnail!=False):
            service.thumbnails().set(
                videoId=response_upload.get('id'),
                media_body=MediaFileUpload(thubnail)
            ).execute()





    elif (api=="selenium"):
        print("in progress")


    else:     

        p=other.get_Destination(1)
        file=open(p+"/"+title+".txt","w",encoding="utf-8")
        file.write("Title : "+title +"\n")
        file.write("Description : "+"\n"+description+"\n")
        file.write("File Name : "+str(file)+"\n")
        if thubnail != False :
            file.write("thubnail : "+thubnail+"\n")
        file.close()

