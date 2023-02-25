import re

#tokenize
# by commas
# sort
# ignore common words

IGNORED_WORDS = {"ja?l?a?n?", "jakarta"}
def tokenize(str)
    strList = str.split(", ")

