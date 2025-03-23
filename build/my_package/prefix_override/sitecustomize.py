import sys
if sys.prefix == '/var/home/gregorni/Projects/hector-crawler/my_ros2_project/.pixi/envs/default':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/var/home/gregorni/Projects/hector-crawler/my_ros2_project/install/my_package'
