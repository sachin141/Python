import os
import glob


#os is used for dir nevigation
#glob is used for finding particular file type

for item in os.listdir("."):
	if os.path.isfile(item):
		print(item + " is file")
	elif os.path.isdir(item):
		print(item + " is directory")
	else:
		print(item + " unable to specify")

		
print(glob.glob('*.py'))
