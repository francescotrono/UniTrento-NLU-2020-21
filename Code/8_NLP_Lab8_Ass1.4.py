import spacy

#FUNCTION: is subtree of dependents for each token:
def span_root(sentence):

    #check type of input arg:
    if type(sentence) is spacy.tokens.doc.Doc:
        #if Doc, is already parsed:
        doc = sentence
    else:
        #if list, convert to string:
        if type(sentence) is list:
            str1 = " "
            str1 = str1.join(sentence)
        else:
            #casting just for safety:
            str1 = str(sentence)
        
        #and parse:
        spacy_nlp = spacy.load('en_core_web_sm')
        doc = spacy_nlp(str1)

    #convert doc to span:
    span = doc[0:len(doc)+1]
    print(str(span))

    return span.root


#MAIN:
#input can be a string sentence, a list of strings, a sentence in Doc format or directly a span:
word_list = ['a', 'nonexecutive', 'director']
sent = 'a nonexecutive director'
spacy_nlp = spacy.load('en_core_web_sm')
doc = spacy_nlp(sent)
span = doc[0:3]

#calling function (all versions will work):
print(span_root(word_list))
print(span_root(sent))
print(span_root(doc))
print(span_root(span))
