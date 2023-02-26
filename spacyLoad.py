# import anyio
# import appnope
# import attrs
import spacy
import pandas

nlp = spacy.load('en_core_web_md')
tokenizeFirstSample = nlp(u'I slapped him in the face')
tokenizeSecondSample = nlp(u'he hit me on the head')
print(tokenizeFirstSample.similarity(tokenizeSecondSample)); # returns 0.88
# what is a good threshold?

POScounts = tokenizeFirstSample.count_by(spacy.attrs.POS)

# for token in tokenizeFirstSample:
#     if (token.pos == 91):
#         print(token.text)

# Named Entity Recognition on Singapore address test
prop_noun_sample1 = nlp(u'Yishun Ring Road Block 327')

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + str(spacy.explain(ent.label_)))
    else:
        print("nothing here!")

show_ents(prop_noun_sample1)
#

