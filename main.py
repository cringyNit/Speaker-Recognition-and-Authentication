#import os
#import time
#import playsound

import GMMTesting
import GMMTraining
import sounddevice
from scipy.io.wavfile import write
from commands import getoutput as gt


def record(Name, Range, Path) :
	sr =44100
	second = 6
	for i in range(Range) : 
		record_voice=sounddevice.rec(int(second * sr),samplerate=sr,channels=2)
		sounddevice.wait()
		fname=Name+str(i+1)+".wav"
        
		write(fname,sr,record_voice)

if __name__ == "__main__":
    
    print("Select Option:\n1. Sign In\t 2.Sign Up")
    a=int(input())
    
    if(a == 1) :
        record("temp" , 1 , "")
        print "Hello " + GMMTesting.testSingleaudio("temp1.wav")
        gt("rm temp1.wav")
        
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
        GMMTraining.GMMModels('TrainingData/' , 'GMMModels')


