import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'my_bot'
    package_share = get_package_share_directory(package_name)

    joy_config = LaunchConfiguration('joy_config')
    joy_dev = LaunchConfiguration('joy_dev')
    config_filepath = LaunchConfiguration('config_filepath')

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_share, 'launch', 'launch_sim.launch.py')
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'joy_config',
            default_value='turtlesim_ps4',
            description='Controller configuration file name without .config.yaml',
        ),
        DeclareLaunchArgument(
            'joy_dev',
            default_value='0',
            description='Joystick device ID',
        ),
        DeclareLaunchArgument(
            'config_filepath',
            default_value=[
                TextSubstitution(text=os.path.join(package_share, 'config', '')),
                joy_config,
                TextSubstitution(text='.config.yaml'),
            ],
            description='Path to the teleop_twist_joy configuration file',
        ),
        simulation,
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
            parameters=[
                config_filepath,
                {'publish_stamped_twist': True},
            ],
        ),
    ])
