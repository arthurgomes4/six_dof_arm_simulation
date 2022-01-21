#! /usr/bin/env python

import rospy
import sys
import time
from std_msgs.msg import Float64

def deg2rad(d):
    return d*3.142/180

def write(obj,angle):
    msg = Float64()

    while obj.get_num_connections() == 0:
        pass
    msg.data = deg2rad(angle)
    obj.publish(msg)

if __name__ == '__main__':
    print('starting')

    jp = [float(x) for x in sys.argv[1:]]
    rospy.init_node('joint_pos_pub')
    j1 = rospy.Publisher('/six_dof_v2/j1_position_controller/command', Float64, queue_size=1)
    j2 = rospy.Publisher('/six_dof_v2/j2_position_controller/command', Float64, queue_size=1)
    j3 = rospy.Publisher('/six_dof_v2/j3_position_controller/command', Float64, queue_size=1)
    j4 = rospy.Publisher('/six_dof_v2/j4_position_controller/command', Float64, queue_size=1)
    j5 = rospy.Publisher('/six_dof_v2/j5_position_controller/command', Float64, queue_size=1)
    # j6 = rospy.Publisher('/six_dof_v2/j6_position_controller/command', Float64, queue_size=1)

    joints = [j1, j2, j3, j4, j5]
    
    for i in range(5):
        write(joints[i], jp[i])
    
    print('shutting down')
else:
    pass