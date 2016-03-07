import id3
import reader

def printList(nestedList):
    if len(nestedList) == 0:
        return

    if not isinstance(nestedList, list):
        print(nestedList)
    else:
        for index in range(0,len(nestedList)):
            # header += "\t"
            printList(nestedList[index])

# def printList(nestedList):
#     if len(nestedList) == 0:
#         return



relationName, attributeList, dataList = reader.readARFF("contact-lenses.arff")
# relationName, attributeList, dataList = reader.readARFF("restaurants.arff")
# relationName, attributeList, dataList = reader.readARFF("weather.nominal.arff")
# tester = id3.tree("heyo",[4,5])
# print(tester)

# print(relationName)
# print(attributeList)
# print(dataList)

tree = id3.id3(dataList,attributeList,dataList)
header = ""
printList(tree)
print(tree)

