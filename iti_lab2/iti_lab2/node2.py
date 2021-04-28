#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class my_node(Node):
    def __init__(self):
        super().__init__("Number_counter")
        self.create_service(SetBool,"reset_server",self.srv_call)
        self.create_timer(1/1,self.number_counter_call)
        self.obj_pub=self.create_publisher(Int64,"number_counter",10)
        self.create_subscription(Int64,"number",self.timer_call,10)
        self.get_logger().info("sub node2 is running")
        self.acc=0

    def srv_call(self,rq,rsp):
        req_a=rq.data
        if req_a==True:
            self.acc=0
        return rsp    
            
           

    def timer_call(self,msg):
        strr=msg.data
        num=int(strr)
        self.get_logger().info(str(self.acc))
        self.acc +=num
        
        
    def number_counter_call(self):
        msg=Int64()
        msg.data=self.acc
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