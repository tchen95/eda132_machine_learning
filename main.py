import id3
import reader

relationName, attributeList, dataList = reader.readARFF("restaurants.arff")
# tester = id3.tree("heyo",[4,5])
# print(tester)
print(id3.id3(dataList,attributeList,dataList))