from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'my_bot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='frits',
    maintainer_email='frits@example.com',
    description='Launch turtlesim with PlayStation controller support.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={},
)
