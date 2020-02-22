#!/usr/bin/env python
import rospy
from ros_basics.msg import customMsg


def sendData():
    #create node
    #rospy.init_node(node_name,anonymous=True)
    #setting anonymous=True means we can 
    #use the same node_name for multiple nodes
    #and work in tandem
    rospy.init_node('customSend',anonymous=True)
    #rospy.Publisher(topic_name,topic_type,queue_size )
    publisher = rospy.Publisher('Data',customMsg,queue_size = 10)
     
    #Rate of sending message
    #in Hz so time = 1/Hz
    #1 sec = 1 hz
    #2 sec = 0.5 hz and so on
    rate = rospy.Rate(1)
     
    #initialise a while loop till we receive 
    # interrupt exception 
    while not rospy.is_shutdown():

        data = customMsg()
        data.first_name = "John"
        data.last_name = "Doe"
        #print in terminal
        rospy.loginfo(data)
        #publish the data
        publisher.publish(data)
        #sleep for specified time i.e. rate
        rate.sleep()


if __name__ == "__main__":
    try:
        sendData()
    except rospy.ROSInterruptException:
        pass
    

        
