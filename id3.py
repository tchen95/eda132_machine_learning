from random import randint
import math

# tree function
def tree(label, children=[]):
    return [label] + list(children)


def label(tree):
    return tree[0]

def children(tree):
    return tree[1:]


#takes in examples, which is a list of lists, and attributes, which is also a list of lists, and returns decision tree
def id3(examples, attributes, parentExamples):
    if examples is None:
        # Encountering "new" combination of attributes (not present in training set)
        return tree(pluralityValue(attributes[-1], parentExamples))
    sameClass = sameClassification(examples) # returns a classification
    if sameClass != "":
        # Encounter a pure set
        return tree(sameClass)
    elif len(attributes) == 1: # Only contains classification
        # Encountering non-deterministic combination of attributes
        # Same combo of attributes, different classification
        return tree(pluralityValue(attributes[0], examples))
    else:
        splittingAttribute = importance(examples, attributes)
        newAttributes = [] # list without the attribute to be split on
        splittingAttributeCategories = []
        #removes the splitting attribute from list of available attributes and grabs the categories of the splitting attribute
        attributeIndex = 0
        for index in range(0, len(attributes)):
            if attributes[index][0] != splittingAttribute:
                newAttributes += attributes[index]
            else:
                splittingAttributeCategories = attributes[index][1:]
                attributeIndex = index

        splitExamplesList = splitExamples(attributeIndex, splittingAttributeCategories, examples)
        children = []
        for index in range(0, len(splittingAttributeCategories)):
            if subsetIsPure(splitExamplesList[index]):
                return sameClassification(splitExamplesList[index])
            else:
                childTree = id3(splitExamplesList[index], newAttributes, examples)
                children += childTree
        newTree = tree(splittingAttribute, children)
        return newTree


#takes in examples, a list of lists, and attributes, a list of lists, and returns attribute with greatest information gain
def importance(examples, attributes):
    classification1 = []
    classification2 = []
    for entry in examples:
        if entry[-1] == attributes[-1][0]:
            classification1 += [entry]
        else:
            classification2 += [entry]
    attributeGains = []
    #calculates the overall entropy of the examples
    overallEntropy = entropy(len(classification1), len(classification2))
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
            subExamples = divideExamples[subcategory]
            firstClass = []
            secondClass = []
            for entry in subExamples:
                if entry[-1] == attributes[-1][0]:
                    firstClass += [entry]
                else:
                    secondClass += [entry]
            subClassEntropy = entropy(len(firstClass), len(secondClass))
            subCategoryEntropy += [subClassEntropy]
        #calculates information gain from this particular attribute
        subCategoryTotalEntropy = 0
        for counter in range(0, len(subCategoryEntropy)):
            subCategoryTotalEntropy -= ((len(divideExamples[counter]) / len(examples)) * subCategoryEntropy[counter])
        gain = overallEntropy + subCategoryTotalEntropy
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


#takes in number of examples in classification 1 and number of examples in classification 2 and calculates the entropy of that given set of data
def entropy(classification1, classification2):
    totalExamples = classification1 + classification2
    figure1 = classification1 / float(totalExamples)
    figure2 = classification2 / float(totalExamples)
    return ((-1 * figure1) * math.log(figure1, 2)) - ((figure2) * math.log(figure2, 2))


#returns a boolean determining of all the examples are the same classification or not
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
    return categorizedExamples


#return a boolean determining whether or not or subset of examples are all pure
def subsetIsPure(examples):
    classification = examples[0][-1]
    for index in range(1, len(examples)):
        if examples[index][-1] != classification:
            return False
    return True