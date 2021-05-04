#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_msgs.msg import Itilab3

class my_node(Node):
    
    def __init__(self):
        super().__init__("Int_publisher")
        self.get_logger().info("node1 is running")
        self.create_timer(1/1,self.timer_call)
        self.obj_pub=self.create_publisher(Itilab3,"number",10)
        
        
      
    def timer_call(self):
        msg=Itilab3()
        self.get_logger().info(msg.name)
        self.obj_pub.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()




'''
def main(args=None):
    rclpy.init(args=args)
    node=Node("saeedBayome")
    node.get_logger().info("Node is start")
    rclpy.shutdown()

if __name__=="__main__":
    main()


'''