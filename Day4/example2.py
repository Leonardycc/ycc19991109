import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
     
def callback(move):
        if(move.linear.x>0):
          rospy.loginfo("I am moving positively")
        if (move.linear. x<0):
          rospy.loginfo("I am moving negatively")
        if (move.angular. z>0):
          rospy.loginfo("I am moving leftward")
        if (move.angular. z<0):
          rospy.loginfo("I am moving rightward")

def listener():
   
         rospy.init_node('listener', anonymous=True)
     
         rospy.Subscriber("cmd_vel", Twist, callback)
     
         # spin() simply keeps python from exiting until this node is stopped
         rospy.spin()
     
if __name__ == '__main__':
         listener()
