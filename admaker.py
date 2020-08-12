from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip
import os

video_files = []

for i in os.listdir():
	if i.endswith(".mp4"):
		video_files.append(i)

for i, clip in enumerate(video_files):
	video_files[i] = VideoFileClip(clip)

video_files.append(TextClip("Get this guitar now.", fontsize = 50, color = 'white').set_duration(2))
combined_clip = concatenate_videoclips(video_files, method="compose")

audioclip = AudioFileClip("Advertising.mp3").set_duration(combined_clip.duration)
final_clip = combined_clip.set_audio(audioclip)

final_clip.write_videofile("final_video.mp4", fps=24, logger=None)