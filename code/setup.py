import sys
import os 


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

	dependencies = ['mpg123']
	# Install Needed packages through apt-get
	# TODO: Need to add a script for building gespeak instead of espeak because it worked better
	# in practice on the raspberry pi but had a more complicated build process
	apt_gets(dependencies)


if __name__ == '__main__':
	main()