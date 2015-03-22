"""
    :file:           tracker.py
    :author(s):      Louis Cruz, Frank Chan, Orens Xhagolli
    :description:    Module that contains functions that poll the LeapMotion device
"""

import Leap  #LeapMotion module
import math


def get_hand(controller, hand, log=False):
    """                 Hand handler.
    :param controller:  (Leap.Controller()) A Leap.Controller() instance to be passed.
    :param log:         (Boolean) Do you wish to keep a log of the function?
    :return:            (int) An integer from 1-12 representing the height of the hand detected.
    """
    hands = controller.frame().hands
    if hands.rightmost.is_right and hand is 'Right':
        position = math.floor(hands.rightmost.palm_position.y//25)
    elif hands.leftmost.is_left and hand is 'Left':
        position = math.floor(hands.leftmost.palm_position.y//25)
    else:
        if log:
            print(hand + " hand not detected, normal speed assumed.")
        return 6
    if log:
        print(hand + " detected, height: "+ str(position)+'.')
    if position > 12:
        return 12
    elif position < 1:
        return 6
    else:
        return position
