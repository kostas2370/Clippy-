import datetime
import sqlite3
import pytube
import other
import edit
import random
import os
import glob
def get_youtube_video_info(link):
           """
            Args: a ling from youtube video (str)
            Returns: a list with video information (list)
            exception: unavaliable link 
           """

           try:
               video=pytube.YouTube(link)
           except:
               print("This link doesnt work !") 
               return False
           title=video.title
           views=video.views
           duration=video.length
           rating=video.rating
           video_link=link
           upload_date=video.publish_date
           download_date="NULL" #6
           channel_id=video.channel_id
           channel_url=video.channel_url
           avaliabillity=video.check_availability()
           estimated_filesize="null"
           channel_name=video.author
           lista=[title,views,duration,rating,video_link,upload_date,download_date,channel_id,channel_url,avaliabillity,estimated_filesize]
           return lista

def download_youtube(link,typex="mp4"):
           """
            Args: a ling from youtube video (str) and the type of download (mp4/mp3)
            Returns: the downloaded video(str)
            exception: unavaliable link 
            db: it inserts the video information in youtube_clips / if type == mp3 it will insert in music clips too
           """


           destination=other.get_Destination(0) 
           conn=sqlite3.connect("db/database.db") 
           c=conn.cursor()    
           if(link[0:24]!="https://www.youtube.com/"):
               print("Unavaliable link") 
               return False
           try: 
                video=pytube.YouTube(link)
                stream=video.streams.get_highest_resolution()
                if other.check_file(video.title)==True:
                     conn.close()
                     return "This video exists" 
                else:
                     if other.check_if_db(link)==True:
                             conn.close()
                             return "This video exists"      
                     else:
                             if(typex=="mp3"):
                                name="song"+str(random.randint(0,1000))
                                stream.download(destination,name+".mp4")
                             else:
                                stream.download(destination)
           except:
                print("internet error")
                return False
           update_db=get_youtube_video_info(link)
           update_db[6]=datetime.date.today()
          
           video_position=destination+"/"+update_db[0]+".mp4"
           update_db[9]="download"
           try:
                update_db[10]=os.path.getsize(video_position)/1000000
           except:
                update_db[10]=0 
           list_of_files = glob.glob(other.get_Destination(0)+"/*.mp4")
           video_name=max(list_of_files,key=os.path.getctime)
           
           update_db.append(os.path.basename(video_name))
           channel_name=video.author
           update_db.append(channel_name)
           update_db.append("youtube")
           c.execute("INSERT INTO youtube_clips (title,views,duration,rating,video_link,upload_date,download_date,channel_id,channel_url,avaliability,filesize,file_name,channel_name,clip_type) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",update_db)

           if typex=="mp3"  :
                edit.convert_to_mp3(name,True) 
                c.execute("INSERT INTO music(song_name,file_name,link) VALUES (?,?,?)",[update_db[0],(name+".mp3"),link])
           conn.commit()
           conn.close()

           return video.title+" Downlpaded succesfully"
           
def download_playlist(link):
    """

            Args: a link from youtube playlist (str)
            Returns: the downloaded video (str)
            exception: unavaliable link 
           
    """

    playlist=pytube.Playlist(link)
    
    for x in playlist:
        try:
                print(download_youtube(x))
        except:
                print("unavaliable link ")  
