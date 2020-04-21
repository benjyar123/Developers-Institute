# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

zipped = zip(keys, values)
dictionary = dict(zipped)
print(dictionary)

# Exercise 2

store = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 1.
store['number_stores'] = 2

# 2.
print(store["name"] + "'s customers are " + store["type_of_clothes"][0] + ", " + store["type_of_clothes"][1] + " and " + store["type_of_clothes"][2] + ".")

# 3.
store["country_creation"] = "Spain"

#4.
if "international_competitors" in store.keys():
    store["international_competitors"].append("Desigual")

# 5.
del store["creation_date"]

# 6.
print(store["international_competitors"][-1])

# 7.
text = "The major colours in the US are {} and {}.".format(store["major_color"]["US"][0], store["major_color"]["US"][1])
print(text)

# 8.
print(len(store))

# 9.
print(store.keys())

#10
more_on_store = {
    "creation_date": 1975,
    "number_stores": 10000,
}

store["number_stores"] = more_on_store["number_stores"]
print(store["number_stores"])

# Bonus Section
# 1)
store["stores_worldwide"] = {}

# 2.
def addStore (country, number):
    if "stores_worldwide" in store.keys():
        # store["stores_worldwide"].update({country: number})
        store["stores_worldwide"][country] = number

# 3.
print(store["stores_worldwide"])

# 4.
addStore("Italy", 22)
addStore("Belgium", 14)

print(store)