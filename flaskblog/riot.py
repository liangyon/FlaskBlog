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


if __name__ == '__main__':
    main()
