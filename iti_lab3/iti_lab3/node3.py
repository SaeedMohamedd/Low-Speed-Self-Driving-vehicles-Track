#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_msgs.srv import Firstsr

class My_client(Node):
    def __init__(self):
        super().__init__("reset_client")
        self.service_client(True)
       

    def service_client(self,a):
        client=self.create_client(Firstsr,"reset_server")
        while client.wait_for_service(0.5)==False:
            self.get_logger().warn("waiting server to statrt")
        request=Firstsr.Request()
        self.get_logger().warn("Server ok make request")
        request.flagg=a
        future_obk=client.call_async(request)
        future_obk.add_done_callback(self.future_call)


    def future_call(self,future_msg):
        response=Firstsr.Response()
        self.get_logger().info(response.message)      





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