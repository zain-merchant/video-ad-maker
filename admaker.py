#for windows users: install ImageMagic & uncomment lines 2 & 3
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.10-Q16-HDRI\magick.exe"})

from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, concatenate_audioclips, AudioClip, CompositeAudioClip
import os

fr = input("Enter Desired Framerate, leave blank and hit enter for default(24): ")
if fr == "":
    fr = 24
else: fr = int(fr)
    
output_name = input("Enter Desired Output Name, leave blank and hit enter for default(final_video.mp4): ")
if output_name == "":
    output_name = "final_video.mp4"

video_files = []

#for each video in folder
for i in os.listdir():
    if i.endswith(".mp4"):
        video_files.append(i)
        
#create 'clip' for each video
for i, clip in enumerate(video_files):
    video_files[i] = VideoFileClip(clip)

print("Number of video files loaded: " + str(len(video_files)))

#title frontend
title = input("Enter Title Screen Text, leave blank and hit enter to skip: ")

#endscreen
endtext = input("Enter Endscreen Text, leave blank and hit enter to skip: ")
if endtext != "":
    video_files.append(TextClip(endtext, fontsize = 50, color = 'white').set_duration(5))

#combine video clips
combined_clip = concatenate_videoclips(video_files, method="compose")

#title backend
if title != "":
    txt_clip = TextClip(title,fontsize=70,color='white')
    txt_clip = txt_clip.set_pos('bottom').set_duration(5)
    video = CompositeVideoClip([combined_clip, txt_clip])
else:
    video = combined_clip
    
#audio
audio_files = []

for i in os.listdir():
    if i.endswith(".mp3") or i.endswith(".wav"):
        audio_files.append(i)

print("Audio files loaded are: " + str(audio_files))

for i, clip in enumerate(audio_files):
    audio_files[i] = AudioFileClip(clip)

#ToDo Concatenate audio tracks into audioclip
combined_audio = concatenate_audioclips(audio_files)

#Set Duration of audioclip
background_audio = combined_audio.set_duration(video.duration)

#combine videos' audio and audio track
video_audio = video.audio
print(background_audio)
print(video_audio)
final_audio = CompositeAudioClip([background_audio, video_audio])
final_clip = video.set_audio(final_audio)

#render
print("Composition successful. Rendering!")
final_clip.write_videofile(output_name, fps=fr, logger=None)
