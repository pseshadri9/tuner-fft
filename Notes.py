from scipy.fftpack import fft
from math import floor
import numpy as np
#import operator
class Notes():
    def __init__(self,note, freq):
        self.note = note
        self.freq = freq


    def makeNotes(self):
        note = []
        v = 1
        count = 0
        for z in range(0, 108):
            if v>12:
                v = v - 12
                count = count + 1
            if v == 1:
                note.append('C%d' % (count))
            elif v == 2:
                note.append('C#/Db(%d)' % (count))
            elif v == 3:
                note.append('D%d' % (count))
            elif v == 4:
                note.append('D#/Eb(%d)' % (count))
            elif v == 5:
                note.append('E%d' % (count))
            elif v == 6:
                note.append('F%d' % (count))
            elif v == 7:
                note.append('F#/Gb(%d)' % (count))
            elif v == 8:
                note.append('G%d' % (count))
            elif v == 9:
                note.append('G#/Ab(%d)' % (count))
            elif v == 10:
                note.append('A%d' % (count))
            elif v == 11:
                note.append('A#/Bb(%d)' % (count))
            elif v == 12:
                note.append('B%d'% (count))
            v = v + 1
        return note

    def makeFreq(self):
        freq = []
        for x in range(0,108):
            freq.append(16.3516 * (2 ** (x/12)))
        return freq

    def getFreq(self,snd,fs):
        # #fft_output = fft(snd)
        # norm = 2.**(int(str(snd.dtype)[-2:]) - 1) # normalize between -1 and 1
        # snd = snd / norm
        # #print(snd.shape, snd)
        # s1 = snd[:,0]
        # print(s1.shape, s1)
        # n = len(s1)
        # p = fft(s1)
        # nUniquePts = int(ceil((n + 1)/2.0))
        # p = abs(p[0:nUniquePts]) #absolute value provides magnitude
        yft = fft(snd)
        freq = np.linspace(0,fs/2,num=(fs/2)/(fs/len(snd)))
        # if len(snd) % 2 == 0:
        #     ydft = yft[1:len(snd)/2+1]
        # else:
        #     ydft = yft[1:floor(len(snd)/2)+1]
        ydft = yft[1:floor(len(snd)/2+1)]
        index = ydft.argmax()
        return float(freq[index])


    def compareFreq(self,freqArr,notefreq):
        for x in range(0, len(freqArr)):
            freqArr[x] = abs(freqArr[x] - notefreq)
        #index, minval = min(freqArr, key=operator.itemgetter(freqArr))
        minval = min(freqArr)
        i = freqArr.index(minval)
        return i



# print(Notes(4,5).makeFreq())
# print(Notes(4,5).makeNotes())
# print(len(Notes(4,5).makeFreq()))
# print(len(Notes(4,5).makeFreq()))
#print(norm)
#a = snd.dtype
#print(a)qedfrw
#print(sampFreq)
#print(snd)
