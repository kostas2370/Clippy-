# CliPpy

game mode : https://youtu.be/dGtgDQZ7U_E






Clippy is a program to make twitch compilation videos automated
First of all open the settings file and insert your cliend id(twitch) secret client id (twithc) and the location of your selenium exe file
Modules you need to have downloaded :

Modules we will use :
  1.	Os
  2.	Sqlite3
  3.	Pytube
  4.	Youtube api
  5.	Moviepy
  6.	Twitch api
  7.	Request
  8.	Beutifulsoup
  9.	getpass
  10.	glob
  11.	time
  12.	shutil
  13.	random
  14. psutil	
  15. json
  16. urllib
  17. selenium
  18. twitch
  19. Google
  20. undetected_chromedriver
  21. moviepy
  
Programs you need installed :

  1. ffmpeg : https://www.ffmpeg.org/
  2. selenium for the google chrome version you use : https://www.selenium.dev/
  
Basic fuctions :
  
  1. setup.setup(mode) : mode="default" or mode="newdest" 
    if you put newdest : you set the destinations for the folders 
  
  2. youtube_funcs.download_youtube(link,type="mp4") 
  3. youtube_funcs.download_playlist(link) #playlist link
  
  4. twitch_funcs.download_twitch(link="",game="",creator="") #The only mandatory is link
  5. twitch_funcs.get_clips(amt=10,game_name="",streamer_id="")#Mandatory is game_name or Streamer_id (Streamer id is still on process)

  6. other.set_intro(path,filename)
  7. other.set_outro(path,filename)
  
  8. edit.cut_video(video_name,start_time,end_time,clip_names="default") #start time and end_time are lists with times in seconds etc start_time=[10,20,30] end_time=[15,25,35]
  9. edit.vidMake_mode_compilation(amt,title,music=False,music_selection="default",intro=False,outro=False,serie="Random stream compilation",game=False)
  
  10.real_upload.upload(title,description,file,api=False,thubnail=False) #to make this work you need to download the json file from youtube_api team and replace it
 
  11.video(get_clips=True,title="default",amt=20,music=False,music_selection="default",game=False,intro=True,outro=True,serie="Random Compilation",api=False))
  
 
 
If you want to upload a video through youtube api you will need to place the json file from youtube api with the client ids you need in folder src/db.  




  For questions,contact me in kostas2372@gmail.com
