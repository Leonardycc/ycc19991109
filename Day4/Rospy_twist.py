import rospy
from geometry_msgs.msg import Twist

xue_pub=rospy.Publisher('/cmd_vel', Twist,queue_size=10)
rospy.init_node('xuehenxiaowugui')
xuegai_rate=rospy.Rate(5)

while not rospy.is_shutdown():
    xue_cmd=Twist()
    xue_cmd.linear.x=0.1
    xue_cmd.angular.z=0.2
  
    xue_pub.publish(xue_cmd)

    xuegai_rate.sleep()
