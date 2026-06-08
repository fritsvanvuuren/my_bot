from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # turtle_teleop_key is an interactive terminal program and cannot be launched reliably
    # through ros2 launch in the same background session. Run it from a separate terminal:
    #   ros2 run turtlesim turtle_teleop_key
    return LaunchDescription([
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
            emulate_tty=True,
        ),
    ])
