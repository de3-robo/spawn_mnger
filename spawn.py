#!/usr/bin/env python
import rospy, tf, random
import sys
import os
from gazebo_msgs.srv import DeleteModel, SpawnModel # for Gazebo
from geometry_msgs.msg import Pose # for object orientation

#initialising node in which the service resides
rospy.init_node('spawn_brick',log_level=rospy.INFO)

quaternion = tf.transformations.quaternion_from_euler(0,0,1.570796)
#defining brick orientation, which will be translated into quarternion

# defining pose of object to be spawned
initial_pose = Pose()
initial_pose.position.x = 0.5
initial_pose.position.y = 0.5
initial_pose.position.z = 0.2
initial_pose.orientation.x = quaternion[0]
initial_pose.orientation.y = quaternion[1]
initial_pose.orientation.z = quaternion[2]
initial_pose.orientation.w = quaternion[3]

# Finding the model file to be spawned
file = os.path.expanduser('~/.gazebo/models/Brick/model-1_4.sdf')
f = open(file, "r")
sdff = f.read()

rospy.wait_for_service('gazebo/spawn_sdf_model')
spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)

# function that defines the service gen_brick
def gen_brick_handler(req):
    i = random.randint(1,5000)
    spawn_model_prox("brick_"+str(i), sdff, "brick_"+str(i), initial_pose, "world")
    resp = TriggerResponse()
    return resp

#CODE FOR MAKING this node into a service
from std_srvs.srv import Trigger, TriggerResponse
gen_brick_s = rospy.Service('gen_brick', Trigger, gen_brick_handler)

19  # spin() simply keeps python from exiting until this node is stopped
rospy.spin()