import re
import pandas

testString1 = pandas.read_csv("customer_addresses_id.csv").iloc[0,1]
testString2 = pandas.read_csv("customer_addresses_id.csv").iloc[0,2]

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


