#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class My_client(Node):
    def __init__(self):
        super().__init__("reset_turtle")
        self.service_client()

    def service_client(self):
        client=self.create_client(Empty,"reset")
        while client.wait_for_service(0.5)==False:
            self.get_logger().warn("waiting server to statrt")
        request=Empty.Request()

        future_obk=client.call_async(request)
        future_obk.add_done_callback(self.future_call)


    def future_call(self,future_msg):
        self.get_logger().info("Reset_Turtle___Done__")        





def main(args=None):
    rclpy.init(args=args)
    client=My_client()
    rclpy.spin(client)

    rclpy.shutdown()

if __name__=="__main__":
    main()


'''
    cliet_obj=client.create_client(AddTwoInts,"first_server_name")
    while cliet_obj.wait_for_service(0.5)==False:
        client.get_logger().warn("wait server to run first")
    req=AddTwoInts.Request()
    req.a=8
    req.b=10
    future_obj=cliet_obj.call_async(req)
    rclpy.spin_until_future_complete(client,future_obj)
    responce=future_obj.result()
    client.get_logger().error(str(responce.sum))
'''