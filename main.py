#import os
#import time
#import playsound

import GMMTesting
import GMMTraining
import sounddevice
from scipy.io.wavfile import write
from commands import getoutput as gt
import recognition
import preprocessing

threshold =  0.6
def record(Name, Range, Path) :
	sr =44100
	second = 6
	for i in range(Range) : 
		record_voice=sounddevice.rec(int(second * sr),samplerate=sr,channels=2)
		sounddevice.wait()
		fname=Name+str(i+1)+".wav"
        
		write(fname,sr,record_voice)

if __name__ == "__main__":
    
    print("Select Option:\n1. Sign In\t 2.Sign Up\t 3. Change Password")
    a=int(input())
    
    if(a == 1) :
        print "press 1 to give passcode"
        input()
        record("temp" , 1 , "")
        name = GMMTesting.testSingleaudio("temp1.wav")
        preprocessing.start("temp1.wav")


        corr , offset  = recognition.start('temp1.wav'  , "PasswordData/"+name+"/"+name+"1.wav")
        if corr > threshold :
            print "Hello " + name
        else :
            print name
            print "Not Authenticated. Try Again!"
        gt("rm temp1.wav")
        #authentication to be added
        
        
    elif (a == 2) :
        print("Enter your Name : ")
        name = raw_input()
        path = "TrainingData/" + name
        gt("mkdir %s" %(path))
        
        print("We will take 5 sample. Press 1 to start recording")
        input()
        
        record(name , 5 , path)
        
        for i in range(5) :
            fname=name+str(i+1)+".wav"
            gt("mv %s %s" %(fname , path))        
        # GMMTraining.GMMModels('TrainingData/' , 'GMMModels')
        GMMTraining.singleModelTraining(path,'GMMModels')
        print "press 1 to give passcode"
        input()
        passpath = "PasswordData/"+name
        gt("mkdir %s" %(passpath))
        
        #saving passcord after preprocessing
        record(name,1,passpath)
        preprocessing.start(name+"1.wav")
        gt("mv %s %s" %(name+"1.wav" , passpath))  

    elif a==3:
        print("Enter your Name : ")
        name = raw_input()
        passpath = "PasswordData/"+name

        record(name,1,passpath)
        preprocessing.start(name+"1.wav")
        gt("mv %s %s" %(name+"1.wav" , passpath))  


