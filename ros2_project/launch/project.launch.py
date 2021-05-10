from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    obj_launch=LaunchDescription()


    node1=Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtle1'
    )
    node2=Node(
        package='ros2_project',
        executable='spawn'
    )
    node3=Node(
        package='ros2_project',
        executable='control'
    )
    obj_launch.add_action(node1)
    obj_launch.add_action(node2)
    obj_launch.add_action(node3)




    return obj_launch
