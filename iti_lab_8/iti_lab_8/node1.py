#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class my_node(Node):
    
    def __init__(self):
        super().__init__("Str_publisher")
        self.get_logger().info("node is running")
        self.create_timer(1/1,self.timer_call)
        self.obj_pub=self.create_publisher(String,"str_tobic",10)
        self.i=0
       
    def timer_call(self):
        msg=String()
        if self.i == 0:
            msg.data="Hi"
            self.i=1
        elif self.i == 1:
            msg.data="Hello"
            self.i=0   
        self.get_logger().info(msg.data)
        self.obj_pub.publish(msg)

        

    def rec_flag(self,f):
        self.flag=f.data

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