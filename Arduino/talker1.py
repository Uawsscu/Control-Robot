#!/usr/bin/env phthon

import sys
import rospy
from std_msgs.msg import UInt8

from os import path
import pyaudio
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

#from cuttext import *

def speech() :
    MODELDIR = "/home/uawsscu/PycharmProjects/Project2/model"
    DATADIR = "/home/uawsscu/PycharmProjects/Project2/data"

    config = Decoder.default_config()
    config.set_string('-logfn', '/dev/null')
    config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
    config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
    config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
    decoder = Decoder(config)

    # Switch to JSGF grammar
    jsgf = Jsgf(path.join(DATADIR, 'sentence.gram'))
    rule = jsgf.get_rule('sentence.move')  # >> public <move>
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
        buf = stream.read(20)
        if buf:
            decoder.process_raw(buf, False, False)

            if decoder.get_in_speech() != in_speech_bf:
                in_speech_bf = decoder.get_in_speech()
                if not in_speech_bf:
                    decoder.end_utt()

                    try:
                        strDecode = decoder.hyp().hypstr

                        if strDecode != '':
                            if strDecode == 'turn on':
                                printResulf(strDecode)
                                talker(1)
                            elif strDecode == 'turn off':
                                printResulf(strDecode)
                                talker(0)
                            elif strDecode[-3:] == 'end':
                                printResulf(strDecode)
                                print "1"
                                # get_object_train(decoder.hyp().hypstr)
                            elif strDecode[:5] == 'jerry':
                                printResulf(strDecode)
                                print "2"
                                # get_object_command(strDecode)
                            elif strDecode[:11] == 'do you know':
                                printResulf(strDecode)
                                print "3"
                                # get_object_question(strDecode)
                    except AttributeError:
                        pass

                    decoder.start_utt()
        else:
            break
    decoder.end_utt()
    print('An Error occured :', decoder.hyp().hypstr)


def talker(msg):
    pub = rospy.Publisher('setLed', UInt8, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    pub.publish(int(msg))

def printResulf(strDecode) :
    print 'Stream decoding result:', strDecode

if __name__ == '__main__':
    speech()