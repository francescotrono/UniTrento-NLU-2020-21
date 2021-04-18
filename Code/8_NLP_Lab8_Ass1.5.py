import spacy

#FUNCTION: is subtree of dependents for each token:
def key_spans(sentence):

    #parsing:
    spacy_nlp = spacy.load('en_core_web_sm')
    sent = spacy_nlp(sentence)

    keyspans = {}

    for token in sent:
        #subject, direct object or indirect object (dative):
        if (token.dep_ == 'nsubj') or (token.dep_ == 'dobj') or (token.dep_ == 'dative'):
            dep = token.dep_
            #get subtree:
            span_wds = list(token.subtree)
            #save in dict:
            keyspans[dep] = span_wds
    
    return keyspans


#MAIN:
sentence = 'Pierre Vinken, 61 years old, will give the board a new task as the nonexecutive director.'

#calling function:
ksp = key_spans(sentence)

#printing results:
for key in ksp:
    print(key, "\t", list(ksp[key]))
