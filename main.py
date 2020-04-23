import os
import time
import playsound
import sounddevice
from scipy.io.wavfile import write


print("Select Option:\n1. Sign In\t 2.Sign Up")
a=input();
a=int(a)
if(a!=1) :
	print(a)
else:#Sign Up

	print("We will take 5 sample. Press 1 to start recording")
	input()
	sr=44100
	second=6
	for i in range(5):
		print(str(i)+" recording....")
		record_voice=sounddevice.rec(int(second * sr),samplerate=sr,channels=2)
		sounddevice.wait()
		fname="record"+str(i)+".wav"
		write(fname,sr,record_voice)
		print(str(i)+" recognition done")


def record(Name, Range, Path) :
	sr =44100
	second = 6
	for i in range(Range) : 
		record_voice=sounddevice.rec(int(second * sr),samplerate=sr,channels=2)
		sounddevice.wait()

		fname=Name+str("_pass")+".wav"

		write(fname,sr,record_voice)