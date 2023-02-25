import re
import pandas


def readFile(FILESTRING):
    return pandas.read_csv(FILESTRING)


# tokenize
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
                str2[i] = re.sub("token2", "", str2[i])
                continue
    return matchingTokens / totalTokens


def zeroList(n):
    """

    :param n: number of elements
    :return: list of n elements all initialised to Zero
    """
    requiredList = []
    for i in range(n):
        requiredList.append(0)
    return requiredList


def generate_data_frame(database):
    """
    Generates a pandas dataframe given a dictionary
    :param database: {key1: valueArray1 ... keyN: valueArrayN}
    :return: A dataframe that contains keys as columns and rows as valueArrays
    """
    # goal: extract one list for each key
    KeysList = []
    ValuesList = []
    for item in database.keys():
        KeysList.append(item)
    for item in database.values():
        ValuesList.append(item)
    df = pandas.DataFrame(ValuesList).transpose()
    df.columns = KeysList
    return df



def get_similar_addresses(location, limit, customer_info, column):
    """

    :param location: the address the driver wants to go to
    :param limit: the amount of similar addresses required
    :param customer_info: the dictionary to read from
    :param column: the column where the addresses to be compared to are
    :return: A list of size limit containing the top {X: x, Y: y, Desc: driverDesc} dictionaries
    """
    results = zeroList(limit)
    sim_results = zeroList(limit)
    df = generate_data_frame(customer_info)
    database_size = df.shape[0]
    for i in range(database_size):
        sim = similarity(location, df.iloc[i, column])
        for j in range(len(results)):
            if sim >= sim_results[j]:
                sim_results.insert(j, sim)
                sim_results.pop()
                results.insert(j, df.iloc[i, column])
                results.pop()
                break
    return dict(zip(results, sim_results))

sample_dict = {"Addresses": ["addr1", "addr2"],
               "X": ["x1", "x2"],
               "Y": ["y1", "y2"],
               "Desc": ["desc1", "desc2"]}

x = get_similar_addresses("addr1", 1, sample_dict, 0)

[print(y) for y in x.items()]
