#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_policy_name_from_kind
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time
import numpy as np
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi

class my_node (Node):
    def __init__(self):
        super().__init__("Node1_name")       
        self.create_subscription(Odometry,"/odom",self.sub_call,10)
        self.get_logger().info("Node is started")
        self.file1 = open('pose.csv', 'r')
        self.Lines = self.file1.readlines()
        self.x_list=[]
        self.y_list=[]
        self.yaw_list=[]
        self.index=3
        self.counter=0

        for line in self.Lines:
            x,y,yaw=line.split(",")
            self.x_list.append(x)
            self.y_list.append(y)
            self.yaw_list.append(yaw)
            self.counter+=1

        self.x=0.0
        self.y=0.0
        self.yaw=0.0
    def euler_from_quaternion(self, quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w

        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw 
    def sub_call(self,msg):
        self.x=msg.pose.pose.position.x
        self.y=msg.pose.pose.position.y
        quant=Quaternion()
        quant.x=msg.pose.pose.orientation.x
        quant.y=msg.pose.pose.orientation.y
        quant.z=msg.pose.pose.orientation.z
        quant.w=msg.pose.pose.orientation.w
        roll,pitch,self.yaw=self.euler_from_quaternion(quant)
        
        yaw_degree_current=(self.yaw*180) / pi
        #self.get_logger().info(f"the current  x pos is {self.x} the current y pose is {self.y} and current yaw degree {yaw_degree_current}")
        #self.get_logger().info(f"the Dest  x pos is {self.x_list[self.index]} the Dest y pose is {self.y_list[self.index]} and Dest yaw degree {self.yaw_list[self.index]}")
        x_low=float(self.x_list[self.index]) - .5
        x_hight=float(self.x_list[self.index]) + .5 
        y_low=float(self.y_list[self.index]) - .5
        y_high=float(self.y_list[self.index]) + .5
        yaw_low=float(self.yaw_list[self.index]) -5 
        yaw_high=float(self.yaw_list[self.index]) +5 
        self.get_logger().info(f"the current  x pos is {self.x} the current y pose is {self.y} and current yaw degree {yaw_degree_current}")
        self.get_logger().info(f"the Dest  x pos is {self.x_list[self.index]} the Dest y pose is {self.y_list[self.index]} and Dest yaw degree {self.yaw_list[self.index]}")

        #if (((float(self.x_list[self.index]) - .5) > self.x > float(self.x_list[self.index]) +.5 ) and ((float(self.y_list[self.index]) - .5)>self.y >   (float(self.y_list[self.index]) + .5)) and ((float({self.yaw_list[self.index]}) - 5)< yaw_degree_current< (float({self.yaw_list[self.index]}) +5) )):
        '''
        if (self.x >x_low  and  self.x < x_low) and (self.y > y_low   and  self.y <y_high  ) and (yaw_degree_current > yaw_low and yaw_degree_current<yaw_high):
            self.index +=1 
            while(self.index>self.counter):
                self.get_logger().info(" i execute all position and last one is {self.x_list[self.index-1]} , {self.y_list[self.index-1]} ,{self.yaw_list[self.index]}")
        
            self.get_logger().info(" go to next on")
        '''
        if (self.x >x_low  and  self.x < x_hight) :
            self.get_logger().info("x is ok")
            if (self.y > y_low   and  self.y <y_high  ): 
                self.get_logger().info("y is ok")
                if (yaw_degree_current > yaw_low and yaw_degree_current<yaw_high):
                    self.get_logger().info("yaw is ok")
                    self.index +=1 
                    while(self.index>self.counter):
                        self.get_logger().info(" i execute all position and last one is {self.x_list[self.index-1]} , {self.y_list[self.index-1]} ,{self.yaw_list[self.index]}")
        
                    self.get_logger().info(" go to next on")

        



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()


