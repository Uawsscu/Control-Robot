from os import path
import pyaudio
import sys
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

from textblob import TextBlob

from capture import *


class CutText():
    # -------FOR TRAIN ONLY-------
    def get_object(self, text):  # this is a ball end
        # CUT_"END" [0:3]
        ans = text[0:-3]
        print "!!"+ans
        b = TextBlob(ans)
        sentence = b.sentences[0]
        for word, pos in sentence.tags :
            if pos[0:1] == 'N':
                print word + " >>N"
                return word







MODELDIR = "/home/uawsscu/PycharmProjects/Project2/model"
DATADIR = "/home/uawsscu/PycharmProjects/Project2/data"

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
decoder = Decoder(config)

# Switch to JSGF grammar
jsgf = Jsgf(path.join(DATADIR, 'sentence.gram'))
rule = jsgf.get_rule('sentence.move') #>> public <move>
fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
fsg.writefile('sentence.fsg')

decoder.set_fsg("sentence", fsg)
decoder.set_search("sentence")

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

in_speech_bf = False
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        if decoder.get_in_speech():
            sys.stdout.write('.')
            sys.stdout.flush()
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()

                try:
                    strDecode = decoder.hyp().hypstr
                    if strDecode != '':
                        print 'Stream decoding result:', strDecode
                        if strDecode[-3:] == 'end':
                            CutText().get_object(decoder.hyp().hypstr)
                except AttributeError:
                    pass

                decoder.start_utt()
    else:
        break
decoder.end_utt()
print('An Error occured :', decoder.hyp().hypstr)