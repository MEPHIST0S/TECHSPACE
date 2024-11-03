import os
import re

directory = './templates/'

pattern = re.compile(r'(src|href)="(img|css|js)/([^"]+\.(jpg|png|webp|css|js))"')

def replace_paths_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    def replace_match(match):
        path_type = match.group(1)
        folder = match.group(2)
        filename = match.group(3)
        return f'{path_type}="{{{{ url_for(\'static\', filename=\'{folder}/{filename}\') }}}}"'

    new_content = pattern.sub(replace_match, content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(new_content)

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        file_path = os.path.join(directory, filename)
        print(f"Processing file: {file_path}")
        replace_paths_in_file(file_path)

print("Done!")