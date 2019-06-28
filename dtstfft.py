from scipy.io.wavfile import read
from scipy.signal import stft
import numpy as np
import pywt

scale = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B']

# Stereo audio; take only the first channel.
rate, data = read("marySongOrig.wav")
data0 = data#[:, 0]

# For wavelet transform, let the input data stream be even.
# Get rid of the first element if the amount of data is odd.
if len(data0) % 2 == 1:
    data0 = data0[1:]

# Obtain wavelet.
db1 = pywt.DiscreteContinuousWavelet('db1')

# Denoise the wave using the SureShrink method, where SURE
# is Stein's Unbiased Risk Estimate. Use stationary wavelet
# transform.
# Take the inner product of the original audio with the
# Daubechies wavelet db1. In the time-freq-domain, use soft-
# thresholding to reduce frequencies below a threshold,
# then apply Inverse Stationary Wavelet Transform to get the
# denoised signal. Assume noise is white Gaussian.
output = pywt.swt(data0, db1)

# Measure the threshold. 
# Here we use Donoho and Johnstone's method to estimate the
# noise level σ. This is based on the last level of the 
# detail coefficients, according to the mean absolute
# deviation. The formula is median({|d_J-1, k|}) / 0.6745
# where k is a power of 2 according to SWT and d_J-1 is
# the downsampled next layer, through median normalization
def measure_threshold(timefreq_coeffs):
    thresholds = []
    for cA, cD in timefreq_coeffs:
        lmbda = np.sqrt(2 * np.log(len(cD)))
        σ = np.median(np.abs(cD - np.median(cD))) / 0.6745
        σ *= 0.64 # Hyperparameter
        thresholds.append(lmbda * σ)

    return thresholds

thresh = measure_threshold(output)

# Compute the threshold. Apply soft-thresholding
def apply_threshold(timefreq_coeffs, thresholds):
    for i, (cA, cD) in enumerate(timefreq_coeffs):
        pywt.threshold(cD, thresholds[i], mode='soft')
        timefreq_coeffs[i] = cA, cD

apply_threshold(output, thresh)

# Revert back to the time-domain.
data0 = pywt.iswt(output, db1)

# Compute the Discrete-Time Short-Time Fourier Transform 
# of the data. Equivalent to computing the DFT of every
# time delta of the audio file after applying a window
# function. Returns sample frequencies (f), list of sampled
# times (t), and the DTSTFT matrix.
f, t, Zxx = stft(data0, fs=rate, nfft=rate, noverlap=None)

# Compute the magnitude to turn each DFT bin into
# frequencies. Simplification by taking the largest
# frequency as *the* frequency.
magnitude = np.abs(Zxx)

frequencies = []
for dft_bin in magnitude.T:
    i = np.argmax(dft_bin[1:f.shape[0]//2])
    frequencies.append(i * rate / (f.shape[0]))

# Transforming each frequency into half-steps as compared
# to middle C, listed at 261.626 Hz. Get rid of infinities.
# The very first component at index zero is the DC component.
# Taking the logarithm will turn this into negative infinity.
C4 = 261.626
semitones = np.array(list(map(lambda x: round(12 * np.log(x / C4) / np.log(2)), frequencies)))
semitones = np.delete(semitones, np.where(np.isinf(semitones)))
notes = np.array(list(map(lambda x: scale[int(x % len(scale))], semitones)))

print(notes)
