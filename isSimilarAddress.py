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
    """
    Tokenises a string by spliting it at commas and removes ignored words
    :param str: string to be tokenised
    :return: List of tokens
    """
    strList = str.split(", ")
    for i in range(len(strList)):
        for IW in IGNORED_WORDS:
            strList[i] = re.sub(IW, "", strList[i])
    strList.sort()
    return strList

def similarity(add1, add2):
    """

    :param add1: address 1
    :param add2: address 2
    :return: Similarity index of (matching tokens / longest address tokens)
    """
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
    """

    :param n: number of elements
    :return: list of n elements all initialised to Zero
    """
    requiredList = []
    for i in range(n):
        requiredList.append(0)
    return requiredList

def getSimilarAddresses(input, limit, file, column):
    """

    :param input: the address the driver wants to go to
    :param limit: the amount of similar addresses required
    :param file: the database to read from
    :param column: the column where the addresses to be compared to are
    :return: A list of size limit containing the top {Location : Similarity} pairs
    """
    results = zeroList(limit)
    simResults = zeroList(limit)
    OpenedFile = readFile(file)
    databaseSize = OpenedFile.shape[0]
    for i in range(databaseSize):
        sim = similarity(input, OpenedFile.iloc[i, column])
        for j in range(len(results)):
            if (sim >= simResults[j]):
                simResults.insert(j, sim)
                simResults.pop()
                results.insert(j, OpenedFile.iloc[i, column])
                results.pop()
                break
    return dict(zip(results, simResults))

x = getSimilarAddresses("jalan Rawakuda pengaritan Rt01/Rw01 · Karangharum (Karang Harum), Jawa Barat, Kab. Bekasi, Kedung Waringin"
                          , 5, "customer_addresses_id.csv", 1)

[print(y) for y in x.items()]