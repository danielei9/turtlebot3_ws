from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='position_publisher',
            executable='position1_publisher',
            output='screen'),
    ])
