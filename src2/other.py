import os
import sqlite3
import shutil
import datetime
import random
import time
def check_file(file_name):

        final_path=f'{get_Destination(0)}\\{file_name}.mp4'
        files_to_delete_path=f'{get_Destination(2)}\\{file_name}.mp4'
        if (os.path.exists(final_path)==True):
            return True;
                  
        else :
            return os.path.exists(files_to_delete_path)

def move_file(path_filename,where_filename):
        shutil.move(path_filename,where_filename)

def get_down_history(what,x):
    conn=sqlite3.connect("db/database.db")
    c=conn.cursor()
    if(x=="*"):
             try:
                    c.execute(f"SELECT {what} FROM youtube_clips")

                    for row in c.fetchall():
                            print (f'{row}\n')
                            
             except:
                    print ("Syntax error")
                    return False

    else: 
              try:
                    entolh="SELECT {} FROM youtube_clips WHERE {} "
                    c.execute(entolh.format(what,x))  
                    for row in c.fetchall():
                             print (f'{row}\n')
              except:
                    print ("Syntax error")
                    return False

def get_Destination(x):
           conn=sqlite3.connect("db/database.db")
           c=conn.cursor()
           c.execute("SELECT * FROM settings ")
           for row in c.fetchall():
               destination=row[x]
           conn.close()
           return  destination
def get_video_files(game=False):
    x=get_Destination(0)
    lista=os.listdir(x)
   
    try:
        lista.remove("edited")
    except:
        pass
    for x in lista :
        if ".mp4" not in x:
            lista.remove(x)

    if (game==False):
        pass
    else:
        conn=sqlite3.connect("db/database.db")
        c=conn.cursor()
        c.execute(f"SELECT file_name FROM youtube_clips WHERE game='{game}'") 
        new_list=[]
        for row in c.fetchall():
            if row[0] in lista:
                if row[0] not in new_list:
                    new_list.append(row[0])
        return new_list

def get_video_files_creator(streamer=False):
    x=get_Destination(0)
    lista=os.listdir(x)
   
    try:
        lista.remove("edited")
    except:
        pass
    for x in lista :
        if ".mp4" not in x:
            lista.remove(x)

    if (streamer==False):
        pass
    else:
        conn=sqlite3.connect("db/database.db")
        c=conn.cursor()
        c.execute(f"SELECT file_name FROM youtube_clips WHERE channel_name='{streamer}'") 
        new_list=[]
        for row in c.fetchall():
            if row[0] in lista:
                if row[0] not in new_list:
                    new_list.append(row[0])
        return new_list

def snuffle(lista,amt=5):
    lista_pointer=0
    used_positions=[]
    new_list=[]
    
        


    if(len(lista)<=amt):
        amt=len(lista)
    new=amt*["1"]     
    for i in range(amt):
        positons=random.randint(0,len(lista)-1)
        if positons not in used_positions:
            new[i]=(lista[positons])
            used_positions.append(positons)
        else:
            while positons in used_positions :
                positons=random.randint(0,len(lista)-1)
                if(positons not in  used_positions):
                    new[i]=(lista[positons])
                    used_positions.append(positons)
                    break
    for x in new:
            if x == '':
                    new.remove('')
    return new


def check_if_db(link):
    conn=sqlite3.connect("db/database.db")
    c=conn.cursor()
    c.execute(f"SELECT * FROM youtube_clips WHERE video_link ='{link}'")
    x=False
    if len(c.fetchall())>=1:
        x=  True    
   
    conn.close()    
    return x
def set_intro(path,filename):
    destination_to_go=get_Destination(4)
    try:
        x=f'{path}\\{filename}'
        destination=f'{get_Destination(4)}\\intro.mp4 '    
        os.system(f"ffmpeg -i \"{x}\" -vf \"scale=1920:1080\" \"{destination}\"")
    except:
        print("We can't find this video")
        return False

def set_outro(path,filename):

    try:
        x=f'{path}\\{filename}'
        destination=f'{get_Destination(4)}\\outro.mp4 '          
        os.system(f"ffmpeg -i \"{x}\" -vf \"scale=1920:1080\" \"{destination}\"")
    except:
        print("We can't find this video")
        return False


def get_creator(file_name):
    conn=sqlite3.connect("db/database.db")
    c=conn.cursor()
    c.execute(f"SELECT channel_name FROM youtube_clips WHERE file_name= '{file_name}'")
    lista=c.fetchall()
    creator=""
    if (len(lista)>0):
        
        for x in lista:      
            creator=x[0]
    else:
        c.execute(f"SELECT publisher FROM cutted_clip WHERE clip_name= '{file_name[0:len(file_name)-3]}'")  
        lista=c.fetchall()
        for x in lista:
            creator=x[0]

    if len(creator)>0: 
        j= creator
    else:
        j='no info'
        
    conn.commit()
    conn.close()
    return j
def convert_time(times):
    x=time.gmtime(times)
    res = str(time.strftime("%M:%S",x))
    return res

def get_previous_day(day=1):
    previous_date = datetime.datetime.today() - datetime.timedelta(days=day)
    return previous_date.isoformat() + "Z"
def cut_clip_link(link):
    slug=link.rsplit('/', 1)[-1]
    return slug

def check_lang(lista,lang="en"):
    new_list=[]
    amt=0
    for i in lista:
        amt=amt+1
        if i["language"]==lang and check_if_db(i["url"])==False:
            new_list.append(i)
            
        
        elif(amt>=len(lista)):
            break
        else:
            continue
    return new_list