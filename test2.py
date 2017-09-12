from textblob import TextBlob
from capture import *

def get_object_train(text):
    # CUT "END"
    print "Train ---Obj---"
    ans = text[6:-3]
  #  print "!!" + ans
    b = TextBlob(ans)
    sentence = b.sentences[0]
    print sentence
    for word, pos in sentence.tags:
        if pos[0:1] == 'N':
            # CAPTURE
            #cap_ture(word)
            print word + " >>N"
            break
    return word

def get_object_command(text):
    print "Command ---Obj---"
    ans = text[6:]
    print "!!" + ans
    b = TextBlob(ans)
    sentence = b.sentences[0]
    print sentence
    for word, pos in sentence.tags:
        if pos[0:1] == 'N':
            # CAPTURE
            # cap_ture(word)
            print word + " >>N"
            break
    return word

def get_verb_command(text):
    print "Command --Verb--"
    b = TextBlob(text)
    sentence = b.sentences[0]
    print sentence
    for word, pos in sentence.tags:
        if pos[0:1] == 'V':
            # CAPTURE
            #cap_ture(word)
            print word + " >>V"
            break
    return word

def get_object_question(text):
    print "question--Obj--"
    b = TextBlob(text)
    sentence = b.sentences[0]
    print sentence
    for word, pos in sentence.tags:
        if pos[0:1] == 'N':
            # CAPTURE
            # cap_ture(word)
            print word + " >>N"
            break
    return word

sub ='Do you know ball'
get_object_question(sub)
get_object_command(sub)
get_verb_command(sub)
get_object_train(sub)