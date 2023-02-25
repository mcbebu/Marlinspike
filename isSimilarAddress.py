import re
import pandas

def readFile(FILESTRING):
    return pandas.read_csv(FILESTRING)

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
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                matchingTokens += 1
                # solve edge case of str1 which have many copies of a word from str2
                str2[i] = re.sub("token2","",str2[i])
                continue
    return matchingTokens/totalTokens

def zeroList(n):
    requiredList = []
    for i in range(n):
        requiredList.append(0)
    return requiredList

def getSimilarAddresses(input, limit, file, column):
    results = zeroList(limit)
    OpenedFile = readFile(file)
    databaseSize = OpenedFile.shape[0]
    for i in range(databaseSize):
        sim = similarity(input, OpenedFile.iloc[i, column])
        for i in range(len(results)):
            if (sim >= results[i]):
                results.insert(i, sim)
                results.pop()
                break
    return results

print(getSimilarAddresses("jalan Rawakuda pengaritan Rt01/Rw01 · Karangharum (Karang Harum), Jawa Barat, Kab. Bekasi, Kedung Waringin"
                          , 5, "customer_addresses_id.csv", 1))