#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class my_node(Node):
    def __init__(self):
        super().__init__("Number_counter")
        self.obj_pub=self.create_publisher(String,"reset_flag",10)
        self.create_subscription(String,"number",self.timer_call,10)
        self.get_logger().info("sub node is running")

    def timer_call(self,msg):
        strr=msg.data
        data_list=strr.split(",")
        num=data_list[1]
        self.get_logger().info(num)
        if int(num) == 4 :
            m=String()
            m.data='f'
            self.obj_pub.publish(m)
    
        

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