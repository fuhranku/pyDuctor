# pyDuctor
pyDuctor is a project started by Orens Xhagolli (RIT), Louis Cruz (Cornell), Frank Chan (Cornell).

It allows you to control various features of .wav audio files through a LeapMotion device.

#What can you do with pyDuctor?
Through the LeapMotion device, you can control the volume of your computer in instant speed, providing a smooth control over the up and down beats. Also, you can control the speed and consequently the pitch of a particular audio section.

#Outside dependencies
- LeapMotion SDK (Python)
- Python 2.7 (This comes as a result of the LeapMotion SDK :/)
    Python 2.7 Installation Instructions (Windows Only):
    1. Download Python 2.7 from <a href="http://www.python.org">python.org</a>
    2. Follow Python 2.7 Installation Instructions (If you need to use these instructions, you should probably use defaults to avoid adding to the confusion.)
    3. (THIS IS IMPORTANT) Make sure to set the paths:
        - Open CMD as Admin
        - Type "SET PATH=C:\Python27\;%PATH%"
        - And "SET PATH=C:\Python27\Scripts;%PATH%"
    This allows you to run python and pip from command line through a command like: "python"
        
- MIT CSAIL pyAudio
    pyAudio Installation instructions (Cannot be found on pip directly):
    1. Make sure you followed the installation instructions for Python 2.7 correctly
    2. Go to a Terminal(Unix-based)/CMD(Windows - Run as admin).
    3. Type "pip install wheel"
    4. Go <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio">here</a>.
    5. Download "PyAudio‑0.2.8‑cp27‑none‑win32.whl" or "PyAudio‑0.2.8‑cp27‑none‑win_amd64.whl"
    6. Back to the terminal, type "pip install (file address)" where (file address) is the address of the file that you just downloaded.
- Other (System Dependent)

We will try to provide maximum support for making sure you acquire all dependencies.
Note: Wherever there are "", they are just meant to show that that's text you need to type, DO NOT type the quotation marks.