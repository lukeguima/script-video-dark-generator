import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
import time

def compile_video(audio_path, background_path, output_path):
    if not os.path.exists(audio_path) or not os.path.exists(background_path):
        raise ValueError("O áudio ou o vídeo de fundo não foram encontrados.")

    start_time = time.time()

    background_clip = VideoFileClip(background_path)
    audio_clip = AudioFileClip(audio_path)

    background_clip = background_clip.subclip(0, audio_clip.duration)

    background_clip = background_clip.resize((1080, 1920))
    background_clip = background_clip.set_position("center")

    background_clip = background_clip.set_audio(audio_clip)

    background_clip.write_videofile(
        output_path,
        preset="ultrafast",
        fps=30
    )

    background_clip.close()
    audio_clip.close()

    end_time = time.time()
    print(f"Tempo total de criação do vídeo: {(end_time - start_time) / 60:.2f} minutos")
