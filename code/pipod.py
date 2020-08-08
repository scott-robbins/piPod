import random
import utils 
import time 
import sys 
import os 


def create_user():
	username = raw_input('Enter a username for piPod to speak to you:\n')	
	os.mkdir(os.getcwd()+'/PIPOD')
	open(os.getcwd()+'/PIPOD/username.txt','wb').write(username)
	path_added = False
	while not path_added:
		musicpath = raw_input('Enter the path you would like to use to point to music by default:\n')
		if os.path.isdir(musicpath):
			path_added  = True
			open(os.getcwd()+'/PIPOD/music.txt','wb').write(musicpath)
		else:
			print('[!!] Cannot point PiPod to play music from path: %s because it cannot be found' % musicpath)



def shuffle(uname):
	if os.path.isfile(os.getcwd()+'/PIPOD/music.txt'):
		music_dir = utils.swap(os.getcwd()+'/PIPOD/music.txt',False).pop()
		songs = list(os.listdir(music_dir))
		random.shuffle(songs)
		for song in songs:
			if song != '..':
				ext = song.split('.')[1]
				print song.split('.')
				if ext == 'mp3':
					os.system('mpg123 %s/%s' % (music_dir,song))
				else:
					os.system('aplay %s/%s' % (music_dir,song))
	else:
		utils.speak('Sorry %s, but you have not setup a music folder' % uname)
		exit()


def main():
	if not os.path.isdir(os.getcwd()+'/PIPOD'):
		create_user()
	else:
		username = utils.swap(os.getcwd()+'/PIPOD/username.txt', False).pop()
		os.system('paplay service-login.oga')
		utils.speak('Hello there %s. Your Pi Pod is starting.' % username)
		# Now start shuffling music (default mode)
		shuffle(username)


if __name__ == '__main__':
	main()