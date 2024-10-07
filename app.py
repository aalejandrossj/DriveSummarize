# Este codigo inicia una serie de programas que tratan sobre descargar videos de una carpeta de Google Drive, convertirlos a mp3 y transcribirlos a texto, para luego ser 
# analizados por un modelo de chatgpt, y guardar las respuestas en un airtable mediante una accion post.

import subprocess
import os
import gdown
from moviepy.editor import VideoFileClip
import shutil

# Función para descargar todos los archivos de una carpeta de Google Drive
def download_folder_from_drive(url):
    # Extraer el ID de la carpeta de la URL de Google Drive
    folder_id = url.split('/')[-1]
    download_url = f'https://drive.google.com/drive/folders/{folder_id}'
    gdown.download_folder(download_url, output='VideoResumer', quiet=False, use_cookies=True)

# Función para extraer todos los archivos de video de VideoResumer y moverlos a videostomp3
def extract_videos_to_folder():
    source_folder = 'VideoResumer'
    destination_folder = 'videostomp3'
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.mp4'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(source_path, destination_path)
                print(f'Movido {source_path} a {destination_path}')

# Función para convertir archivos MP4 a MP3
def convert_mp4_to_mp3():
    folder_path = 'videostomp3'
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp4'):
            mp4_path = os.path.join(folder_path, file_name)
            mp3_path = os.path.join(folder_path, file_name.replace('.mp4', '.mp3'))
            video = VideoFileClip(mp4_path)
            video.audio.write_audiofile(mp3_path)
            video.close()
            print(f'Convertido {mp4_path} a {mp3_path}')
            os.remove(mp4_path)  # Eliminar el archivo MP4 después de la conversión
            print(f'Eliminado {mp4_path}')

def main():
    url = input('Pon la URL de la carpeta de Google Drive: ')
    
    # Descargar todos los archivos de la carpeta de Google Drive
    download_folder_from_drive(url)
    
    # Extraer todos los archivos de video y moverlos a videostomp3
    extract_videos_to_folder()
    
    # Convertir archivos MP4 a MP3 y eliminar los archivos MP4
    convert_mp4_to_mp3()
    
    # Ejecutar el script de transcripción después de completar el proceso
    shutil.rmtree("VideoResumer")
    subprocess.run(["python", "transcript.py"])

if __name__ == "__main__":
    main()