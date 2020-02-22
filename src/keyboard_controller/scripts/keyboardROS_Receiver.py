#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ros_basics.msg import Movement

def messageHandler(message):
    # %s string %d int %f float
    rospy.loginfo("Forward Value: %s",message.forward)
    rospy.loginfo("Backward Value: %s",message.backward)
    rospy.loginfo("Right Value: %s",message.frontRight)
    rospy.loginfo("Left Value: %s",message.frontLeft)

def receive():
    #create node
    #rospy.init_node(node_name,anonymous=True)
    #setting anonymous=True means we can 
    #use the same node_name for multiple nodes
    #and work in tandem
    rospy.init_node('receive',anonymous=True)
    #rospy.Subscriber(topic_name,topic_type,handler)
    subscriber = rospy.Subscriber('Data',Movement,messageHandler)
     
    #initialise a spin loop of rospy which exits
    rospy.spin() 
  


if __name__ == "__main__":
    try:
        receive()
    except rospy.ROSInterruptException:
        pass
    

        
