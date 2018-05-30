# -*- coding=utf-8 -*-
__author__ = "jingchuan.wei"

from airtest.core.api import using,sleep,stop_app,snapshot,clear_app,wake,home,start_app
# from airtest.report.report import simple_report
import time
from airtest.core.api import text,touch
using("D:/test/spider/login.air")
using("D:/test/spider/rewardLevel.air")
from login import Login
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import unittest
from poco.drivers.unity3d import UnityPoco

class CommentNotEnoughCoins(Login):
    @classmethod
    def setUpClass(cls):
        super(CommentNotEnoughCoins, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(CommentNotEnoughCoins, cls).tearDownClass()

    def setUp(self):
        stop_app("com.gameholic.drawsomethingbyspider")
        clear_app("com.gameholic.drawsomethingbyspider")
        wake()
        home()
        start_app("com.gameholic.drawsomethingbyspider")
        sleep(7)
        self.poco = UnityPoco()
        print("test reward level no coins start")

    def testCommentNotEnoughCoins(self):

        self.permissionClick()
        self.autoUpdate()
        self.login("wn10002", "z123456")
        self.waitLogin()
        sleep(5)

        self.enterReward()
        #金币不足无法进入一个关卡
        self.enterOneReward()
        #进入评论，输入星级和评论文字，点击评论，提示金币不足
        self.poco("Tree").child()[0].child("Evaluate").click()
        sleep(1)
        self.startRating()
        self.enterCommnet()
        self.comment()
        #结束测试
        stop_app("com.gameholic.drawsomethingbyspider")
        sleep(2.0)
        snapshot(msg="app stopped")
        print("finish test")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CommentNotEnoughCoins('testCommentNotEnoughCoins'))
    runner = unittest.TextTestRunner()
    runner.run(suite)