#for windows users: install ImageMagic & uncomment lines 2 & 3
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.10-Q16-HDRI\magick.exe"})

from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, concatenate_audioclips
import os

fr = 24
#fr = input("Enter Desired Framerate: ")
output_name = "final_video.mp4"
#output_name = input("Enter Desired Output Name:")

video_files = []

#for each video in folder
for i in os.listdir():
    if i.endswith(".mp4"):
        video_files.append(i)
        
#create 'clip' for each video
for i, clip in enumerate(video_files):
    video_files[i] = VideoFileClip(clip)

print(video_files)
    
#endscreen
endtext = input("Enter Endscreen Text, leave blank and hit enter to skip: ")
if endtext != "":
    video_files.append(TextClip(endtext, fontsize = 50, color = 'white').set_duration(5))

#combine video clips
combined_clip = concatenate_videoclips(video_files, method="compose")

#title
title = input("Enter Title Screen Text, leave blank and hit enter to skip: ")
if title != "":
    txt_clip = TextClip(title,fontsize=70,color='white')
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    combined_clip = CompositeVideoClip([combined_clip, txt_clip])

#audio
audio_files = []

for i in os.listdir():
    if i.endswith(".mp3") or i.endswith(".wav"):
        audio_files.append(i)

print(audio_files)

for i, clip in enumerate(audio_files):
    audio_files[i] = AudioFileClip(clip)

#ToDo Concatenate audio tracks into audioclip
combined_audio = concatenate_audioclips(audio_files)

#Set Duration of audioclip
audioclip = combined_audio.set_duration(combined_clip.duration)
final_clip = combined_clip.set_audio(audioclip)

#render
print("Composition successful. Rendering!")
final_clip.write_videofile(output_name, fps=fr, logger=None)
