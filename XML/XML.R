library(XML)
setwd("D:/Datasets/")
document <- xmtTreeParse("foods.xml", useInteralNodes = TRUE)

rootNode <- xmlRoot(document)
xmlName(rootNode)

names(rootNode)
class(rootNode)

rootNode[[2]]
names(rootNode[[2]])
rootNode[[2]][["price"]]