import id3
import reader

def printList(nestedList,header):
    if len(nestedList) == 0:
        print("\n")
        return
    if not isinstance(nestedList, list):
        # header = header[1:]
        print(header+"|"+nestedList)
    else:
        # print(nestedList[0])
        header += "  "
        for index in range(0,len(nestedList)):
            printList(nestedList[index],header)

# def printList(nestedList):
#     if len(nestedList) == 0:
#         return



relationName, attributeList, dataList = reader.readARFF("contact-lenses.arff")
tree = id3.id3(dataList,attributeList,dataList)
header = ""
print(relationName)
printList(tree,header)

relationName, attributeList, dataList = reader.readARFF("restaurants.arff")
tree = id3.id3(dataList,attributeList,dataList)
header = ""
print("\n\n"+relationName)
printList(tree,header)

relationName, attributeList, dataList = reader.readARFF("weather.nominal.arff")
tree = id3.id3(dataList,attributeList,dataList)
header = ""
print("\n\n"+relationName)
printList(tree,header)

# print(tree)

