#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from std_srvs.srv import Empty

#from rclpy.qos_overr import QoSOverridingOptions
#from rclpy.qos_overriding_options import QosCallbackResult

class my_node(Node):
    
    def __init__(self):
        super().__init__("Sub_Node")
        self.get_logger().info("Sub_Node is running")
        self.create_subscription(Pose,"/turtle1/pose",self.timer_call,10)
        #self.sub = self.create_subscription(String, '/my_topic', self.timer_call, 10,qos_overriding_options=QoSOverridingOptions.with_default_policies(callback=self.qos_callback,))
        self.x=0.0
        self.y=0.0

     
    def timer_call(self,msg):
        self.x=msg.x
        self.y=msg.y
        self.get_logger().info(f"{self.x} {self.y}")
        if self.x<2  or self.x > 8 : 
            if self.y<2 or self.y>8:
                self.get_logger().info("here")
                client=self.create_client(Empty,"reset")
                while client.wait_for_service(0.5)==False:
                    self.get_logger().warn("waiting server to statrt")
                request=Empty.Request()
                future_obk=client.call_async(request)
                


    
   

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