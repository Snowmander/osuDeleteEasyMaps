import json
import requests
import os
import shutil
from time import sleep
DesiredDifficulty = 4.0

dictionary = set()
last_date_before = "0"
last_date = "2005-11-01 01:01:01"

try:
    api_token = os.environ['osuAPI']
except:
    # huh, you're not me
    api_token = input("osu!API Key?\n")
    DesiredDifficulty = float(input("Minimum Difficulty?\n"))
    directory = input("Songs Folder Path?\n")

def AddMaps():
    global last_date, last_date_before
    response = requests.get("https://osu.ppy.sh/api/get_beatmaps?since={}&k={}&m=0".format(last_date, api_token))
    if response.status_code == 200:
            req = json.loads(response.content.decode('utf-8'))
            last_date_before = last_date
            for map in req:
                if float(map['difficultyrating']) >= DesiredDifficulty:
                    dictionary.add(int(map['beatmapset_id']))
                last_date = map['approved_date']

            print(dictionary)
            print(last_date_before)

def WriteList():
    f = open('workfile', 'w')
    f.seek(0)
    f.write('\n'.join(str(e) for e in dictionary))
    f.close()


while(last_date_before != last_date):
    AddMaps()

WriteList()
print(last_date)