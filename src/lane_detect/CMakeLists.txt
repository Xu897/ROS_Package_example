cmake_minimum_required(VERSION 2.8.3)
project(lane_detect)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  rospy
  sensor_msgs
)

set(OpenCV_STATIC OFF)
find_package(  OpenCV REQUIRED )
include_directories(${OpenCV_INCLUDE_DIRS})

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES api_lane_detection
  CATKIN_DEPENDS cv_bridge image_transport rospy sensor_msgs
  DEPENDS system_lib
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS lane_detection
   src/main.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )
