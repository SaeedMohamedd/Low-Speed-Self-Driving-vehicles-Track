#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class my_node(Node):
    def __init__(self):
        super().__init__("Number_counter")
        self.create_timer(1/1,self.pub_num)
        self.str_topic_pub=self.create_publisher(String,"number",10)
        self.obj_pub=self.create_publisher(String,"reset_flag",10)
        self.create_subscription(String,"str_tobic",self.timer_call,10)
        self.get_logger().info("sub node is running")
        self.num_str=0
    def pub_num(self):
        msg=String()
        msg.data=f"number id:{self.num_str}"
        self.str_topic_pub.publish(msg)

    def timer_call(self,msg):
        strr=msg.data
        data_list=strr.split(",")
        num=data_list[1]
        self.num_str=int(num)
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