from openai import OpenAI
import os
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

messages = [
    {"role": "system", "content": 'You are an assistant specialized in summarizing video content. You will be given the title and text of the video, and even if the content is in any language, you must summarize it in Spanish. Provide ONLY the summarized text, nothing else.'},
]

transcripted_folder = 'transcripted'
summarized_folder = 'summarized'

if not os.path.exists(summarized_folder):
    os.makedirs(summarized_folder)

for file_name in os.listdir(transcripted_folder):
    if file_name.endswith('.txt'):
        file_path = os.path.join(transcripted_folder, file_name)
        
        # Leer el contenido del archivo
        with open(file_path, 'r', encoding='utf-8') as file:
            user_input = file.read()
        
        messages.append({"role": "user", "content": user_input})
        
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        
        # Save the summarized text in a file named after the original file in the summarized folder
        summarized_file_path = os.path.join(summarized_folder, file_name)
        with open(summarized_file_path, 'w', encoding='utf-8') as file:
            file.write(completion.choices[0].message.content)
        
        print(f'Summary saved to {summarized_file_path}')
        
        # Clear the user message for the next iteration
        messages.pop()

# Ejecuta el codigo para subir los resumenes al airtable
subprocess.run(["python", "post_summary.py"])