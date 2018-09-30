# Day 1

## color track

  * 开启地盘
  * //roslaunch mx_bringup rbc_camera_start.launch
  * 开启颜色追踪
  * //roslaunch mx_apps opencv3_follower.launch color


## mapping follower

  * 开启地盘
  * //roslaunch mx_bringup rbc_lidar_start.launch
  * 开启建图模式
  * //roslaunch mx_nav gmapping_demo.launch

## wechat control

  * 启动威信控制
  * rosrun mx_test ros_wechat.py

## 深度跟随

  * 开启地盘
  * //roslaunch mx_bringup rbc_show_start.launch
  * 启动PCL点云追踪follower
  * //roslaunch mx_apps follower2.launch

## voice system
  
  * 开启语音交互
  * roslaunch voice_bringup voice_bringup.launch ;exec bash
  
## 终端指令

 * Ctrl+Alt+Shift+T: 启动终端
 * Ctrl+Shift+T: 合并终端（已有终端时）
 * pwd: 查看根目录 
 * /： 根目录
 * ~： 用户（cd=cd~=cd Desktop/intel/)
 * cd： 进入文件夹
 * cd..: 返回上一级
 * cd -： 撤销
 * ls： 查看文件夹中内容
 * mkdir： 创建文件夹
 * -p： 连续创建
 * touch： 创建文件
 * rm： remove 删除文档
 * rm -r（文件名）：删除文件夹
 * rm py： py文件其全部删除
 * gedit： 更改文件
 * wq： 退出
 * man： 注释
 * vi： 没有桌面时更改文件 （esc+shift+;+w+q）
   


  
