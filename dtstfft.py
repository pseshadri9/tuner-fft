from scipy.io.wavfile import read
from scipy.signal import stft
import numpy as np

scale = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B']

# Stereo audio; take only the first channel.
rate, data = read("GottErhalteFranzDenKaiser.wav")
data0 = data[:, 0]

# Compute the Discrete-Time Short-Time Fourier Transform 
# of the data. Equivalent to computing the DFT of every
# time delta of the audio file after applying a window
# function. Returns sample frequencies (f), list of sampled
# times (t), and the DTSTFT matrix.
f, t, Zxx = stft(data0, fs=2.0, window='blackmanharris', noverlap=None)

# Compute the magnitude to turn each DFT bin into
# frequencies. Simplification by taking the largest
# frequency as *the* frequency.
magnitude = np.abs(Zxx)

frequencies = []
for dft_bin in magnitude.T:
    i = np.argmax(dft_bin)
    frequencies.append(list(i * rate / f.shape)[0])

# Transforming each frequency into half-steps as compared
# to middle C, listed at 261.626 Hz. Get rid of infinities.
# The very first component at index zero is the DC component.
# Taking the logarithm will turn this into negative infinity.
C = 261.626
semitones = np.array(list(map(lambda x: round(12 * np.log(x / C) / np.log(2)), frequencies)))
semitones = np.delete(semitones, np.where(np.isinf(semitones)))
notes = np.array(list(map(lambda x: scale[int(x % len(scale))], semitones)))

print(notes)
