import Leap
from math import floor

def getPitch(lastFrameID, controller):

        frame = controller.frame()
        frameID = frame.id
        if not(frameID == lastFrameID):
                lastFrameID = frameID
                hands = frame.hands
                if(hands.leftmost.is_left):
                        left = hands.leftmost
                        position = floor(left.palm_position.y//25)
                        if(position > 12):
                                position = 12
                        if(position < 1):
                                position = 1
                        return position
                else:
                        return 6
        else:
                return 6
