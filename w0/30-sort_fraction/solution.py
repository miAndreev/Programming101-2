from collections import OrderedDict
from operator import itemgetter

def sort_fractions(fractions):
    fractionsDictionary = {}
    for fraction in fractions:
        fractionsDictionary[fraction] = fraction[0] / fraction[1]
    
    orderedFractionsDict = OrderedDict(sorted(fractionsDictionary.items(), key=itemgetter(1)))
    outputOrderedFractions = []
    
    for fraction in orderedFractionsDict:
        outputOrderedFractions.append(fraction)
    
    return outputOrderedFractions
