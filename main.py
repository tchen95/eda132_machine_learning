import id3
import reader

relationName, attributeList, dataList = reader.readARFF("restaurants.arff")
finalTree = id3.id3(dataList,attributeList,dataList)
print(finalTree)

# testAttributes = [['wind','weak','strong'],['willGo','y','n']]
# testData = [['weak','y'],['weak','y'],['weak','y'],['weak','y'],['weak','y'],['weak','y'],['weak','n'],['weak','n'],['strong','y'],['strong','y'],['strong','y'],['strong','n'],['strong','n'],['strong','n']]

# print(id3.importance(testData,testAttributes))