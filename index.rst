=========================================
Documentation on spawn_mnger ROS package
=========================================

The main purpose of the 'spawn_mnger' *ROS package* is to interface with Gazebo, and spawn objects within
Gazebo during a simulation. Running this code would be more practical than using the 'drag and drop'
interface within Gazebo, as during simulations spawning can be automated at pre-determined locations,
which is especially applicable for having a repeatable 'brick-pickup' procedure in this project.

'spawn.py'_ contains the main code, and defines the ROS service that is called in the 'arm_master_main.py'_ main loop.

Setup
----------

The ROS services that communicate with Gazebo are the following:


   .. literalinclude:: spawn.py
      :lines: 5-6

From ''geometry_msgs'', the message type ''Pose()'' is also required: this is understood by Gazebo as to in what pose
the object needs to be spawned. Whilst it takes in normal (x,y,z) co-ordinates for translation, the
orientation values are different, which will be covered later.

We then initiate a node named ''spawn_brick'', which will be the node in which the latter defined service
resides on.

Defining object pose
---------------------

   .. literalinclude:: spawn.py
      :lines: 14-21

''Pose()'' takes in quaternion instead of *conventional* (roll, pitch, yaw) Euler angles. Therefore, a
conversion is required, which is conveniently provided by a function within ''tf''.

Afterwards, ''initial_pose'' is defined as a ''Pose()'' type, and the translation and translated
orientation values are written in. **These values should be the same as that within the ''get_pick_loc()''
service defined within ''brick_manager_server.py'' inside the ''arm_master'' ROS package.**

The function ''gen_brick_handler()'' takes all the pre-defined pose and spawn instructions and does the
actual spawning in Gazebo. Each object requires a unique ID, therefore a random integer is appended
to ''brick_''.

Finally, the function defined is referenced to be called as a ROS service named ''gen_brick''.