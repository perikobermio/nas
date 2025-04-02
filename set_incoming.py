import json
import sys
import shutil
import os

try:
    data = json.loads(sys.argv[1])

    for type, types  in data.items():
        for item in types:
            path = item['path'].replace('/d/NAS/', '/var/www/index/storage/') #containerran patha
            os.makedirs(os.path.dirname(path), exist_ok=True)
            shutil.move(f"/var/www/index/storage/Incoming/{item['original_file']}", path)

    print('dena OK')
            
except Exception as e:
    print(f"Errore bat egon da: {e}")
