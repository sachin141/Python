import os


f = open("demofile2.txt", "w")

for count in range(1,50):
	f.write(str(count)+ "\n")

f.close()


f=open("demofile2.txt", "a")

for count in range(50,100):
	f.write(str(count)+"\n")

f.close()

f=open("demofile2.txt", "r")

for line in f.readlines():
	print(line)

f.close()

#renaming file
os.rename("demofile2.txt", "sachin.txt")

#delete file
#os.delete("sachin.txt")


