#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from nav_msgs.msg import Path
import math

class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Path,"/plan",self.timer_call,10)
        
        self.get_logger().info("subscriber is started")

        self.create_timer(1/1,self.timer_pub)
        self.obj_pub=self.create_publisher(String,"my_topic",10)

        self.get_logger().info("publisher ready")
        self.curv_value=0.0

    def menger_curvature(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
            
        curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))#Menger curvature 
        return curvature
      


    def timer_pub(self):
        msg=String()
        if self.curv_value >2 :
            msg.data=f"The robot is turning with a curvature {self.curv_value}"
                
        if self.curv_value <1 and self.curv_value > 0 :
            msg.data="The path is straight"

    def timer_call(self,msg):
        pose_len=len(msg.poses)
        if pose_len >= 11 :
            x1=msg.poses[0].pose.position.x 
            y1=msg.poses[0].pose.position.y 
            x2=msg.poses[5].pose.position.x 
            y2=msg.poses[5].pose.position.y 
            x3=msg.poses[10].pose.position.x  
            y3=msg.poses[10].pose.position.y 
            self.curv_value=self.menger_curvature(x1,y1,x2,y2,x3,y3)
            
            if self.curv_value >2 :
                self.get_logger().info(f"The robot is turning with a curvature {self.curv_value}")
                
            if self.curv_value <1 and self.curv_value > 0 :
                self.get_logger().info("The path is straight")
                
            
            self.get_logger().info(str(self.curv_value))

        


def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()


