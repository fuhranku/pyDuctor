import Leap, time
from math import floor
from Leap import SwipeGesture
def  getTempo(lastFrameID, controller):
        frame = controller.frame()
        frameID = frame.id
        if not(frameID == lastFrameID):
                lastFrameID = frameID
                hands = frame.hands
                if(hands.rightmost.is_right):
                        right = hands.rightmost
                        position = floor(right.palm_position.y//25)
                        if(position > 12):
                                position = 12
                        if(position < 1):
                                position = 6
                        print(position)
                        return position
                else:
                        return 6
        else:
                return 6
