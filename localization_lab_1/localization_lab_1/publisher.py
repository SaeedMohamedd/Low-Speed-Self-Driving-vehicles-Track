#!/usr/bin/env python3

from rcl_interfaces import msg
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from math import e, sin, cos, pi
from geometry_msgs.msg import Quaternion

class my_node (Node):
    def __init__(self):
        super().__init__("imu_publisher_node")       
        self.create_timer(1/30,self.timer_call)
        self.obj_pub=self.create_publisher(Imu,"zed2_imu",10)
        self.get_logger().info("Node is started")
        self.file1 = open('imu_data.csv', 'r')
        self.Lines = self.file1.readlines()
        self.acc_X_list=[]
        self.acc_Y_list=[]
        self.acc_Z_list=[]
        self.ang_X_list=[]
        self.ang_Y_list=[]
        self.ang_Z_list=[]
        self.yaw_deg_list=[]
        self.index=0
        self.count_lines=0

        for line in self.Lines:
            acc_X,acc_Y,acc_z,ang_X,ang_Y,ang_z,yaw_deg=line.split(",")
            self.acc_X_list.append(acc_X)
            self.acc_Y_list.append(acc_Y)
            self.acc_Z_list.append(acc_z)
            self.ang_X_list.append(ang_X)
            self.ang_Y_list.append(ang_Y)
            self.ang_Z_list.append(ang_z)
            self.yaw_deg_list.append(yaw_deg)
            self.count_lines+=1


    def quaternion_from_euler(self, roll, pitch, yaw):
        qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
        qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
        qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
        qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
        return Quaternion(x=qx, y=qy, z=qz, w=qw)

    def timer_call(self):
        msg=Imu()
        yaw_co=0.0
        ang_Z_co=0.0
        msg.header.frame_id="zed2_imu_link"
        msg.linear_acceleration.x=float(self.acc_X_list[self.index])*9.8
        msg.linear_acceleration.y=float(self.acc_Y_list[self.index])*9.8
        msg.linear_acceleration.z=float(self.acc_Z_list[self.index])*9.8
        msg.linear_acceleration_covariance=[0.001, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0, 0.0, 0.001]
        msg.angular_velocity.x=float(self.acc_X_list[self.index])
        msg.angular_velocity.y=float(self.acc_Y_list[self.index])
        msg.angular_velocity.z=float(self.acc_Z_list[self.index])
        if abs(float(self.ang_Z_list[self.index]))< 0.3:
            yaw_co=0.001
            ang_Z_co=0.001
        else:
            yaw_co=0.1
            ang_Z_co=0.1
        msg.angular_velocity_covariance=[0.001, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0, 0.0, ang_Z_co]
        msg.orientation_covariance=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, yaw_co]
        yaw_rad=(float(self.yaw_deg_list[self.index])*pi)/180
        qua=self.quaternion_from_euler(0,0,yaw_rad)
        msg.linear_acceleration.x=qua.x
        msg.linear_acceleration.y=qua.y
        msg.linear_acceleration.z=qua.z
        self.obj_pub.publish(msg)
        self.index+=1
        if self.index >= self.count_lines:
           self.index=0
            

        



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()


