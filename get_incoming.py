import os
import sys
import json
import re

data                = {}
path                = '/d/NAS/'
data['Serijek']     = []
data['Pelikulek']   = []

def getMetadata(f, regex):
    s = re.search(regex, f)
    return str(s.group(1)) if s else ''

def getTitle(input):
    output = re.sub(r"[0-9]+\D[0-9]+", '', input)
    output = re.sub(r"\s+-\s+", '', output)
    output = re.sub(r"HDTV.*", '', output)
    output = re.sub(r"[_\+]", ' ', output)
    output = re.sub(r"\[[^\]]+\]", '', output)
    output = re.sub(r"\.[^$]+$", '', output)
    output = re.sub(r'@\w+', '', output)
    return str(output.strip()) 

def transform(f):
    meta                    = {}
    meta['original_file']   = f
    meta['extension']       = getMetadata(f, r"\.(\w+)$")
    meta['season']          = getMetadata(f, r"(\d{1,2})\D\d{1,3}").zfill(2)
    meta['chapter']         = getMetadata(f, r"\d{1,2}\D(\d{1,3})").zfill(2)
    meta['title']           = getTitle(f)

    if meta['season'] == '00':
        meta['path']         = f"{path}Pelikulek/{meta['title']}/{meta['title']}.{meta['extension']}"
        data['Pelikulek'].append(meta)
    else:
        meta['path']         = f"{path}Serijek/{meta['title']}/Season {meta['season']}/{meta['title']} - s{meta['season']}e{meta['chapter']}.{meta['extension']}"
        data['Serijek'].append(meta)

def get(path):
    try:
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)) and f.lower().endswith(('.mp4', '.mkv', '.avi')):
                transform(f)
                
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":

    incoming_path = '/d/NAS/Incoming'
    if len(sys.argv) > 1:
        incoming_path = sys.argv[1]

    get(incoming_path)
    
    print(json.dumps(data))
