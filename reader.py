# Emily Zhou and Tammy Chen
# EDA132 Machine Learning Assignment

def readARFF(filename):
    file = open(filename, "r")
    relationName = ""
    attributeList = []
    dataList = []
    isData = False

    for line in file:
        # If not a comment and not a new line
        if line[0] != '%' and line[0] != '\n':
            # If it has the relation tag
            if line[1].lower() == 'r':
                relationName = line[10:]
            # If it has the attribute tag
            if line[1].lower() == 'a':
                categories = []
                tempList = line[11:].split("\t")
                categories.append(tempList[0])
                tempString = tempList[1].strip()[1:-1]
                splitString = tempString.split(',')
                for item in splitString:
                    categories.append(item)
                attributeList.append(categories)

            # If it has the data tag
            if line[1].lower() == 'd':
                isData = True

            if isData and line[0] != '@':
                splitData = line.strip().split(',')
                dataList.append(splitData)

    return relationName, attributeList, dataList

relationName, attributeList, dataList = readARFF("restaurants.arff")
print(relationName)
print(attributeList)
print(dataList)
