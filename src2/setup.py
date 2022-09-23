import os
import sqlite3
import getpass
import requests
import other
def db_making(clips_destination,video_destination,clips_to_delete_destination,music_destination,always_destination,prebuild_photos):

                conn=sqlite3.connect("db/database.db")
                c=conn.cursor()
                c.execute("""create table IF NOT EXISTS settings (clips_destination TEXT,video_destination TEXT,clips_to_delete_destination TEXT,music_destination TEXT,always_destination TEXT,prebuild_photos TEXT)""")
              
              
                c.execute(f"INSERT INTO settings VALUES('{clips_destination}','{video_destination}','{clips_to_delete_destination}','{music_destination}','{always_destination}','{prebuild_photos}')")
                c.execute("create table IF NOT EXISTS youtube_clips(video_id INTEGER PRIMARY KEY,title TEXT,views INTEGER,duration REAL,rating REAL,video_link TEXT,upload_date TEXT,download_date TEXT,channel_id TEXT,channel_url TEXT,avaliability TEXT,filesize INTEGER,file_name TEXT,channel_name TEXT,clip_type TEXT,game TEXT)")
                c.execute("create table IF NOT EXISTS music(music_id INTEGER PRIMARY KEY,song_name TEXT,file_name TEXT,link TEXT)")
                c.execute("create table IF NOT EXISTS cutted_clip(clip_id INTEGER PRIMARY KEY,clip_name TEXT,full_video_name TEXT,publisher TEXT,link TEXT,time_START INTEGER,time_END INTEGER)")
                c.execute("create table IF NOT EXISTS videos(video_id INTEGER PRIMARY KEY,video_name TEXT,serie TEXT,thubnail_path TEXT,Tags TEXT,url TEXT,description TEXT,views INTEGER,filename_path TEXT)")

                conn.commit()
                conn.close()
def mk_dirs(default):
               



                try:
                                os.mkdir(f'{default}\\automation')
                                default2=default+"automation/"
                                os.mkdir(f'{default2}\\always_destination')
                                os.mkdir(f'{default2}\\clips')
                                os.mkdir(f'{default2}\\clips/edited')
                                os.mkdir(f'{default2}\\video')
                                os.mkdir(f'{default2}\\used_clips')
                                os.mkdir(f'{default2}\\music_clips')
                                os.mkdir(f'{default2}\\prebuild_photos')
                                return default2
                except:
                                print("The files already exist !")

                                return False
def setup(mode="default"):
                x=getpass.getuser()
                
                default=f'C:/users/{x}/Videos/'
                if(mode=="default"):
                                p=mk_dirs(default)
                                
                                if(p==False):
                                                return (False)
                elif (mode=="newdest"):
                                save_files=input("Give me path :")
                                p=mk_dirs(save_files)
                                if(p==False):
                                                return (False)
                else:
                           print("This mode doesnt exist !")

                try:
                    db_making((p+"clips"),(p+"video"),(p+"used_clips"),(p+"music_clips"),(p+"always_destination"),(p+"prebuild_photos"))
                except:
                    print("Something went wrong")
                download_prebuild_photos()
def download_prebuild_photos():
    twitch_image="https://www.freepnglogos.com/uploads/twitch-app-logo-png-3.png"
    youtube_image="https://www.freepnglogos.com/uploads/youtube-logo-icon-transparent---32.png"
    x=other.get_Destination(5)
    response_ytb=requests.get(youtube_image)
    response_twitch=requests.get(twitch_image)
    ytb_file=open(x+"/youtube.png","wb")
    twitch_file=open(x+"/twitch.png","wb")
    ytb_file.write(response_ytb.content)
    ytb_file.close()
    twitch_file.write(response_twitch.content)
    twitch_file.close()