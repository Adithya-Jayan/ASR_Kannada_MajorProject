#data augmentation

import numpy
import librosa
from scipy.io import wavfile
import random
import math

in_signal, sr = wavfile.read('hello_l.wav')
rms_input=math.sqrt(np.mean(in_signal**2))

#here generate snr as random number (what range tho?)
rms_noise=math.sqrt((rms_input**2)/(pow(10,snr/10))) #rms noise = standard deviation of noise
noise=numpy.random.random(0,rms_noise,in_signal.shape[0]) #number of data points
noisy_signal=in_signal+noise 
wavfile.write("noisy_data.wav", sr, noisy_signal)
