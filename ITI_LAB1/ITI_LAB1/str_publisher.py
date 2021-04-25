#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class my_node(Node):
    
    def __init__(self):
        super().__init__("Str_publisher")
        self.get_logger().info("node is running")
        self.create_timer(1/1,self.timer_call)
        self.obj_pub=self.create_publisher(String,"number",10)
        self.create_subscription(String,"reset_flag",self.rec_flag,10)
        self.i=0
        self.flag=''
    def timer_call(self):
        msg=String()
        msg.data=f"SaeedMohamedElsaidBayome is publish,{self.i} "
        self.get_logger().info(msg.data)
        self.obj_pub.publish(msg)
        if self.flag =='f':
            self.i=0
            self.flag=''
        self.i+=1

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