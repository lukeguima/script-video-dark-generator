import os
import yt_dlp
from moviepy.editor import VideoFileClip

def create_background_clip(link, temp_folder, start_background_clip='[0:00]'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(temp_folder, '%(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True)
        filename = ydl.prepare_filename(info_dict)

    start_min, start_sec = map(int, start_background_clip.strip("[]").split(":"))
    start_time = start_min * 60 + start_sec

    # Use 'with' to ensure video file is closed properly
    with VideoFileClip(filename) as video_clip:
        subclip = video_clip.subclip(start_time, video_clip.duration)

        subclip_filename = os.path.join(temp_folder, "background_subclip.mp4")
        subclip.write_videofile(subclip_filename, codec="libx264", preset="ultrafast", fps=30)

    # Return path to the subclip
    return subclip_filename
