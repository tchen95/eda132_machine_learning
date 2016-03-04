import id3
import reader
relationName, attributeList, dataList = reader.readARFF("restaurants.arff")

print(id3.id3(dataList,attributeList,dataList))