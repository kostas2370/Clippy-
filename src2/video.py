import other
import youtube_funcs
import edit
import setup
import os
import glob
import upload
import time
import real_upload
import twitch_funcs
def video(get_clips=True,title="default",amt=2,music=False,music_selection="default",game=False,intro=True,outro=True,serie="Random Compilation",api=False,mode="game",streamers="",days=1):
		streamer=""
		if (get_clips ==True): 
			if (mode=="streamer"):
				if len(streamers)==0:
					return "You need to put streamer"
				else:
					streamer=twitch_funcs.get_streamer_id(streamer_name=streamers)
			elif(mode=="game"):
				if game==False :
					return "you need to put game"
			else:
				return "invalid mode"

			try:	
				P=(twitch_funcs.get_clips(game_name=game,amt=amt,mode=mode,streamer_id=streamer,started_at=days))
				print(P)
			except:
				print("anavaliable game")
				return False
		try:
			x=edit.vidMake_mode_compilation(amt,title,music=music,music_selection=music_selection,intro=intro,outro=outro,serie=serie,game=game,mode=mode,streamer=streamers)
		except:
			print ("Cant")
			return False

		real_upload.upload(x[0],x[1],x[2],api)

def test():
	setup.setup()
	video(game="League of Legends",amt=3,serie="LoL",get_clips=True,mode="game",days=1,intro=False,outro=False)

