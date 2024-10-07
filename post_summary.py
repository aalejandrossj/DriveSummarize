import requests
import os
import subprocess

def post_summary(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            summary_file = os.path.join(folder_path, file_name)
            title = file_name.replace('.txt', '')
            url = ''  # Empty URL

            # Read the summarized content
            with open(summary_file, 'r', encoding='utf-8') as file:
                summary_content = file.read()

            # Make a POST request
            response = requests.post(
                '',
                data={
                    'summary': summary_content,
                    'title': title,
                    'url': url
                }
            )

            print(f'POST request sent for {title}. Response status code: {response.status_code}')

if __name__ == "__main__":
    summarized_folder = 'summarized'
    post_summary(summarized_folder)
    
    # Ejecuta el archivo clear.py para borrar todo lo descargado
    subprocess.run(["python", "clear.py"])