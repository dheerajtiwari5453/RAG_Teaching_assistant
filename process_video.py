# converts the videos to mp3
import os
import subprocess

files = os.listdir("videos")
#print(files)
for file in files:
    #print(file)
    tutorial_num = file.split("Lec-")[1].split("_")[0]
    title = file.split("_ ", 1)[1].rsplit(".mp4", 1)[0]
    print(tutorial_num, title)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audio/{tutorial_num}_{title}.mp3"])