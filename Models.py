import cPickle


def saveModels(path , model , name) :
    path = path + '/' + name + '.gmm'
    cPickle.dump(model , open(path , 'w'))
    
    print 'Saved for ' + name
    
def retrieveModels(modelname) :
    return cPickle.load(open(modelname , 'r'))
    