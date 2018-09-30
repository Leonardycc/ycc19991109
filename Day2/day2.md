# Day 2

## Github注册&推送学习笔记
* 申请帐号
* 配置用户名
### 创建仓储

* 克隆                 //git clone
* 状态确定以及存储加备注//git status & git commit -am + name of file
* 推送                 //git push
* (git&github区别：git--本地搭建； github--远端平台）
* 查看改动             //git dif
## 创建带空格文件

* 1. 以“ ”代替空格
* 2. 以\  代替空格
## ROS框架

* 发布者->话题->订阅者
* ros节点 
* rosnode info
* //displaying debug information, including publications, subscriptions and connections.
* ros消息 
* rosmsg show
* //displaying information about ROS Message types
* ros话题 
* rostopic info

## This is the current list of supported commands: 
* rostopic bw	        display bandwidth used by topic
* rostopic delay	display delay of topic from timestamp in header
* rostopic echo	        print messages to screen
* rostopic find	        find topics by type
* rostopic hz	        display publishing rate of topic 
* rostopic info   	print information about active topic
* rostopic list 	list active topics
* rostopic pub 	        publish data to topic
* rostopic type	        print topic or field type
## 建立空间&功能包
* 1 创建内嵌文件
* //mkdir name/src -p
* 2 进入文件以及查看内容
* //cd name & ls
* 3 进入src文件以及创建工作空间
* //cd src & catkin_init_workspace 
* 4 退出src以及查看内容
* //cd .. & ls
* 5 编译&加入bashrc自动加载环境
* //catkin_make 
* 6 进入src文件创建功能包
* //cd src/ & catkin_create_pkg name2 rospy
* 7 进入package并检查文件
* //cd name2/ & ls
* 8 新建并撰写launch文件
* //gedit go.launch
* //(<launch>
* // <node name="talker" pkg="rospy_tutorials" type="talker" />
* //</launch>
* 9 启动launch文件
* roslaunch go.launch
