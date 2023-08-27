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

def getHolybotsAcc(steamkey):
    id='76561198029848726'
    data = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key='+steamkey+'&steamid='+id)
    data = json.loads(data.text)

    shotshit = 0
    shotsfired = 0

    for item in data['playerstats']['stats']:
        if item['name']=='total_shots_hit':
            shotshit = item['value']
        if item['name']=='total_shots_fired':
            shotsfired = item['value']

    accuracy = 100 - ((shotsfired - shotshit) / shotsfired * 100)
    accComment = f'Holybot\'s accuracy is {int(accuracy)}%'

    return accComment

def getHolybotsMaps(steamkey):
    id='76561198029848726'
    data = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key='+steamkey+'&steamid='+id)
    data = json.loads(data.text)

    maps = {}

    for item in data['playerstats']['stats']:
        if item['name']=='total_wins_map_cs_assault':
            print(item)
            maps.update(item)
            print(maps)
        if item['name']=='total_wins_map_cs_italy':
            maps.update(item)
            print(maps)

    print(f'this is maps {maps}')




if __name__ == '__main__':
    steamkey = "F29EB3D121C129EE524D9E858DC9FE4A"
    print(getHolybotsRatio(steamkey))
    print(getHolybotsAcc(steamkey))
    print(getHolybotsMaps(steamkey))
