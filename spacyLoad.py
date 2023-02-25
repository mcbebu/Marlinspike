# import anyio
# import appnope
# import attrs

import spacy
nlp = spacy.load('en_core_web_lg')
tokenizeFirstSample = nlp(u'Walk across the road and turn left after the church')
tokenizeSecondSample = nlp(u'walk by the church then turn')
tokenizeThirdSample = nlp(u'walk by the playground and look for a red house')

print(tokenizeFirstSample.similarity(tokenizeSecondSample));
print(tokenizeThirdSample.similarity(tokenizeFirstSample));
POScounts = tokenizeFirstSample.count_by(spacy.attrs.POS)

for token in tokenizeFirstSample:
    if token.pos == "NOUN":
        print(token.text)

# We should remove VERBS such as walk, turn and items that are very common words in most descriptions

# TODO: determine if a description of an area is similar and aggregate them
# After reaching a locale pointed out by google maps, there are 5 different

