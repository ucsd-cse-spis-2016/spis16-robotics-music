import omxplayer
import os
from omxplayer import OMXPlayer
from time import sleep


def list_files(mypath):
    file_list =[]
    for f in os.listdir(mypath):
        if os.path.isfile(os.path.join(mypath, f)):
            file_list.append(f)

    return file_list


path = "/media/USB DISK/"
os.chdir(path)
file_list = list_files('./')

try:

    for f in file_list:
        player = OMXPlayer(f)
        dur = player.duration()
        if dur == None:
            break
        print "Playing .....", f
        print "Duration ", dur

        player.play()
    
        sleep(20)
        player.pause()
        player.quit()
        
except KeyboardInterrupt:
    exit()
