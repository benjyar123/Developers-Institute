import json
from .models import Player

def populate_team():
    with open("newplayers.json", "r") as f:
        data = json.load(f)
        print("test")

        for x in range (len(data["api"]["players"])):
            if data["api"]["players"][x]["league"] == "Championship":
                # kwargs = {
                #     "first_name": data["api"]["players"][x]["firstname"],
                #     "last_name": data["api"]["players"][x]["lastname"],
                #     "position": data["api"]["players"][x]["position"],
                #     "age": data["api"]["players"][x]["age"],
                #     "nationality": data["api"]["players"][x]["nationality"],
                #     "team_name": data["api"]["players"][x]["team_name"],
                #     "height": data["api"]["players"][x]["height"],
                #     "weight": data["api"]["players"][x]["weight"],
                #     "appearances": data["api"]["players"][x]["games"]["appearences"],
                #     "goals": data["api"]["players"][x]["goals"]["total"],
                #     "passing_accuracy": data["api"]["players"][x]["passes"]["accuracy"],
                #     "successful_dribbles": data["api"]["players"][x]["dribbles"]["success"],
                #     "tackles": data["api"]["players"][x]["tackles"]["total"],
                #     "fouls_committed": data["api"]["players"][x]["fouls"]["committed"],
                # }

                player = Player()
                player.first_name = data["api"]["players"][x]["firstname"]
                player.last_name = data["api"]["players"][x]["lastname"]
                player.position = data["api"]["players"][x]["position"]
                player.age = data["api"]["players"][x]["age"]
                player.nationality = data["api"]["players"][x]["nationality"]
                player.team_name = data["api"]["players"][x]["team_name"]
                player.height = data["api"]["players"][x]["height"]
                player.weight = data["api"]["players"][x]["weight"]
                player.appearances = data["api"]["players"][x]["games"]["appearences"]
                player.goals = data["api"]["players"][x]["goals"]["total"]
                player.passing_accuracy = data["api"]["players"][x]["passes"]["accuracy"]
                player.successful_dribbles = data["api"]["players"][x]["dribbles"]["success"]
                player.tackles = data["api"]["players"][x]["tackles"]["total"]
                player.fouls_committed = data["api"]["players"][x]["fouls"]["committed"]
                player.save()
                print("should be about to save")
                print(player.team_name + ": " + player.first_name + " " + player.last_name)

                # for items in kwargs.items():
                #     print (items[0], items[1])
                #
                # print(kwargs.items())
                # print(" ")

# populate_team()

