import requests, json

# This code runs an api request to get all player stats for a given team in the premier league 2019-20 season
# team ids need to go in the url (collected from a separate api request)
# each time code is run with different team id a local json db of all imported players is added to -
# ready for later use with populate module

url = "https://v2.api-football.com/players/team/37/2019-2020"
headers = {
    'x-rapidapi-host': "https://api-football-v1.p.rapidapi.com/v2/players/team/37/2019-2020",
    'x-rapidapi-key': "a9e9fb42eaa5fa6f668f5bc36a11ed4b"
    }
response = requests.request("GET", url, headers=headers)
print(response.text)
api_data = response.json()

with open('cards/newplayers.json', 'r') as f:
    json_data = json.load(f)
    player_list = json_data["api"]["players"]
    print(len(player_list))

for player in api_data["api"]["players"]:
    player_list.append(player)
print(len(player_list))

with open('cards/newplayers.json', 'w') as f:
        json.dump(json_data, f)
