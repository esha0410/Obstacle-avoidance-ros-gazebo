#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    # 10/5 = 2
    regions = [ 
      min(min(msg.ranges[0:1]), 10),
      min(min(msg.ranges[2:3]), 10),
      min(min(msg.ranges[4:5]), 10),
      min(min(msg.ranges[6:7]), 10),
     min( min(msg.ranges[8:9]), 10),
     ]
    rospy.loginfo(regions)

def main():
    rospy.init_node('laser_readings')
    sub= rospy.Subscriber("/myrobo/laser_scan", LaserScan, clbk_laser)

    rospy.spin()

if __name__ == '__main__':
    main()