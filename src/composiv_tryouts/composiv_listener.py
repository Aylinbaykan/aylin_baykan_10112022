#!/usr/bin/env python
import rospy
from std_msgs.msg import String 

global my_data

def callback(data):
	my_data =data.data
	rospy.loginfo(rospy.get_caller_id() + "I heard %s" , my_data)

def listener():
	rospy.init_node('listener', anonymous = True)
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()
if __name__ == '__main__':
	listener()

