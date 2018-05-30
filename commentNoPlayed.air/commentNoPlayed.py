# -*- coding=utf-8 -*-
__author__ = "jingchuan.wei"

from airtest.core.api import using,sleep,stop_app,snapshot
# from airtest.report.report import simple_report
import sys
import time
from airtest.core.api import text,touch
sys.path.append("D:/test/spider/login.air")
using("D:/test/spider/rewardLevel.air")
from login import Login
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import unittest

class CommentNoPlayed(Login):
    @classmethod
    def setUpClass(cls):
        super(CommentNoPlayed, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(CommentNoPlayed, cls).tearDownClass()

    def setUp(self):
        print("test reward level no coins start")

    def testCommentNoPlayed(self):

        self.permissionClick()
        self.autoUpdate()
        self.login("wn10008", "z123456")
        self.waitLogin()
        sleep(5)

        self.enterReward()
        self.poco("Tree").child()[0].child("Evaluate").click()
        sleep(1)
        self.startRating()
        self.enterCommnet()
        self.comment()
        self.poco("Return").click()
        sleep(1)
        self.poco("Return").click()
        sleep(1)

        #结束测试
        stop_app("com.gameholic.drawsomethingbyspider")
        sleep(2.0)
        snapshot(msg="app stopped")
        print("finish test")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CommentNoPlayed('testCommnetNoPlayed'))
    runner = unittest.TextTestRunner()




