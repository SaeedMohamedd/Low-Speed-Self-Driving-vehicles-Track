#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
from rclpy.qos import qos_profile_sensor_data
from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy
#from rclpy.qos_overr import QoSOverridingOptions
#from rclpy.qos_overriding_options import QosCallbackResult

class my_node(Node):
    
    def __init__(self):
        super().__init__("Sub_Node")
        self.get_logger().info("Sub_Node is running")
        self.create_subscription(String,"my_topic",self.timer_call,rclpy.qos.qos_profile_sensor_data)
        #self.sub = self.create_subscription(String, '/my_topic', self.timer_call, 10,qos_overriding_options=QoSOverridingOptions.with_default_policies(callback=self.qos_callback,))
        self.counter=0
        
      
    def timer_call(self,msg):
        self.counter+=1
        self.get_logger().info(f"Saeed Mohamed heard: {msg.data} {self.counter} times")
    
   

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