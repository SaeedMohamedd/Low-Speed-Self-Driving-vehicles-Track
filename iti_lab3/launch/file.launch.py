from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    obj_launch=LaunchDescription()


    node1=Node(
        package='iti_lab3',
        executable='node_server'
    )
    node2=Node(
        package='iti_lab3',
        executable='node_client'
    )
    obj_launch.add_action(node1)
    obj_launch.add_action(node2)




    return obj_launch
