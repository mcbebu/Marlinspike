import re
import pandas

def readFile(FILESTRING):
    return pandas.read_csv(FILESTRING)

OpenedFile = readFile("customer_addresses_id.csv")

df = OpenedFile.shape;
print(df[0])
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

def zeroList(n):
    requiredList = []
    for i in range(n):
        requiredList.append(0)
    return requiredList

def getSimilarAddresses(input, limit, column, row):
    results = zeroList(limit)
    tokenInput = tokenize(input)
    databaseSize = df[0]
    for i in range(databaseSize):
        sim = similarity(tokenInput, tokenize(OpenedFile.iloc[column, row]))
        for i in range(len(results)):
            if (sim >= results[i]):
                results.insert(sim, i).pop()
    return results

