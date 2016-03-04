# Emily Zhou and Tammy Chen
# EDA132 Machine Learning Assignment

def readARFF(filename):
    file = open(filename, "r")
    relationName = ""
    attributeList = []
    dataList = []
    isData = False
    count = 0
    for line in file:
        # print(count, line)
        count += 1
        # If not a comment and not a new line
        if line[0] != '%' and line[0] != '\n':
            # If it has the relation tag
            if line[0:2].lower() == '@r':
                relationName = line[10:]
            # If it has the attribute tag
            if line[0:2].lower() == '@a':
                categories = []
                tempList = line[11:].split()
                categories.append(tempList[0])
                # print(tempList)
                tempString = tempList[1].strip()[1:-1]
                # print(tempString)
                splitString = tempString.split(',')
                for item in splitString:
                    categories.append(item)
                attributeList.append(categories)

            # If it has the data tag
            if line[0:2].lower() == '@d':
                isData = True

            if isData and line[0] != '@':
                splitData = line.strip().split(',')
                dataList.append(splitData)

    return relationName, attributeList, dataList
