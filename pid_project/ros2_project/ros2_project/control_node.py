#!/usr/bin/env python3

import random
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Kill
from my_msgs.srv import Killsr
from example_interfaces.msg import Bool
import math

class my_node(Node):
    def __init__(self):
        super().__init__("Control_node")
        #self.create_service(Firstsr,"reset_server",self.srv_call)
        #self.create_timer(1/1,self.number_counter_call)
        #self.obj_pub=self.create_publisher(Itilab3,"number_counter",10)
        self.create_subscription(Pose,"/new_turtle/pose",self.timer_call_new_turtle,10)
        self.create_subscription(Pose,"/turtle1/pose",self.timer_call_turtle1,10)
        self.obj_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("control node2 is running")
        self.x1  = 0.0
        self.y1  = 0.0
        self.x2 =  0.0
        self.y2  = 0.0
        self.diff_x=0.0
        self.diff_y=0.0
        self.sqr_diff_x=0.0
        self.sqr_diff_y=0.0
        self.sqr_diff=0.0
        self.angle0=0.0
        self.angle=0.0
        self.anglefb=0.0
        self.linear_dist=0.0
        self.lin_vel=0.0
        self.theta_error=0.0
        self.flag=True
        self.x=0.0
        self.y=0.0
        self.thetaa=0.0
        self.once=True
        #self.spawn_service_client()

        self.el_old=0
        self.El=0
        self.ul=0
        self.ea_old=0
        self.Ea=0
        self.ua=0

    def spawn_service_client(self):
        client=self.create_client(Spawn,"spawn")
        while client.wait_for_service(0.5)==False:
            self.get_logger().warn("waiting server to statrt")
        request=Spawn.Request()
        self.x=random.uniform(1, 10)
        self.y=random.uniform(1, 10)
        self.thetaa=random.uniform(0,1)
        request.x=self.x
        request.y=self.y
        request.theta=self.thetaa
        request.name="new_turtle"
        future_obk=client.call_async(request)
        future_obk.add_done_callback(self.get_logger().warn("create new turtle succes"))
        
    def timer_call_turtle1(self,msg):
        #self.timer_call_new_turtle
        self.x1=msg.x
        self.y1=msg.y
        self.angle0=msg.theta
        #self.get_logger().info(f"Turtle 1{self.x1} {self.y1} {self.angle0}")
        self.sqr_diff=abs(math.sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2)))
        #self.lin_vel=self.sqr_diff* 0.5
        self.theta_desired=math.atan2((self.y2-self.y1),(self.x2-self.x1))
        self.theta_error=self.theta_desired-self.angle0
        kpl=.1
        kil=.001
        kdl=.005
        self.el_dot=self.sqr_diff-self.el_old
        self.El+=self.sqr_diff
        self.ul=(kpl*self.sqr_diff)+(kil*self.El)+(kdl*self.el_dot)
        self.el_old=self.sqr_diff

        kpa=1
        kia=.001
        kda=.1
        self.ea_dot=self.theta_error-self.el_old
        self.Ea+=self.theta_error
        self.ua=(kpa*self.theta_error)+(kia*self.Ea)+(kda*self.ea_dot)
        self.ea_old=self.theta_error




        #goal=abs(math.sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2)))
        msg=Twist()
        #msg.linear.x=self.lin_vel
        #msg.angular.z=self.theta_error *2
        msg.linear.x=float(self.ul)
        msg.angular.z=float(self.ua)

        '''
        #print(self.x2,self.y2,self.angle0)
        self.diff_x=abs(self.x1-self.x2) 
        self.diff_y=abs(self.y1-self.y2)
        self.sqr_diff_x=pow(self.diff_x,2)
        self.sqr_diff_y=pow(self.diff_y,2)
        self.sqr_diff=math.sqrt( self.sqr_diff_x+self.sqr_diff_y)
        self.angle=math.atan2(self.diff_y,self.diff_x)
        self.anglefb=self.angle-self.angle0
        self.ang_vel=(self.theta_error)*self.P_ang
        
        if self.anglefb < .5 and self.anglefb > 0 :
            msg.linear.x=1.0

        if self.anglefb > .5 or self.anglefb < 0:
            msg.linear.x=0.0
        print(self.angle,self.angle,self.anglefb)
        '''
        #self.get_logger().info(f"Turtle 1: {self.flag} sqt_diff: { self.sqr_diff} once : {self.once}")
        if self.flag == True:
            self.obj_pub.publish(msg)
            self.get_logger().warn("Turtle 1 obj_pub to cmd_vel")
        if self.sqr_diff < .1 and self.sqr_diff > 0 :
            self.flag=False
            self.lin_vel=0.0
            self.theta_error=0.0
            #self.x1=0
            #self.y1=0
            #self.angle0=0
            #msg.linear.x=0.0
            #msg.angular.z=0.0
            #self.lin_vel=0
            #self.theta_error=0
            #self.sqr_diff=0
            #self.obj_pub.publish(msg)
            #kill_msg=Bool()
            #kill_msg.data=True
            #self.kill_pub.publish(kill_msg)
            if self.once==True:
                self.once=False
                self.kill_service_client()
                print("send kill msg")

    def kill_service_client(self):
        client=self.create_client(Killsr,"kill_turtle_srv")
        while client.wait_for_service(0.5)==False:
            self.get_logger().warn("waiting server to statrt")
        request=Killsr.Request()
        request.data=True
        future_obk=client.call_async(request)
        future_obk.add_done_callback(self.refreach_flag)
        self.get_logger().warn("kill and create new one")

    def refreach_flag(self,future_msg):
        future_msg=Killsr.Response()
        bool_ff=future_msg.resv
        self.flag=future_msg.resv
        self.once=True
        self.get_logger().warn(str(bool_ff))


    def timer_call_new_turtle(self,msg):
        self.x2=msg.x
        self.y2=msg.y
        self.angle=msg.theta
        #self.get_logger().info(f"new turtle{self.x2} {self.y2} {self.angle}")
       
       
      
'''       
    def number_counter_call(self):
        msg=Itilab3()
        msg.num=self.acc
        self.obj_pub.publish(msg)
            def srv_call(self,rq,rsp):f
        req_a=rq.flagg
        if req_a==True:
            self.acc=0
        return rsp    
''' 

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