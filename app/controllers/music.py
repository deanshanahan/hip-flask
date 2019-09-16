""" Responds healthy if the service is healthy.
"""

import json
from flask import Blueprint
from flask import Response
import numpy 
import math
import pyaudio   
import sys

MUSIC = Blueprint('music', __name__)

@MUSIC.route('', methods=['GET'])
def music():
    """ Return statement stating the service is healthy if the service
    is running. """
    
    PyAudio = pyaudio.PyAudio     #initialize pyaudio
    
    #See https://en.wikipedia.org/wiki/Bit_rate#Audio
    BITRATE = 16000     #number of frames per second/frameset.      
    
    FREQUENCY = 500     #Hz, waves per second, 261.63=C4-note.
    LENGTH = 1     #seconds to play sound
    
    if FREQUENCY > BITRATE:
        BITRATE = FREQUENCY+100
    
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''    
    
    #generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    
    
    for x in range(RESTFRAMES): 
        WAVEDATA = WAVEDATA+chr(128)
    
    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), 
                    channels = 1, 
                    rate = BITRATE, 
                    output = True)
    
    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()

    return Response("{'status':'healthy'}", status=200, mimetype='application/json')
