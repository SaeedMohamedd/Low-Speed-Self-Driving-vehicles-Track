#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from nav_msgs.msg import Path
import math
import numpy as np

class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Path,"/local_plan",self.timer_call,10)
        
        self.get_logger().info("subscriber is started")

        self.create_timer(1/1,self.timer_pub)
        self.obj_pub=self.create_publisher(String,"my_topic",10)

        self.get_logger().info("publisher ready")
        self.curv_value=0.0

    def timer_pub(self):
        msg=String()
        if self.curv_value >2 :
            msg.data=f"The robot is turning with a curvature {self.curv_value}"
                    
        if self.curv_value <1 and self.curv_value > 0 :
            msg.data="The path is straight"

    def timer_call(self,msg):
        
        pose_len=len(msg.poses)
        print(len(msg.poses))
                
        if pose_len >= 7 :
            x1=msg.poses[0].pose.position.x 
            y1=msg.poses[0].pose.position.y 
            first_orient=msg.poses[0].pose.orientation
            _,_,yaw1=self.euler_from_quaternion(first_orient)
            x2=msg.poses[int(pose_len/2)].pose.position.x 
            y2=msg.poses[int(pose_len/2)].pose.position.y
            second_orient=msg.poses[pose_len-1].pose.orientation
             
            x3=msg.poses[pose_len-1].pose.position.x  
            y3=msg.poses[pose_len-1].pose.position.y
            third_orient=msg.poses[pose_len-1].pose.orientation 
            _,_,yaw2=self.euler_from_quaternion(second_orient)
            self.curv_value=self.menger_curvature(x1,y1,x2,y2,x3,y3)
                    
            if self.curv_value >1 :
                if yaw1> 0:
                    if yaw2>yaw1:
                        self.get_logger().info(f"The robot is turning to the right with a curvature {self.curv_value}")
                    elif yaw2 <yaw1 :
                        self.get_logger().info(f"The robot is turning to the left with a curvature {self.curv_value}")
                elif yaw1 <0:
                        if yaw2>yaw1:
                            self.get_logger().info(f"The robot is turning to the left with a curvature {self.curv_value}")
                        elif yaw2 <yaw1 :
                            self.get_logger().info(f"The robot is turning to the right with a curvature {self.curv_value}")

                        
            if self.curv_value <1 and self.curv_value > 0 :
                self.get_logger().info("The path is straight")
                        
                    
            self.get_logger().info(str(self.curv_value))

    def menger_curvature(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
            
        try:
            curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))#Menger curvature 
            return curvature
        except:
            return 0 
        
    def euler_from_quaternion(self, quaternion):
        """
        Converts quaternion (w in last place) to euler roll, pitch, yaw
        quaternion = [x, y, z, w]
        Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
        """
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
                        
                

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()


