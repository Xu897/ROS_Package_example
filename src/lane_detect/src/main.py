import rospy
import cv2
from cv_bridge import CvBridge

TEAM="Team"


def callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    cv2.imshow("View", cv_image)

rospy.init_node('application')
# rospy.Subscriber(TEAM + "_image", 1, callback)
rospy.spin()
