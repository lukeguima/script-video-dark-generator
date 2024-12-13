import os
from src.utils.clean_temp_files import clean_temp_files
from src.utils.create_folder import create_folder
from src.generator.cortes.create_audio_clip import create_audio_clip
from src.generator.cortes.create_background_clip import create_background_clip
from src.generator.cortes.compile_video import compile_video

def video_generator():
    # Folders default
    temp_folder = 'temp'
    output_folder = 'output'
    
    # Inputs do Cortes
    link_audio_youtube = 'https://www.youtube.com/watch?v=AW36rKr2yxs'
    start_audio_clip = '[0:40]'
    final_audio_clip = '[1:49]'

    link_image_youtube = 'https://www.youtube.com/watch?v=Tp6HQCb70yM'
    start_background_clip = '[0:00]'

    video_name = 'verdadeira_transformacao'

    create_folder(temp_folder)
    create_folder(output_folder)
    clean_temp_files(temp_folder)

    start_min, start_sec = map(int, start_audio_clip.strip("[]").split(":"))
    end_min, end_sec = map(int, final_audio_clip.strip("[]").split(":"))
    start_time = start_min * 60 + start_sec
    end_time = end_min * 60 + end_sec

    audio_path = create_audio_clip(link_audio_youtube, temp_folder, start_time, end_time)
    print(f"Áudio salvo em: {audio_path}")

    background_path = create_background_clip(link_image_youtube, temp_folder, start_background_clip)
    print(f"Vídeo de fundo salvo em: {background_path}")

    output_path = os.path.join(output_folder, f"{video_name}.mp4")
    compile_video(audio_path, background_path, output_path)
    print(f"Vídeo final salvo em: {output_path}")
    clean_temp_files(temp_folder)
