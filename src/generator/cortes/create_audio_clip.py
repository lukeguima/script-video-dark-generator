import os
import yt_dlp
from moviepy.editor import AudioFileClip

def create_audio_clip(link_video_youtube, temp_folder, start_time, end_time):
    sanitized_filename = "audio_download.mp3"
    safe_audio_path = os.path.join(temp_folder, sanitized_filename)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(temp_folder, 'audio_download.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link_video_youtube])

    if not os.path.exists(safe_audio_path):
        raise FileNotFoundError(f"Arquivo não encontrado após o download: {safe_audio_path}")

    audio_clip = AudioFileClip(safe_audio_path)
    audio_duration = audio_clip.duration

    if start_time >= audio_duration:
        audio_clip.close()
        raise ValueError(f"O tempo de início ({start_time}s) é maior ou igual à duração do áudio ({audio_duration}s).")
    if end_time > audio_duration:
        print(f"Ajustando o tempo de fim ({end_time}s) para a duração máxima do áudio ({audio_duration}s).")
        end_time = audio_duration

    cut_audio = audio_clip.subclip(start_time, end_time)
    cut_audio_path = os.path.join(temp_folder, "corte_audio.mp3")
    cut_audio.write_audiofile(cut_audio_path, codec="mp3")
    
    cut_audio.close()
    audio_clip.close()

    return cut_audio_path
