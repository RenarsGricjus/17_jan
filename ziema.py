raksts = input("Write your name: ")
with open("name.txt", "w", encoding="utf8") as theshit:
    theshit.write(raksts)

# encoding izmanto lai varētu atpazīt latviešu burtus.