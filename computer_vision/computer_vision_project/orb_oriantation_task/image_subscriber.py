#!/usr/bin/env python3

from ast import Num
from PIL.Image import NONE
from matplotlib.pyplot import gray, imread
from numpy.core.fromnumeric import shape
import rclpy
import numpy as np
import math
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import time
import math

# Instantiate CvBridge
bridge = CvBridge()
#img2=NONE

class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Image,"/intel_realsense_d435_depth/image_raw",self.img_cb, rclpy.qos.qos_profile_sensor_data)
        
        self.get_logger().info("subscriber is started")
        self.first=0
        self.d_x=0
        self.d_y=0
        self.img1=None
        self.img2=None


        
    def img_cb(self,message):
        self.d_x=0
        self.d_y=0
        #cv2_img = bridge.imgmsg_to_cv2(message, "bgr8")
        #cv2.imwrite('saved_img.png', cv2_img)
        #cv2.imshow("cv2_img", cv2_img)
        #k=cv2.waitKey(1)
        # 115 s ,116 t
        #if k == 115:
        #	cv2.imwrite("saved_img1.png", cv2_img)
        #if k == 116:
        #	cv2.imwrite("saved_img2.png", cv2_img)
        if self.first ==0 :
            fram1 = bridge.imgmsg_to_cv2(message, "bgr8")
            self.img1 = cv2.cvtColor(fram1, cv2.COLOR_BGR2GRAY)     
            self.first=1
            print("first")
            return
        print("DO")
        self.img2=self.img1.copy()
        fram1 = bridge.imgmsg_to_cv2(message, "bgr8")
        self.img1 = cv2.cvtColor(fram1, cv2.COLOR_BGR2GRAY)
        cv2.imshow("cv2_img", self.img1)
        k=cv2.waitKey(1)



        #sift
        orb = cv2.ORB_create()
        t0 = time.time()
        keypoints_1, descriptors_1 = orb.detectAndCompute(self.img1, None)
        keypoints_2, descriptors_2 = orb.detectAndCompute(self.img2, None)

        #feature matching
        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
        if descriptors_1 is not None and descriptors_2 is not None:
            matches = bf.match(descriptors_1, descriptors_2)

            matches = sorted(matches, key = lambda x:x.distance)
            list_kp1 = [keypoints_1[mat.queryIdx].pt for mat in matches] 
            list_kp2 = [keypoints_2[mat.trainIdx].pt for mat in matches]
            
            img3 = cv2.drawMatches(self.img1, keypoints_1, self.img2, keypoints_2, matches, self.img2, flags=2)
            cv2.imshow("matching", img3)
            k=cv2.waitKey(1)

            print ("Execution time: " + str(time.time() - t0))
            print(len(list_kp1),len(list_kp2))
            if len(matches)>0 and len(list_kp1)>0 and len(list_kp2):
                print("a pose")
                i=0

                len_k1=len(list_kp1)
                print(len_k1)
                while i< len_k1:
                    #print(list_kp1[i][0]-list_kp2[i][0])
                    self.d_x+=list_kp1[i][0]-list_kp2[i][0]
                    self.d_y+=list_kp1[i][1]-list_kp2[i][1]
                    #print(self.d_x,self.d_y)
                    i+=1

                
                d_x=int(self.d_x/len_k1) *-5
                d_y=int(self.d_y/len_k1) 
                print(d_x,d_y)
                arrow_img=np.copy(self.img1)
                cv2.arrowedLine(arrow_img,(160,120),(160+d_x,120+d_y),(255,0,0),8);
                cv2.imshow("line", arrow_img)
                
            
        '''
        if len(matches)>0 and len(keypoints_1)>0 and len(keypoints_2):
            i=0
            d_x=[]
            d_y=[]
            t_x=0
            t_y=0
            a_x1=0
            a_y1=0
            a_x2=0
            a_y2=0
            len_k1=len(keypoints_1)-1
            len_k2=len(keypoints_2)-1
            if len_k1>len_k2:
                len_k1=len_k2
            while i < len_k1:
                #print(keypoints_2[i].pt[0]-keypoints_1[i].pt[0],keypoints_2[i].pt[1]-keypoints_1[i].pt[1],math.atan(keypoints_1[i].pt[0]-keypoints_2[i].pt[0]/keypoints_1[i].pt[1]-keypoints_2[i].pt[1]))
                d_x.append(keypoints_2[i].pt[0]-keypoints_1[i].pt[0])
                d_y.append(keypoints_2[i].pt[1]-keypoints_1[i].pt[1])
                t_x+=keypoints_2[i].pt[0]-keypoints_1[i].pt[0]
                t_y+=keypoints_2[i].pt[1]-keypoints_1[i].pt[1]
                a_x1+=keypoints_1[i].pt[0]
                a_y1+=keypoints_1[i].pt[1]
                a_x2+=keypoints_2[i].pt[0]
                a_y2+=keypoints_2[i].pt[1]
                i+=1
            if len_k1==0:
                len_k1=1
            f_x=t_x/len_k1
            f_y=t_y/len_k1

            print("average the each point",a_x1/len_k1,a_y1/len_k1,a_x2/len_k1,a_y2/len_k1)
            x1=int(a_x1/len_k1)
            y1=int(a_y1/len_k1)
            x2=int(a_x2/len_k1)
            y2=int(a_y2/len_k1)
            cv2.arrowedLine(img1,(160,120),(160+x2,120+y2),(255,0,0),8);
            cv2.imshow("line", img1)
            print(f_x,f_y)
            if f_x >0:
                print("right")
            else:
                print("left")

            if f_y >0:
                print("down")
            else:
                print("Up")

            '''







          
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()


