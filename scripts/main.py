"""
    Author: Orens Xhagolli
    Description: pyDuctor allows you to control various features of .wav audio
    files through a LeapMotion device. 
"""

#Built-in Python imports
import wave, os
from subprocess import Popen

#Python Audio Auxiliary Library - MIT CSAIL pyAudio
import pyaudio

#The LeapMotion API
import Leap

#pyDuctor Modules
import trackPointer
import Left

#Variables
def CHUNK():
    return 4096

devnull = open(os.devnull, 'wb')

Popen(['C:\Program Files (x86)\Leap Motion\Core Services\VisualizerApp.exe'], stdout=devnull, stderr=devnull)

controller = Leap.Controller()

wv = wave.open("tdfw.wav", "rb")

p = pyaudio.PyAudio()

frames_played = 0

data = wv.readframes(CHUNK())
frm = 0
rt = wv.getframerate()

if(controller.is_connected):
    rt = int(trackPointer.getTempo(frames_played, controller)* wv.getframerate()//6)
stream = p.open(format = p.get_format_from_width(wv.getsampwidth()),
                channels = wv.getnchannels(),
                rate = rt,
                output=True)
Popen(['nircmd.exe', 'setsysvolume', str(int(Left.getPitch(frm, controller)*65535/12))], stdout=devnull, stderr=devnull)
print(rt)

while data != '':
    Popen(['nircmd.exe', 'setsysvolume', str(int(Left.getPitch(frm, controller)*65535/12))], stdout=devnull, stderr=devnull)
    temp = rt
    if(controller.is_connected):
        temp = int(trackPointer.getTempo(frames_played, controller) * wv.getframerate()//6)
        print(temp)
    if temp != rt:
        rt = temp
        stream = p.open(format = p.get_format_from_width(wv.getsampwidth()),
                channels = wv.getnchannels(),
                rate = rt,
                output=True)
    
    frames_played += CHUNK()
    stream.write(data)
    data = wv.readframes(CHUNK())

stream.stop_stream()
stream.close()

p.terminate()

print(str(frames_played))
print("success!")
