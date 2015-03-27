"""
    Author: Orens Xhagolli
    Description: pyDuctor allows you to control various features of .wav audio
    files through a LeapMotion device. 
"""

#Built-in Python imports
import wave
import os
import platform
from subprocess import Popen

#Python Audio Auxiliary Library - MIT CSAIL pyAudio
import pyaudio

#The LeapMotion API
import Leap

#pyDuctor Modules
import tracker

#Variables
CHUNK = 4096


def simulator(devnull, log=False):
    """         Runs the LeapMotion Hand Simulator
    :param      operating_system: String that represents the operating system version
    :return:    None
    """
    if log:
        print("pyDuctor - Loading Visualizer on:", platform.system())
    if "Windows" in platform.system():
        Popen(['C:\Program Files (x86)\Leap Motion\Core Services\VisualizerApp.exe'],
              stdout=devnull,
              stderr=devnull)
    else:
        pass

def set_volume(volume, devnull, log=False):
    """             Sets the volume of the computer to the specified parameter
    :param volume:  Value from 1-12 to set the volume
    :return:        None
    """
    if log:
        print("Volume level:", str(volume))
    Popen(['nircmd.exe', 'setsysvolume', str(volume*5461)],
          stdout=devnull,
          stderr=devnull)


def wave_obj(filename):
    """         Opens a given .wav file
    :param      filename: The name of the file to open.
    :return:    The wave object.
    """
    return wave.open(filename, "rb")


def main(filename, log=False, simulate=False):
    """                 The main function
    :param filename:    The name of file to open
    :param log:         Should I keep a log?
    :param simulate:    Do you want the LeapMotion simulator?
    :return:            None
    """
    devnull = open(os.devnull, 'wb')  #Used to Launch Programs Asynchronously
    if simulate:
        simulator(devnull, log)
    controller = Leap.Controller()
    controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
    wv = wave_obj(filename)
    p = pyaudio.PyAudio()
    data = wv.readframes(CHUNK)
    tempo = wv.getframerate()
    volume = 0
    if controller.is_connected:
        tempo = int(tracker.get_hand(controller, "Right", log) * wv.getframerate() // 6)
        volume = tracker.get_hand(controller, "Left", log)
        set_volume(volume, devnull, log)
    stream = p.open(format=p.get_format_from_width(wv.getsampwidth()),
                    channels=wv.getnchannels(),
                    rate=tempo,
                    output=True)

    while data != '':
        prev_tempo = tempo
        prev_volume = volume
        if controller.is_connected:
            tempo = int(tracker.get_hand(controller, "Right", log) * wv.getframerate() // 6)
            volume = tracker.get_hand(controller, "Left", log)
        if tempo != prev_tempo:
            stream = p.open(format=p.get_format_from_width(wv.getsampwidth()),
                            channels=wv.getnchannels(),
                            rate=tempo,
                            output=True)
        if volume != prev_volume:
            set_volume(volume, devnull, log)
        stream.write(data)
        data = wv.readframes(CHUNK)
    stream.stop_stream()
    stream.close()

    p.terminate()

if __name__ == '__main__':
    main("czardas.wav")
