#!/usr/bin/env python3
import random
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from my_msgs.srv import Killsr
from example_interfaces.msg import Bool
from turtlesim.msg import Pose

class My_client(Node):
    def __init__(self):
        super().__init__("Spawn_client_node")
        self.new_turtle_pub=self.create_publisher(Pose,"/new_turtle/pose",10)
        self.create_service(Killsr,"kill_turtle_srv",self.srv_call)
        self.spawn_service_client()
        self.x=0.0
        self.y=0.0
        self.thetaa=0.0
       
       
    def srv_call(self,rq,rep):
        if rq.data ==True :
            self.kill_service()
            self.spawn_service_client()
            #rep=Killsr.Response()
            rep.resv=True
        return rep
        

    def spawn_service_client(self):
        client=self.create_client(Spawn,"spawn")
        while client.wait_for_service(0.5)==False:
            self.get_logger().warn("waiting server to statrt")
        request=Spawn.Request()
        self.x=random.uniform(5, 10)
        self.y=random.uniform(5, 10)
        self.thetaa=random.uniform(0,1)
        request.x=self.x
        request.y=self.y
        request.theta=self.thetaa
        request.name="new_turtle"
        future_obk=client.call_async(request)
        self.get_logger().warn("create new turtle succes")
        future_obk.add_done_callback(self.pub_pose_newTurtle)
        

    def kill_service(self):
        client=self.create_client(Kill,"kill")
        while client.wait_for_service(0.5)==False:
            self.get_logger().warn("waiting server to statrt")
        request=Kill.Request()
        request.name="new_turtle"
        future_obk=client.call_async(request)
        future_obk.add_done_callback(self.get_logger().warn("killing the new turtle succes"))

    def pub_pose_newTurtle(self,a):
        msg=Pose()
        msg.x=self.x
        msg.y=self.y
        msg.theta=self.thetaa
        self.new_turtle_pub.publish(msg)
        self.get_logger().warn("pub pose new turtle succes")




def main(args=None):
    rclpy.init(args=args)
    client=My_client()
    rclpy.spin(client)

    rclpy.shutdown()

if __name__=="__main__":
    main()

