from random import randint
import math
# tree function
def tree(label, children=[]):
    return [label] + list(children)


def label(tree):
    return tree[0]


def children(tree):
    return tree[1:]


# takes in examples, which is a list of lists, and attributes, which is also a list of lists, and returns decision tree
def id3(examples, attributes, parentExamples):
    if examples == []:
        # Encountering "new" combination of attributes (not present in training set)
        return tree(pluralityValue(attributes[-1], parentExamples))
    sameClass = sameClassification(examples)  # returns a classification
    if sameClass != "":
        # Encounter a pure set
        return tree(sameClass)
    elif len(attributes) == 1:  # Only contains classification
        # Encountering non-deterministic combination of attributes
        # Same combo of attributes, different classification
        return tree(attributes[0]+" = "+pluralityValue(attributes[0], examples))
    else:
        splittingAttribute = importance(examples, attributes)
        newAttributes = []  # list without the attribute to be split on
        splittingAttributeCategories = []
        #removes the splitting attribute from list of available attributes and grabs the categories of the splitting attribute
        attributeIndex = 0
        for index in range(0, len(attributes)):
            if attributes[index][0] != splittingAttribute:
                newAttributes += [attributes[index]]
            else: 
                newAttributes += [["XXXXX"]]
                splittingAttributeCategories = attributes[index][1:]
                attributeIndex = index
        splitExamplesList,subCategory = splitExamples(attributeIndex, splittingAttributeCategories, examples)
        children = []
        for index in range(0, len(splittingAttributeCategories)):
            if subsetIsPure(splitExamplesList[index]):
                children += tree(splittingAttribute+ " = "+splitExamplesList[index][0][attributeIndex]+": "+sameClassification(splitExamplesList[index]))
            else:
                treeResult = id3(splitExamplesList[index], newAttributes, examples)
                treeResult[0] = splittingAttribute + " = " + splittingAttributeCategories[index]
                children += treeResult
        return tree(splittingAttribute, [children])


#takes in examples, a list of lists, and attributes, a list of lists, and returns attribute with greatest information gain
def importance(examples, attributes):
    attributeGains = []
    #calculates the overall entropy of the examples
    overallEntropy = editedEntropy(examples, attributes[-1][1:])
    # overallEntropy = entropy(len(classification1), len(classification2))
    for index in range(0, len(attributes) - 1):
        #creates a new sublist for each subcategory of this attribute
        divideExamples = []
        numSubCategories = len(attributes[index]) - 1
        while numSubCategories != 0:
            divideExamples += [[]]
            numSubCategories -= 1
        #divides up the examples amongst each subcategory
        for entry in examples:
            for subcategory in range(0, len(attributes[index]) - 1):
                if entry[index] == attributes[index][subcategory + 1]:
                    divideExamples[subcategory] += [entry]
        #for each subcategory, calculate the entropy
        subCategoryEntropy = []
        for subcategory in range(0, len(divideExamples)):
            subClassEntropy = editedEntropy(divideExamples[subcategory], attributes[-1][1:])
            subCategoryEntropy += [subClassEntropy]
        #calculates information gain from this particular attribute
        subCategoryTotalEntropy = 0
        for counter in range(0, len(subCategoryEntropy)):
            subCategoryTotalEntropy -= ((len(divideExamples[counter]) / float(len(examples))) * subCategoryEntropy[counter])
        gain = overallEntropy + subCategoryTotalEntropy
        if attributes[index][0] == "XXXXX":
            attributeGains += [-1000000] 
        else:
            attributeGains += [gain]
    #finds the attribute with the best information gain
    maxAttribute = 0
    maxGain = -100000
    for index in range(0, len(attributeGains)):
        if attributeGains[index] > maxGain:
            maxGain = attributeGains[index]
            maxAttribute = index
    return attributes[maxAttribute][0]


def pluralityValue(lastAttribute, parentExamples):
    class1 = 0
    class2 = 0
    for example in parentExamples:
        if example[-1] == lastAttribute[1]:
            class1 += 1
        else:
            class2 += 1
    if class1 > class2:
        return lastAttribute[1]
    elif class2 > class1:
        return lastAttribute[2]
    else:
        return lastAttribute[randint(1, 2)]

#takes in examples, a list of lists, and classSubcategories, a list of strings, and outputs the total entropy of the given examples
def editedEntropy(examples, classSubcategories):
    classSublist = []
    numSubCategories = len(classSubcategories)
    while numSubCategories != 0:
        classSublist += [0]
        numSubCategories -= 1
    for example in examples:
        for category in range(0, len(classSubcategories)):
            if example[-1] == classSubcategories[category]:
                classSublist[category] += 1
    totalEntropy = 0
    for item in range(0, len(classSublist)):
        if classSublist[item] != 0:
            figure = classSublist[item] / float(len(examples))
            totalEntropy -= (figure * math.log(figure, 2))
    return totalEntropy


#returns the classification for a pure set
def sameClassification(examples):
    classification = examples[0][-1]
    for index in range(1, len(examples)):
        if examples[index][-1] != classification:
            return ""
    return classification


#takes in attribute, and integer, subcategories, a list of strings, and examples, a list of lists, and returns a list of lists, which correspond to the examples split amongst the appropriate subcategories
def splitExamples(attribute, subCategories, examples):
    categorizedExamples = []
    numSubCategories = len(subCategories)
    while numSubCategories != 0:
        categorizedExamples += [[]]
        numSubCategories -= 1
    for subcategory in range(0, len(subCategories)):
        for entry in examples:
            if entry[attribute] == subCategories[subcategory]:
                categorizedExamples[subcategory] += [entry]
    return categorizedExamples, subCategories[subcategory]


#return a boolean determining whether or not or subset of examples are all pure
def subsetIsPure(examples):
    if examples == []:
        return False
    classification = examples[0][-1]
    for index in range(1, len(examples)):
        if examples[index][-1] != classification:
            return False
    return True