import os
import glob


for item in os.listdir("."):
	if os.path.isfile(item):
		print(item + " is file")
	elif os.path.isdir(item):
		print(item + " is directory")
	else:
		print(item + " unable to specify")

		
print(glob.glob('*.py'))
