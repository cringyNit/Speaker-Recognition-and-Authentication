 import numpy as np
from scipy.io.wavfile import read as rd
from sklearn.mixture import GaussianMixture as GMM
from featureextraction import extract_features
import os
import Models

def testSingleaudio(testpath) :
    samplerate , audiofile = rd(testpath)
    mfcc_features = extract_features(audiofile , samplerate)
    for model in os.listdir('GMMModels/') :
        print model
        tmp = Models.retrieveModels('GMMModels/' + model)
        print tmp.score(mfcc_features)
        
testSingleaudio('cat1.wav')
