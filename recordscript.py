import pyaudio
from Notes import *
import numpy
import keyboard

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 800
NOFFRAMES = 220
RECORD_SECONDS = 5
note = Notes(Notes(4,5).makeNotes(),Notes(4,5).makeFreq())
audio = pyaudio.PyAudio();
stream = audio.open(format=FORMAT, channels=CHANNELS,
                 rate= RATE, input=True,
                 frames_per_buffer=CHUNK)
print("press q to exit")
#for i in range(0,int(RATE/CHUNK * RECORD_SECONDS)):
while True:
    data = stream.read(CHUNK)
    decoded = numpy.fromstring(data,dtype=np.int16)
    index = note.compareFreq(note.freq,note.getFreq(decoded,RATE))
    #print(note.getFreq(decoded,RATE))
    if keyboard.is_pressed('q'): # if q is pressed
        break
    else:
        pass


    print (note.note[index])
    print (note.getFreq(decoded,RATE))

# for i in range(0,int(RATE/CHUNK * RECORD_SECONDS)):
#      data=stream.read(CHUNK)
#      index = compareFreq(Notes().makeFreq(),Notes().getFreq(data))
#      note = Notes().makeNotes()
#      print (note[index])

print("ended")




