import re
import pandas

testString1 = pandas.read_csv("customer_addresses_id.csv").iloc[0,1]
testString2 = pandas.read_csv("customer_addresses_id.csv").iloc[16,1]
#tokenize
# by commas
# sort
# ignore common words

IGNORED_WORDS = {"ja?l?a?n? ", "jakarta"}
def tokenize(str):
    strList = str.split(", ")
    for i in range(len(strList)):
        for IW in IGNORED_WORDS:
            strList[i] = re.sub(IW, "", strList[i])
    strList.sort()
    return strList

def similarity(add1, add2):
    str1 = tokenize(add1)
    str2 = tokenize(add2)
    totalTokens = max(len(str1), len(str2))
    matchingTokens = 0;
    for token1 in str1:
        for token2 in str2:
            if token1 == token2:
                matchingTokens += 1
                continue
    return matchingTokens/totalTokens


def getSimilarAddresses(curr, limit):
    results = []
