import os
import shutil
import time

music_path = r'c:/Users/INFIN8/Music'
pictures_path = r'c:/Users/INFIN8/Pictures'
download_path = r'c:/Users/INFIN8/Downloads'

print("Do you want to sort pictures or music ?")
myChoice = input()

if myChoice == 'pictures' or 'Pictures' or 'Pics' or 'pics':
    if os.path.exists(pictures_path):
        print('File exists. pics')
    else:
        print("File doesn't exist. Creating file.")
        os.makedirs(pictures_path)
        os.chdir(download_path)
        for file in os.listdir(download_path):
            if file.endswith('.png'):
                shutil.move(file,pictures_path)

elif myChoice == 'music' or 'Music':
    if os.path.exists(music_path):
        print('File exists. mus')
    else:
        print("File doesn't exist.")
        os.makedirs(music_path)
    os.chdir(download_path)
    for file in os.listdir(download_path):
        if file.endswith(".mp3"):
            shutil.move(file,music_path)

else:
    print("try again")

time.sleep(10)
