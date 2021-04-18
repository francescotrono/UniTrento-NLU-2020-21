import spacy

#FUNCTION: extract subtree of dependents for each token:
def depsubtree(sentence, info=None):

    #parsing
    spacy_nlp = spacy.load('en_core_web_sm')
    sent = spacy_nlp(sentence)

    #funct:
    dep_subtree = {}
    
    if info == True:
        #return list of tokens in subtree with the addition of dep_ and pos_:
        for token in sent:
            buf = []
            for dependent in token.subtree:
                buf.append([dependent, dependent.dep_, dependent.pos_])
            dep_subtree[token] =  buf          

    else:
        #return subtree only:
        for token in sent:
            dep_subtree[token] = token.subtree     

    return dep_subtree


#MAIN:
sentence = 'Pierre Vinken, 61 years old, will join the board as a nonexecutive director Nov. 29.'

#calling depmap function:
depst = depsubtree(sentence)

#printing results:
for key in depst:
    print(key, "\t", list(depst[key]))
