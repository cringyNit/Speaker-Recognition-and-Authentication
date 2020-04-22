import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
from featureextraction import extract_features
#from sklearn.mixture import GaussianMixture as GMM
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time


sr , audio = read( 'SampleData/Aditya_16.wav')
vector = extract_features(audio , sr)

#log_likelihood = np.zeros(len(models))
gmm = 'Speakers_models/Aditya.gmm'

scores = np.array(gmm.score(vector))
