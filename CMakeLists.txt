cmake_minimum_required(VERSION 3.0.2)
project(py3_example)

find_package(catkin REQUIRED)
catkin_package()

catkin_install_python(PROGRAMS scripts/myscript.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(test/test_my_stuff.launch)
endif()
