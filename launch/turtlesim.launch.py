import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    joy_config = LaunchConfiguration('joy_config')
    joy_dev = LaunchConfiguration('joy_dev')
    cmd_vel_topic = LaunchConfiguration('cmd_vel_topic')
    publish_stamped_twist = LaunchConfiguration('publish_stamped_twist')
    config_filepath = LaunchConfiguration('config_filepath')

    return LaunchDescription([
        DeclareLaunchArgument('joy_config', default_value='turtlesim_ps4'),
        DeclareLaunchArgument('joy_dev', default_value='0'),
        DeclareLaunchArgument('cmd_vel_topic', default_value='/turtle1/cmd_vel'),
        DeclareLaunchArgument('publish_stamped_twist', default_value='false'),
        DeclareLaunchArgument('config_filepath', default_value=[
            TextSubstitution(text=os.path.join(
                get_package_share_directory('my_bot'), 'config', '')),
            joy_config,
            TextSubstitution(text='.config.yaml'),
        ]),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node',
            output='screen',
        ),
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            parameters=[{
                'device_id': joy_dev,
                'deadzone': 0.15,
                'autorepeat_rate': 20.0,
            }],
        ),
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy',
            output='screen',
            parameters=[config_filepath, {'publish_stamped_twist': publish_stamped_twist}],
            remappings=[('/cmd_vel', cmd_vel_topic)],
        ),
    ])
