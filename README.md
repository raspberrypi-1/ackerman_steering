[Screencast from 06-27-2023 06_19_59 PM.webm](https://github.com/raspberrypi-1/ackerman_steering/assets/137257528/1ceaf8b3-cfee-4330-b4e9-d071604479db)# **ackerman_steering**
## **Description**
A car capable of performing obstacle avoidance using Ackerman's Steering. Created using ROS2 Humble.
## **How to build**
*creating a workspace*
```
mkdir -p ~/ackerman_car_ws/src && cd ~/ackerman_car_ws/src
```
## **How to use**
```
# source the workspaces
source ~/ackerman_car_ws/install/setup.bash

# Run the launch file
ros2 launch ackerman_car car.launch.py
```
## **Controlling the car**
*Run the following command to take control of the car*
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/car/cmd_vel
```
## **Obstacle Avoidance**
*Open another terminal and run the following commands*
```
source ~/ackerman_car_ws/install/setup.bash
cd ackerman_car_ws/src/ackerman_car/src

python3 obstacle_avoidance.py
```

[Screencast from 06-27-2023 06_19_59 PM.webm](https://github.com/raspberrypi-1/ackerman_steering/assets/137257528/c8eee974-245b-43e4-86e0-eca5e9a8bde4)
