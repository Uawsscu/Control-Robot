from textblob import TextBlob
from capture import *
from Kinect_detect import *

def get_object_train(text):
    # CUT "END"
    nounP = ''
    np = False
    print "Train ---Obj---"
    ans = text[0:-3]
    #print "!!" + ans
    b = TextBlob(ans)
    for item in b.noun_phrases:
        print item
        np = True
        nounP =item

    if(np==False) :
        sentence = b.sentences[0]
        print sentence

        for word, pos in sentence.tags:
            if pos[0:1] == 'N':
                # CAPTURE
                cap_ture(word)
                print word + " >>N"
                nounP =word
                break
    return nounP




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
            Detect(word,'command')
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
            Detect(word, "question")
            print word + " >>N"
            break
    return word

#sub ='Do you know ball'
#get_object_question(sub)
#get_object_command(sub)
#get_verb_command(sub)
#get_object_train(sub)
get_object_train("This is a red dog end")