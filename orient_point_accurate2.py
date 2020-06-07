#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Point
from tf.transformations import euler_from_quaternion
from math import atan2


x1 = 0.0
y1 = 0.0
theta = 0.0

def newod(msg):
	global x1 
	global y1
	global theta
	
	x1 = msg.pose.pose.position.x
	y1 = msg.pose.pose.position.y
	
	rot = msg.pose.pose.orientation
	(roll,pitch,theta)= euler_from_quaternion([rot.x,rot.y,rot.z,rot.w])
	

rospy.init_node('coordinate')

sub = rospy.Subscriber('/odom', Odometry, newod)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

mov= Twist()
r = rospy.Rate(4)
goal = Point()


while not rospy.is_shutdown():
	goal.x= input('x')
	goal.y= input('y')

	while not rospy.is_shutdown():
		inc_x=goal.x-x1
		inc_y=goal.y-y1
		goal_angle= atan2 (inc_y, inc_x)
			
	
  
		while not rospy.is_shutdown():	
			if goal_angle - theta > 0.1:
			
				mov.angular.z = 0.3
				mov.linear.x = 0.0
			else :
				mov.linear.x = 0.5
				mov.angular.z = 0.0
				break				
		 	pub.publish(mov)
			r.sleep()
	
  
  
  		while not rospy.is_shutdown():	
			if goal_angle - theta < -0.1:
				
				mov.angular.z = -0.3
				mov.linear.x = 0.0
			else :
				mov.linear.x = 0.5
				mov.angular.z = 0.0
				break
			pub.publish(mov)
			r.sleep()	
		
  		if x1>=goal.x and y1>=goal.y:
    			print('reached')
      			break

		pub.publish(mov)
		r.sleep()
pub.publish(mov)
r.sleep()
