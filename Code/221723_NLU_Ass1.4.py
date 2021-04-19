import spacy

#global var
spacy_nlp = spacy.load('en_core_web_sm')

#FUNCTION: identify head of span:
def span_root(sentence):

    #TYPECHECK:
    #if already Span, directly call built-in method:
    if type(sentence) is spacy.tokens.span.Span:
        #print(str(sentence))
        return sentence.root

    #if Doc (already parsed):
    elif type(sentence) is spacy.tokens.doc.Doc:
        #convert Doc to Span:
        span = sentence[0:len(sentence)+1]
        #print(str(span))
        return span.root

    else:
        #if list of strings or of tokens:
        if type(sentence) is list:
            #if list of tokens, convert to list of strings:
            if type(sentence[0]) is spacy.tokens.token.Token:
                sentence = [token.text for token in sentence]
            #convert list to one single string:
            str1 = " "
            str1 = str1.join(sentence)
        else:
            #one single string:
            str1 = str(sentence)
        
        #parsing (calling global variable):
        doc = spacy_nlp(str1)

        #convert doc to span:
        span = doc[0:len(doc)+1]
        #print(str(span))

        return span.root


#MAIN:
#input can be a string sentence...
sent = 'a nonexecutive director'
#...a list of strings...
word_list = ['a', 'nonexecutive', 'director']
#...a sentence in Doc format...
doc = spacy_nlp(sent)
#...a span...
span = doc[0:3]
#...or a list of tokens
tok_lst = [token for token in span]

#calling function (all versions will work):
print(span_root(sent))
print(span_root(word_list))
print(span_root(doc))
print(span_root(span))
print(span_root(tok_lst))
