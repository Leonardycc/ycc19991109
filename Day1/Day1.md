# Day 1

## color track

  开启地盘
//roslaunch mx_bringup rbc_camera_start.launch
  开启颜色追踪
//roslaunch mx_apps opencv3_follower.launch color


## mapping follower

  开启地盘
//roslaunch mx_bringup rbc_lidar_start.launch
  开启建图模式
//roslaunch mx_nav gmapping_demo.launch ;exec bash

## 深度跟随

  开启地盘
//roslaunch mx_bringup rbc_show_start.launch
  启动PCL点云追踪follower
//roslaunch mx_apps follower2.launch ;exec bash

## 终端指令
 cd： 进入文件夹
 cd..: 返回上一级
 cd -： 撤销
 ls： 查看文件夹中内容
 mkdir： 创建文件夹
 -p： 连续创建
 touch： 创建文件
 rm： remove 删除文件
 rm -r（文件名）：删除文件夹
 rm py： py文件其全部删除
 gedit： 更改文件
 wq： 退出
 man： 注释
 vi： 没有桌面时更改文件 （esc+shift+;+w+q）
   


  
