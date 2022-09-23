import sqlite3
from moviepy.editor import *
import os
import random
import other

def get_video_title(serie):
	conn=sqlite3.connect("db/database.db")
	c=conn.cursor()
	c.execute("SELECT MAX(video_id) FROM videos WHERE serie = '{}'".format(serie))
	rows=c.fetchall()
	for row in rows:

		if row[0]==None:
		
			title=serie+" #"+str(1)
		
		else:
			
			title=serie+" #"+str(row[0]+1)
			break
	conn.close()
	return title

def get_video_description(clips,music=False,intro=True):
#Source:
#	type=[time.start : time.end]: Name of clip  : Link\n	
#	type=[time.start : time.end]: Name of clip2 : Link\n
#	type=[time.start : time.end]: Name of clip3 : Link\n
	conn=sqlite3.connect("db/database.db")
	c=conn.cursor()
	text="Source : \n"
	if (music != False):
		c.execute(f"SELECT link FROM music WHERE file_name = \"{os.path.basename(music)}\"")
		for row in c.fetchall():
			musicp=row[0]
		text=text+"music : "+musicp+"\n"
	if intro==True:
		x=other.get_Destination(4)
		intro_path=x+"/intro.mp4"
		intr=VideoFileClip(intro_path)
		strt_time=intr.duration
		
	else:
		strt_time=0
	for clip in clips:
		print(("SELECT duration,title,video_link FROM youtube_clips WHERE file_name='{}'".format(clip)))
		c.execute(f"SELECT duration,title,video_link FROM youtube_clips WHERE file_name=\"{clip}\"")
		for row in c.fetchall():
			p="[{}] : {} : Link : {} \n".format(str(other.convert_time(strt_time)),row[1],row[2])
			text=text+p
			strt_time=strt_time+int(row[0])
	return(text)



