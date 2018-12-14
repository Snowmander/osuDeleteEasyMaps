import json
import requests
import os
import shutil
from time import sleep
DesiredDifficulty = 4
directory = "C:\osuBeatmapTest"

try:
    api_token = os.environ['osuAPI']
except:
    # huh, you're not me
    api_token = input("osu!API Key?\n")
    DesiredDifficulty = float(input("Minimum Difficulty?\n"))
    directory = input("Songs folder path?")




def FindDiffs(set):
    response = requests.get("https://osu.ppy.sh/api/get_beatmaps?s={}&k={}&m=0&a=0".format(set, api_token))
    if response.status_code == 200:
            req = json.loads(response.content.decode('utf-8'))
            res = []
            for map in req:
                if float(map['difficultyrating']) >= DesiredDifficulty:
                    res.append(map['beatmap_id'])
            return res
    else:
        return None

# list beatmaps in the directory
Bm_in_Dir = [(int(name[:name.index(' ')]), name) for name in os.listdir(directory) if os.path.join(directory, name)]
print(Bm_in_Dir)


# delete
for number, name in Bm_in_Dir:
    diffs = []
    ctn = True
    while ctn:
        diffs = FindDiffs(number)
        if diffs != None:
            ctn = False
        else:
            # rate limited?
            sleep(60)
    if len(diffs) == 0:
        shutil.rmtree(os.path.join(directory, name))


