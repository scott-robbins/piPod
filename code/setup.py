import os 



def apt_gets(libraries):
	tmp = '#!/bin/bash\nyes | sudo apt-get update\nyes | sudo apt-get upgrade\n'
	for library in libraries:
		tmp += 'yes | sudo apt-get %s\n' % library
	tmp +='#EOF\n'
	open('setup.sh', 'wb').write(tmp)
	os.system('sudo bash setup.sh')
	os.remove('setup.sh')


def main():
	dependencies = ['espeak', 'mpg123']
	# Install Needed packages through apt-get
	apt_gets(dependencies)
