import requests
import json


def getHolybotsRatio(steamkey):
    id='76561198029848726'
    data = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key='+steamkey+'&steamid='+id)
    data = json.loads(data.text)

    kills = 0
    deaths = 0

    for item in data['playerstats']['stats']:
        if item['name']=='total_kills':
            kills = item['value']
        if item['name']=='total_deaths':
            deaths = item['value']



    kd = kills/deaths
    meme = ''

    if kd > 1:
        meme='adequate'
    if kd == 1:
        meme = 'funny'
    if kd < 1:
        meme = 'totally lame and inexcusable'

    kdlaugh= 'Holybot\'s ' + meme + ' kill death ratio is ' + str(kd)+'.'

    return kdlaugh


if __name__ == '__main__':
    steamkey='changeme'
    print(getHolybotsRatio(steamkey))