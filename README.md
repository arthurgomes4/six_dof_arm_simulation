[![Image](https://img.shields.io/badge/ROS-Melodic-purple.svg)](https://github.com/arthurgomes4)
[![Image](https://img.shields.io/badge/Gazebo-9.0.0-orange.svg)](https://github.com/arthurgomes4)

# Six Dof Arm
This repository contains ROS packages for simulating a six degrees of freedom robotic arm in Gazebo. The arm was designed and is currently being manufactured by [Manu Jain](https://www.linkedin.com/in/manujain24/). This project is under [Robomanipal](https://robomanipal.com/#/) - The official Robotics team of [MAHE](https://manipal.edu/mu.html).

## Introduction
The Robotic Arm was conceived to be an easy-to-build and inexpensive platform for research and education in STEM fields. Currently available 6 degrees of freedom manipulators are either exorbitantly priced or are too rudimentary to be reliable teaching and learning assets. The fundamental goal of this project is to create an affordable, open-source manipulator without compromising on capability. For further documentation refer to [this](./documentation/6dof_v2.pdf).

<p align="center">
  <img src="./README_images/6dof2.gif" width="400" title="bot">
</p>
<p align="center">
    Fig: joint postion control 
</p>

## Specifics
These packages are developed in **ROS melodic** on **Ubuntu 18.04**. The Simulator used is **Gazebo 9.0.0**. 
## List of Packages
- ```six_dof_arm_description```: A description package containing the model URDF file and meshes.
- ```six_dof_arm_control```: A package containing the launch files and scripts for controlling the arm.

## Downloading and using the packages
- Clone the repository into your local workspace with the command
    ```
    git clone https://github.com/arthurgomes4/six_dof_arm_simulation.git
    ```
- Once built and sourced, run the command:
    ```
    roslaunch six_dof_arm_description gazebo.launch
    ```
    This will launch gazebo and the model of the arm.
    
- Depending on which control method you want to adpot run the launch file from ```six_dof_arm_control``` in a similiar way.

[![Image](https://img.shields.io/badge/developed%20using-VSCode-green.svg)](https://code.visualstudio.com/)
[![Image](https://img.shields.io/badge/Developer-arthurgomes4-blue.svg)](https://github.com/arthurgomes4)