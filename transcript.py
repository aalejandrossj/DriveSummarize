import os
import whisper
import subprocess

# Función para transcribir archivos MP3 en la carpeta donde estan los videos en mp3 usando Whisper
def transcribe_mp3_files_with_whisper(folder_path):
    model = whisper.load_model("base")
    transcripted_folder = 'transcripted'
    
    if not os.path.exists(transcripted_folder):
        os.makedirs(transcripted_folder)
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp3'):
            mp3_path = os.path.join(folder_path, file_name)
            result = model.transcribe(mp3_path)
            transcription = result['text']
            text_file_path = os.path.join(transcripted_folder, file_name.replace('.mp3', '.txt'))
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(transcription)
            print(f'Transcrito {mp3_path} a {text_file_path}')

# Función para sacar todos los archivos de la carpeta de videos en mp3
def transcribe_multiple_folders(folders):
    for folder in folders:
        if os.path.exists(folder):
            transcribe_mp3_files_with_whisper(folder)
        else:
            print(f'La carpeta {folder} no existe')

def main():
    folders = ['videostomp3']
    transcribe_multiple_folders(folders)
    # Ejecutar el script de resumen después de completar el proceso
    subprocess.run(["python", "summarize.py"])

if __name__ == "__main__":
    main()