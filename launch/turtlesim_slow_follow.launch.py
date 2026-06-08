from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            output='screen',
        ),
        Node(
            package='turtle_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ],
            output='screen',
        ),
        Node(
            package='turtle_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ],
            output='screen',
        ),
        Node(
            package='my_bot',
            executable='turtle2_slow_listener.py',
            name='slow_listener',
            parameters=[
                {'target_frame': 'turtle1'}
            ],
            output='screen',
        ),
    ])
