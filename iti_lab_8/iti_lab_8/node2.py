#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class my_node(Node):
    def __init__(self):
        super().__init__("Node2")
        self.create_subscription(String,"str_tobic",self.timer_call,10)
        self.get_logger().info("sub node is running")
        

    def timer_call(self,msg):
        strr=msg.data
        self.get_logger().info(f"i here mesg    {strr}")
    
     

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