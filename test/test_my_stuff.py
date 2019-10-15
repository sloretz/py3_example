#! /usr/bin/python

import os
import sys
import unittest


class TestMyStuff(unittest.TestCase):

    def test_expected_python_version(self):
        self.assertEqual(os.environ.get('ROS_PYTHON_VERSION'), sys.version[0])


if __name__ == '__main__':
    import rostest
    rostest.rosrun('py3_example', 'test_my_stuff', TestMyStuff)
