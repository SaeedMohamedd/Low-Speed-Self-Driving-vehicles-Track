#!/usr/bin/env python3

from math import sin, cos, pi
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile

class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        qos_profile = QoSProfile(depth=10)
        #self.create_subscription(Twist,"/cmd_vel",self.twist_call,10)
        self.create_subscription(LaserScan,"/scan",self.scan_call,10)   
        self.vel_pub=self.create_publisher(Twist,"cmd_vel",10) 
        self.get_logger().info("subscriber is started")
        self.stop_msg=Twist()
        self.stop_msg.linear.x=0.0
        self.stop_msg.linear.y=0.0
        self.stop_msg.linear.z=0.0
        self.stop_msg.angular.x=0.0
        self.stop_msg.angular.y=0.0
        self.stop_msg.angular.z=0.0
        

    def scan_call(self,msg):
        laser_data=msg.ranges
        print(laser_data.index(min(laser_data)), min(laser_data))
        if min(laser_data) < 2:
            if  laser_data.index(min(laser_data)) < 20 or  laser_data.index(min(laser_data)) > 340:
                self.vel_pub.publish(self.stop_msg)

        


  


    def scan_bag_call(self,msg):
        msg.header.stamp=self.get_clock().now().to_msg()
        self.scan_pub.publish(msg)

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()


