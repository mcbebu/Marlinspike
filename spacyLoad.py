# import anyio
# import appnope
# import attrs
import spacy
import pandas

nlp = spacy.load('en_core_web_md')
tokenizeFirstSample = nlp(u'I slapped him in the face')
tokenizeSecondSample = nlp(u'he hit me on the head')
tokenizeThirdSample = nlp(u'walk by the playground and look for a red house')

print(tokenizeFirstSample.similarity(tokenizeSecondSample)); # returns 0.88
print(tokenizeThirdSample.similarity(tokenizeSecondSample)); # returns 0.77
# what is a good threshold?

POScounts = tokenizeFirstSample.count_by(spacy.attrs.POS)

for token in tokenizeFirstSample:
    if (token.pos == 91):
        print(token.text)

# We should remove VERBS such as walk, turn and items that are very common words in most descriptions

# TODO: determine if a description of an area is similar

