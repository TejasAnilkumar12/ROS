#!/usr/bin/env python
import rospy
from pynput.keyboard import Key, Listener
from std_msgs.msg import String
from ros_basics.msg import Movement

FRCOMBINATIONS = [
    {Key.up, Key.right}
    
]

FLCOMBINATIONS = [
    {Key.up,Key.left}
    
]


BRCOMBINATIONS = [
    {Key.down, Key.right}
    
]

BLCOMBINATIONS = [
    {Key.down, Key.left}
    
]


# The currently active modifiers
current = set()

# globals
Message = "null"
data = Movement()

# define key press event callback
def on_press(key):
    global Message
    if any([key in COMBO for COMBO in FRCOMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in FRCOMBINATIONS):
            print("forward right")
            data.forward = True
            data.frontRight = True
            data.backRight = False
    if any([key in COMBO for COMBO in FLCOMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in FLCOMBINATIONS):
            print("forward left")
            data.forward = True
            data.frontLeft = True
            data.backLeft = False
    if any([key in COMBO for COMBO in BRCOMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in BRCOMBINATIONS):
            print("backward right")
            data.backward = True
            data.backRight = True
            data.frontRight = False
    if any([key in COMBO for COMBO in BLCOMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in BLCOMBINATIONS):
            print("backward left")
            data.backward = True
            data.backLeft = True
            data.frontLeft = False
    
    if(key==Key.up):
        print("forward")
        data.forward = True
    elif(key==Key.down):
        print("backward")
        data.backward = True
    elif(key==Key.right):
        print("Right")
        data.frontRight = True
    elif(key==Key.left):
        print("Left")
        data.frontLeft = True
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    Message = k

# define key release event callback
def on_release(key):
    global Message
    data.forward = False
    data.backward = False
    data.frontRight = False
    data.frontLeft = False
    data.backRight = False
    data.backLeft = False
    if any([key in COMBO for COMBO in FRCOMBINATIONS]):
        current.remove(key)
    elif any([key in COMBO for COMBO in FLCOMBINATIONS]):
        current.remove(key)
    elif any([key in COMBO for COMBO in BRCOMBINATIONS]):
        current.remove(key)
    elif any([key in COMBO for COMBO in BLCOMBINATIONS]):
        current.remove(key)
    Message = "null"
    # stop on PAUSE
    if key == Key.pause:
        print("quit on PAUSE")
        return False


# main section
if __name__ == "__main__":
    # setup ros publisher
    pub = rospy.Publisher('Data', Movement, queue_size=10) # name of topic: /ctrl_cmd
    rospy.init_node('COntrol', anonymous=True) # name of node: /keyboard_input
    rate = rospy.Rate(10) # publish messages at 10Hz

    # setup keyboard listener
    listener = Listener(on_press=on_press, on_release=on_release, suppress=False)
    listener.start()

    # MAIN LOOP
    # endlessly react on keyboard events and send appropriate messages
    while listener.running and not rospy.is_shutdown():
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()
