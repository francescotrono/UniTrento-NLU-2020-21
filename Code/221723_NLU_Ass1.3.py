import spacy

#FUNCTION: is test_snt a subtree:
def is_subtree(sentence, test_snt):

    #parsing
    spacy_nlp = spacy.load('en_core_web_sm')
    sent = spacy_nlp(sentence)
    test = spacy_nlp(test_snt)

    #funct:
    subtree = []
    test_txt = [token.text for token in test]
    print("Testing: {}".format(test_txt))
    
    #return subtree only:
    for token1 in test:
        for token in sent:
            if token.text == token1.text:
                subtree = token.subtree
                sbt_txt = [toks.text for toks in subtree]
                #print(sbt_txt)

                if (test_txt == sbt_txt):
                    print("Found subtree: {}".format(sbt_txt))
                    return True
    
    print("Not a subtree.")
    return False


#MAIN:
sentence = 'Pierre Vinken, 61 years old, will join the board as a nonexecutive director.'

test = 'a nonexecutive director'
test2 = 'old, will'
test3 = 'the board'

#calling function:
print(is_subtree(sentence, test)) #true
print(is_subtree(sentence, test2)) #false
print(is_subtree(sentence, test3)) #true
