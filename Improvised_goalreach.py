#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Point
from tf.transformations import euler_from_quaternion
from math import atan2, sqrt

x1 = 0.0
y1 = 0.0
theta = 0.0

points = [[2,2], [0,5]]

def newod(msg):
	global x1 
	global y1
	global theta
	
	x1 = msg.pose.pose.position.x
	y1 = msg.pose.pose.position.y
	
	rot = msg.pose.pose.orientation
	(roll,pitch,theta)= euler_from_quaternion([rot.x,rot.y,rot.z,rot.w])
  
  
  
def linear(x, y):
	r = rospy.Rate(4)
	
	goal = Point()
	goal.x= x
	goal.y= y
    
	while not rospy.is_shutdown():
  		
 		inc_x = goal.x-x1
   		inc_y = goal.y-y1
    
   		goal_angle= atan2 (inc_y, inc_x)


		dist= sqrt( (goal.x-x1)**2 + (goal.x-x1)**2 )
		mov.angular.z = 2 * (goal_angle-theta)
		mov.linear.x = 0.5 * dist
		print("dist is", dist)
        	if dist < 0.2:
        		break			
		pub.publish(mov)
		r.sleep()

        
        
        
def rotation(x, y):    
   	r = rospy.Rate(4)
    
	while not rospy.is_shutdown():
      		goal.x = x
        	goal.y = y
		inc_x = goal.x-x1
		inc_y = goal.y-y1
		goal_angle= atan2 (inc_y, inc_x)
        	mov.angular.z = 0.7 * (goal_angle-theta)
		mov.linear.x = 0
		print ("Anglediff", goal_angle, "-",theta)	      		
		if abs(goal_angle-theta) < 0.05:
      			break			
     		pub.publish(mov)
     		r.sleep()
	

rospy.init_node('coordinate')
sub = rospy.Subscriber('/odom', Odometry, newod)

pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

print "Node initiated"
goal = Point()
mov= Twist()

rotation(2,2)
linear(2,2)


rotation(0,5)
linear(0,5)


