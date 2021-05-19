#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist
import time

class my_node (Node):
    def __init__(self):
        super().__init__("Node1_name")       
        self.create_timer(1/1,self.timer_call)
        self.obj_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_subscription(Pose,"/turtle1/pose",self.sub_call,10)
        self.get_logger().info("Node is started")
        self.file1 = open('turtle_commands.csv', 'r')
        self.Lines = self.file1.readlines()
        self.linear_list=[]
        self.velocity_list=[]
        self.index=1

        for line in self.Lines:
            liner_velocity,angular_velocity=line.split(",")
            self.linear_list.append(liner_velocity)
            self.velocity_list.append(angular_velocity)

        self.x=0.0
        self.y=0.0

    def sub_call(self,msg):
        self.x=msg.x
        self.y=msg.y


    def timer_call(self):
        msg=Twist()
        msg.linear.x=float(self.linear_list[self.index])
        msg.angular.z=float(self.velocity_list[self.index])
        self.obj_pub.publish(msg)
        self.get_logger().info(f"{self.linear_list[self.index]} {self.velocity_list[self.index]}  {self.x} {self.y}")
        if not(2<self.x<8 and 2<self.y<8 ):
            self.get_logger().info("out of limit")
            client=self.create_client(Empty,"reset")
            while client.wait_for_service(0.5)==False:
                 self.get_logger().warn("waiting server to statrt")
            request=Empty.Request()
            client.call_async(request)
        self.index+=1
        if self.index >= 13:
            self.index=1
            

        



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()


