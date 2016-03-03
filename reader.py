from collections import namedtuple

def readARFF(filename):
    file = open(filename, "r")
    name = ""
    attributeList = []

    for line in file:
        line.strip()
        if line[0] != "%":
            print(line)
