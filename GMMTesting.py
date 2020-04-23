import numpy as np
from scipy.io.wavfile import read as rd
from sklearn.mixture import GaussianMixture as GMM
from featureextraction import extract_features
import os
import Models

models=[]
models_name=[]

def GMMModels(audiopath , modeldest) :
    for folder in os.listdir(audiopath) :
        mfcc_features = np.asarray(())
        for audio in os.listdir(audiopath + folder) :
            samplerate , audiofile = rd(audiopath + folder + '/' + audio)
            tmp   = extract_features(audiofile,samplerate)
            if mfcc_features.size == 0 :
                mfcc_features = tmp
            else :
                mfcc_features = np.vstack((mfcc_features , tmp))
        
        gmm = GMM(n_components = 16, max_iter = 200, covariance_type='diag',n_init = 3)
        gmm.fit(mfcc_features)
        Models.saveModels(modeldest , gmm , folder)

def testDataSet(datasetpath,succes_rate) :
    for model in os.listdir('GMMModels/') :
        models_name.append(model)
        tmp = Models.retrieveModels('GMMModels/' + model)
        models.append(tmp)
    total_files = 0
    for folder in os.listdir(datasetpath) :
    	for audio in os.listdir(datasetpath + folder) :
    		total_files += 1
    		samplerate , audiofile = rd(datasetpath + folder + '/'+audio)
    		mfcc_features = extract_features(audiofile , samplerate)
    		max_score=-999999
    		max_model=models[0]
    		i=0
    		for model in models :
    			score = model.score(mfcc_features)
    			if score > max_score :
    				max_score = score
    				max_model = models_name[i]
    			i = i + 1
    		
    		print audio
    		print max_model
    		print max_score
    		print "---------------------------------"

    		if max_model[:len(max_model)-4]== folder:
    			succes_rate+=1
    succes_rate = (succes_rate*1.00) / total_files
    print (str((succes_rate)*100)+ "%")


testDataSet('TestingData/',0)
