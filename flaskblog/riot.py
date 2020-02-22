import requests

APIKey = "RGAPI-234ec76f-0cd6-4095-8286-deaa6e3103a0"


def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/" + \
        "summoner/v4/summoners/by-name/" + summonerName + '?api_key=' + APIKey
    # https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/ori%C3%B3n
    print(URL)
    response = requests.get(URL)
    return response.json()


def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + \
        ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + '?api_key=' + APIKey
    #/lol/league/v4/entries/by-summoner/{encryptedSummonerId}
    print(URL)
    response = requests.get(URL)
    return response.json()


def requestLiveData(region, ID, APIKey):
    URL = "https://" + region + \
        ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + \
        ID + '?api_key=' + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()


def main():
    region = "na1"

    summonerName = str(
        input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: '))

    APIKey = "RGAPI-234ec76f-0cd6-4095-8286-deaa6e3103a0"
    responseJSON = requestSummonerData(region, summonerName, APIKey)
    print(responseJSON)

    ID = responseJSON['id']
    ID = str(ID)
    print(ID)
    responseJSON2 = requestRankedData(region, ID, APIKey)
    print(responseJSON2)
    print(responseJSON2[0]['tier'])
    print(responseJSON2[0]['rank'])

    responseJSON3 = requestLiveData(region, ID, APIKey)
    for item in responseJSON3:
        print(item + ": " + str(responseJSON3[item]))

    participants = responseJSON3["participants"]
    for player in participants:
        print(player["summonerName"])


class player:

    summonerName: str

    def __init__(self, json: set):
        self.summonerId = set["summonerName"]


if __name__ == '__main__':
    main()
