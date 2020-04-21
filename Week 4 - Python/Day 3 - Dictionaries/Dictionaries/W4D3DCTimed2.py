sentence = input("Type a sentence: ")
words = sentence.split()
words.reverse()

message = ""
for x in words:
    message += x + " "

print(message)