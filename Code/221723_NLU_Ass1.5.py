import spacy

#FUNCTION: is subtree of dependents for each token:
def key_spans(sentence, out):

    if out not in ['chunk', 'subtree']:
        return -1

    #parsing:
    spacy_nlp = spacy.load('en_core_web_sm')
    sent = spacy_nlp(sentence)

    keyspans = {}
    #key labels:
    #subject (nsubj, nsubjpass, csubj, csubjpass), direct object (dobj), indirect object (dative):
    key_labels = ['nsubj', 'nsubjpass', 'csubj', 'csubjpass', 'dobj', 'dative']

    if out == 'chunk':
        for chunk in sent.noun_chunks:
            #find relevant dep relations:
            if chunk.root.dep_ in key_labels:
                dep = chunk.root.dep_
                #save in dict:
                keyspans[dep] = list(chunk)
    else:
        for token in sent:
            #find relevant dep relations:
            if token.dep_ in key_labels:
                dep = token.dep_
                #get subtree:
                span_wds = list(token.subtree)
                #save in dict:
                keyspans[dep] = span_wds
    
    return keyspans


#MAIN:
sentence = 'The managing director Pierre Vinken will award finance director Paula Merkel a prize for her achievements.'

#calling function:
ksp = key_spans(sentence, out='subtree')
#ksp = key_spans(sentence, out='chunk')

#printing results 1:
for key in ksp:
    print(key, "\t", ksp[key])
