import utils
import sys
import os 


def change_startup_mode(new_mode):
	valid_modes = ['shuffle', 'upload', 'install', 'debug']
	if new_mode not in valid_modes:
		print '[!!] Unrecognized mode provided. Settings are unchanged.'
	content = ''
	for line in utils.swap('/etc/rc.local',False):
		if 'pipod.py' in line.split(' '):
			fcn = line.split('python ')[1].split(' ')[0]
			opt = line.split(fcn)[1].split(' ')[1]
			add = utils.arr2str(line.split(opt)[1].split(' ')[:])
			line = 'python %s -%s' % (fcn, opt) + '\n'

			print '- changing current start-up mode from %s fcn to %s' % (opt, new_mode)
		content += new_line

	print 'New RC File:'
	print content

def apt_gets(libraries):
	"""
	APT_GETS - Install packages that use apt-get to get the right software on the
	RaspberryPi before running the rest of the software.
	"""
	tmp = '#!/bin/bash\nyes | sudo apt-get update\nyes | sudo apt-get upgrade\n'
	for library in libraries:
		if len(library) >1:
			tmp += 'yes | sudo apt-get %s\n' % library
	tmp +='#EOF\n'
	open('setup.sh', 'wb').write(tmp)
	os.system('sudo bash setup.sh')
	os.remove('setup.sh')


def main():
	if '-install' in sys.argv:
		dependencies = ['mpg123']
		# Install Needed packages through apt-get
		# TODO: Need to add a script for building gespeak instead of espeak because it worked better
		# in practice on the raspberry pi but had a more complicated build process
		apt_gets(dependencies)

	# TODO: Add options to switch mode, which should change the section of 
	# /etc/rc.local where pipod.py is called.
	if '-change' in sys.argv and len(sys.argv) > 2:
		mode = sys.argv[2]
		change_startup_mode(mode)


if __name__ == '__main__':
	main()