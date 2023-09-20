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
        if 'total_wins_map_' in item['name']:
            maps[item['name'].split('_')[-1]] = item['value']


    mapsComment = f'Holybot wins the most on the map {(max(maps, key=maps.get))}.'

    return mapsComment

def getUserStats(steamkey, discid):
    steamdict = {'207391826527780865': {'id': '76561198029848726', 'name': 'holybot'},
                 '121853574056640516': {'id': '76561197961452726', 'name': 'holkan'},
                 '529461008025124864': {'id': '76561197962906391', 'name': 'slain'},
                 '207180137802891264': {'id': '76561197961451238', 'name': 'santa'}}

    try:
        id = steamdict[str(discid)]['id']
        name = steamdict[str(discid)]['name']
        print(id)
        data = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key='+steamkey+'&steamid='+id)
        print(data.status_code)
        data = json.loads(data.text)

        shotshit = 0
        shotsfired = 0

        kills = 0
        deaths = 0

        knife = 0

        headshot = 0

        for item in data['playerstats']['stats']:
            if item['name']=='total_shots_hit':
                shotshit = item['value']
            if item['name']=='total_shots_fired':
                shotsfired = item['value']
            if item['name']=='total_kills':
                kills = item['value']
            if item['name']=='total_deaths':
                deaths = item['value']
            if item['name']=='total_kills_knife':
                knife = item['value']
            if item['name']=='total_kills_headshot':
                headshot = item['value']
        hspercent = 100 - ((kills - headshot) / kills * 100)

        accuracy = 100 - ((shotsfired - shotshit) / shotsfired * 100)

        kd = kills / deaths

        msgstats = f'{name}\'s accuracy: {int(accuracy)}%\nkd ratio: {round(kd, 2)}\nknife kills: {knife}\nheadshots: {int(hspercent)}%'

    except KeyError:
        msgstats = "user not found"

    except Exception as e:
        msgstats = e


    return msgstats






if __name__ == '__main__':
    steamkey = 'placeholder'
    #discid = 121853574056640516
    #print(getUserStats(steamkey, discid))
    #print(getHolybotsRatio(steamkey))
    #print(getHolybotsAcc(steamkey))
    #print(getHolybotsMaps(steamkey))
