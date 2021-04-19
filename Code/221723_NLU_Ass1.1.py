import spacy


#HELPER: RECURSIVE FUNCTION:
def traceback(head, path):
    #append to path list:
    path.append([head, head.dep_])

    #call recursion, if not ROOT:
    if head.dep_ != 'ROOT':
        path = traceback(head.head, path)  

    return path

#FUNCTION: create dependency map from every token to the ROOT in a sentence:
def depmap(sentence):

    #parsing
    spacy_nlp = spacy.load('en_core_web_sm')
    sent = spacy_nlp(sentence)

    #funct:
    dep_map = {}

    for token in sent:
        path = []

        #call recursive function to fill in dependency path from token to every head:
        if token.dep_ != 'ROOT':
            path = traceback(token.head, path)

        #save reversed obtained path (should start with ROOT) to dict:    
        dep_map[token] = list(reversed(path))

    return dep_map


#MAIN:
sentence = 'Pierre Vinken, 61 years old, will join the board as a nonexecutive director Nov. 29.'

#calling function:
map = depmap(sentence)

#printing results:
for key in map:
    print(key, "\t", map[key])
