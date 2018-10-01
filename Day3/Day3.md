# Day 3

## rqt图像调试
* 发送消息
* 根据图标形式调节
* 启动rqt
* 打开plugins-visualization-plot
* 根据目标位置改变而改变横纵坐标
## 当控制运动时
* rostopic find 类型
* 开启rqt_graph
* 寻找节点
* rostopic pub 
## 可以用rqt看摄像头以及雷达检验
* 当机器被困住的时候，程序依然会认为机器在走动，所以建立地图偏差
* 检验： 添加odometry以看清
## move base路径规划
* move base实现了自主导航当给予固定目标的时候
* global planer 确定了初始的行驶轨迹
* local planer 作出灵活改变当遇到突发状况
* global costmap 考虑全局代价
* local costmap 考虑临时代价
* recovery behavior 备用方案
## 机器simulation SLAM
* 1 启动gazebo环境包 加载机器人
* roslaunch mx_urdf gazebo.launch
* roslaunch turtlebot_gazebo turtlebot_world.launch
* 2 启动控制
* roslaunch turtlebot_teleop keyboard_teleop.launch
* 3 启动算法功能包
* roslaunch turtlebot_gazebo gmapping_demo.launch
* 4 启动rviz查看地图
* roslaunch turtlebot_rviz_launchers view_navigation.launch
* 5 指定目标 
*
* 6 保存地图
* ~/mxBot_ws/src/mx_turtleBot/mx_bringup/Show地图存放文件夹
* /home/intel/mxBot_ws/src/mx_turtleBot/mx_nav/config/fake网站 

## 实际操作
* 
* roslaunch mx_bringup rbc_lidar_start.launch
* roslaunch mx_nav gmapping_demo.launch
* roslaunch mx_rviz gmapping_view.launch 
## movebase参数 
* base_local_planner_params.yaml
* max_vel_x/ max_vel_y
* escape_vel
* yaw_goal_tolerance
* xy_goal_tolerance
* pdist_scale
* gdist_scale
* vx_sample
* vthea_sample
* holonomic_robot
* costmap_common_params.yaml
* obstacle_range
* raytrace_range
* robot_radius
