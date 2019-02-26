#!/usr/bin/env python
import rospy, tf, random
import sys
import os
from gazebo_msgs.srv import DeleteModel, SpawnModel
from geometry_msgs.msg import Pose

rospy.init_node('spawn_brick',log_level=rospy.INFO)

quaternion = tf.transformations.quaternion_from_euler(0,0,1.570796)

initial_pose = Pose()
initial_pose.position.x = 0.48 #tune this ..
initial_pose.position.y = 0.5
initial_pose.position.z = 0.2
initial_pose.orientation.x = quaternion[0]
initial_pose.orientation.y = quaternion[1]
initial_pose.orientation.z = quaternion[2]
initial_pose.orientation.w = quaternion[3]

#Hopefully should work on everyones computer if not directly change this
file = os.path.expanduser('~/.gazebo/models/Brick/model-1_4.sdf')
#file = "ENTER ABS PATH TO THE model-1_4 file on your computer"
f = open(file, "r")
sdff = f.read()

rospy.wait_for_service('gazebo/spawn_sdf_model')
spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)


def gen_brick_handler(req):
    i = random.randint(1,500)
    spawn_model_prox("brick_"+str(i), sdff, "brick_"+str(i), initial_pose, "world")
    resp = TriggerResponse()
    return resp

#CODE FOR MAKING this node into a servicec
from std_srvs.srv import Trigger, TriggerResponse
gen_brick_s = rospy.Service('gen_brick', Trigger, gen_brick_handler)

rospy.spin()
