#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

pub = None

def callback(data):

    global pub
    move = Twist()

    front = min(data.ranges[0:10] + data.ranges[350:360])

    if front < 0.8:
        move.linear.x = 0
        move.angular.z = 0.5
    else:
        move.linear.x = 0.2
        move.angular.z = 0

    pub.publish(move)


rospy.init_node('avoid_obstacles')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()