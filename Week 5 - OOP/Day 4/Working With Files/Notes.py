
# # A way of overwriting text in a doc...
#
# with open("a_file.text", "r") as f:
#     text = f.read()
#
# text = "some new text " + text
#
# with open("a_file.text", "w") as f:
#     f.write(text)

with open("star_wars.txt", 'r') as f:
    for line in f.readlines():
        print(line)

with open("star_wars.txt", 'r') as f:
    # lines = f.readlines()
    # print(lines[4])
    #
    # words = list(map(list, lines))
    # print(words)

    lines = [line.replace("\n","") for line in f.readlines()]
    print(lines.count("Darth"))
    print(lines.count("Luke"))
    print(lines.count("Lea"))

with open("star_wars.txt", "a+") as f:
    f.write("Benjy")
with open("star_wars.txt", "r") as f:
    text = f.read()


import json
d = [{"name": "John", "age": 21}, {"name": "Sarah", "age": 32}]
with open("family.json", "w") as f:
    json.dump(d, f)
with open("family.json", "r") as f:
    d = json.load(f)
d.append({"name": "Tommy", "age": 15})
with open("family.json", "w") as f:
    json.dump(d, f)


