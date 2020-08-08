import time 
import os 

def swap(filename, destroy):
	data = []
	for line in open(filename, 'rb').readlines():
		data.append(line.replace('\n', ''))
	if destroy:
		os.remove(filename)
	return data

def arr2str(strarr):
	content = ''
	for element in strarr:
		content += element + ' '
	return content

def arr2lines(strarr):
	content = ''
	for element in strarr:
		content += element + '\n'
	return content


def speak(lines):
	os.system('spd-say "%s"' % lines)