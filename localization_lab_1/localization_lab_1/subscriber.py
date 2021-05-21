#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import numpy as np
from math import sin, cos, pi
class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Imu,"/imu",self.timer_call,10)      
        self.get_logger().info("subscriber is started")

    def euler_from_quaternion(self, quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w

        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw        
          
    def timer_call(self,msg):
        a=msg.orientation
        x=abs(msg.linear_acceleration.x)
        z=abs(msg.angular_velocity.z)
        roll,pitch,yaw = self.euler_from_quaternion(a)
        if yaw > -2 or yaw <2 :
            self.get_logger().info(f" yaw {yaw} yaw")
            self.get_logger().info(f"The robot is nearly heading north .. Heading is: {(yaw*180)/pi} degree")
        if x > .3  :
            self.get_logger().info(f" abs linerar accelaration x {x} m/s^2")
            self.get_logger().warn(f"Warning !! .. linear acceleration x exceeded the limit . Current acceleration is {x} m/s^2 where a is the current value.")

        if z> .3  :
            self.get_logger().info(f" abs linerar accelaration x {z} rad/sec")
            self.get_logger().warn(f"Warning !! .. angular velocity z exceeded the limit . Current Angular velocity is {z} rad/sec where a is the current value.")

      
        
        







def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()


