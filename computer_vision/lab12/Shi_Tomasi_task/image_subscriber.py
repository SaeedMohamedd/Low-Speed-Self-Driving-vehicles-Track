#!/usr/bin/env python3

import rclpy
import numpy as np
import math
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()

class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Image,"/intel_realsense_d435_depth/image_raw",self.img_cb, rclpy.qos.qos_profile_sensor_data)
        
        self.get_logger().info("subscriber is started")


        
    def img_cb(self,message):
        cv2_img = bridge.imgmsg_to_cv2(message, "bgr8")
        #cv2.imwrite('saved_img.png', cv2_img)
        cv2.imshow("cv2_img", cv2_img)
        k=cv2.waitKey(1)
        if k == 115:
        	cv2.imwrite("saved_img.png", cv2_img)

          
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()


