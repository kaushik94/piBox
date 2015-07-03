import os
import subprocess

def createBox():
	directory = "../Box"
	if not os.path.isdir(directory):
		os.makedirs(directory)

def main():
	createBox()
	subprocess.call('python cronJob.py &', shell=True)