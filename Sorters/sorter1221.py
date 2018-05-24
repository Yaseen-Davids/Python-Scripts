import os
import shutil

filename =  r'c:/Users/Eku/Desktop/Mixed/Images/'

if os.path.exists(filename):
 print "Yes, Image folder exists"
else:
 print "No, it doesnot exists "
 print "Creating a new directory for Images"
 os.makedirs(filename)

filename1 = r'c:/Users/Eku/Desktop/Mixed/'

os.chdir(filename1)

for file in os.listdir(filename1):
 if file.endswith(".JPG"):
  #print file
  shutil.move(file,filename)

filename = r'c:/Users/Eku/Desktop/Mixed/Songs/'

if os.path.exists(filename):
 print "Yes, songs folder exists"
else:
 print "Songs folder doesnot exists"
 print "Creating new directory for Songs"
 os.makedirs(filename)


filename1 = r'c:/Users/Eku/Desktop/Mixed'

os.chdir(filename1)

for file in os.listdir(filename1):
 if file.endswith(".mp3"):
  #print file
  shutil.move(file,filename)
