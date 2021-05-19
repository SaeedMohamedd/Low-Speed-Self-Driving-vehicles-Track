#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist

class my_node (Node):
    def __init__(self):
        super().__init__("Node1_name")       
        self.create_timer(1/1,self.timer_call)
        self.obj_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_subscription(Pose,"/turtle1/pose",self.sub_call,10)
        self.get_logger().info("Node is started")
        self.file1 = open('turtle_commands.csv', 'r')
        self.Lines = self.file1.readlines()
        self.x=0.0
        self.y=0.0

    def sub_call(self,msg):
        self.x=msg.x
        self.y=msg.y


    def timer_call(self):
        msg=Twist()
        for line in self.Lines:
            liner_velocity,angular_velocity=line.split(",")
            msg.linear.x=float(liner_velocity)
            msg.angular.z=float(angular_velocity)
            self.obj_pub.publish(msg)
            self.get_logger().info(f"{liner_velocity} {angular_velocity}  {self.x} {self.y}")

            if self.x<2  or self.x > 8 : 
                if self.y<2 or self.y>8:
                    self.get_logger().info("out of limit")
                    client=self.create_client(Empty,"reset")
                    while client.wait_for_service(0.5)==False:
                        self.get_logger().warn("waiting server to statrt")
                    request=Empty.Request()

        



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()


