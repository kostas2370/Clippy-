def cut_video(video_name,start_time,end_time,clip_names="default"):
	if(len(start_time)!=len(end_time)):
		print("You forgot a time !")
		return False

	conn=sqlite3.connect("db/database.db")
	c=conn.cursor()
	c.execute("SELECT  clips_to_delete_destination FROM settings")
	for row in c.fetchall():
		destination=row[0]
   
	try:
		path=other.get_Destination(0)
		vid=path+"/"+video_name
		for x in range(len(start_time)):
				st=start_time[x]
				et=end_time[x]
				clip=VideoFileClip(vid,fps=30)
				if(clip.duration<st or clip.duration<et):
						print(str(x)+"clip above limit")
				else:
						clip=clip.subclip(st,et)
						if clip_names=="default":
							filename=video_name+" clip "+str(x)+".mp4"
						else:
							filename=clip_names[x]+".mp4"
			   
						c.execute("SELECT channel_name,video_link FROM youtube_clips WHERE file_name = '{}'".format(video_name))
						for row in c.fetchall():
							channel_name=row[0]
							video_link=row[1]   
						c.execute("INSERT INTO cutted_clip(clip_name,full_video_name,publisher,link,time_START,time_END) VALUES(?,?,?,?,?,?)",[filename[0:len(filename)-3],video_name,channel_name,video_link,start_time[x],end_time[x]])
		
						print(filename)
						clip.write_videofile(path+"/"+filename)  
						clip.close()

		other.move_file(vid,destination+"/"+video_name) 
	 
		conn.commit()
		conn.close()
	except:
		print("couldnt find the file name D: ") 
		return  False
