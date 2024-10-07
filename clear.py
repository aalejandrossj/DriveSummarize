import shutil
import os

folders_to_delete = ['summarized', 'transcripted', 'videostomp3', 'VideoResumer']

for folder in folders_to_delete:
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f'Carpeta {folder} eliminada.')
    else:
        print(f'La carpeta {folder} no existe.')