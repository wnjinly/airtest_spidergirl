# -*- encoding=utf8 -*-
__author__ = "jingchuan.wei"
__title__ = "test basic level"
__desc__ = """
this is a test script.
test basic level
"""


# start your script here
from airtest.core.api import sleep,clear_app,wake,home,start_app,stop_app,snapshot
from airtest.report.report import simple_report
import sys
sys.path.append("D:/test/spider/login.air")
from login import Login
import unittest
from poco.drivers.unity3d import UnityPoco


class BasicLevelCase(Login):
    @classmethod
    def setUpClass(cls):
        super(BasicLevelCase, cls).setUpClass()
    @classmethod
    def tearDownClass(cls):
        super(BasicLevelCase, cls).tearDownClass()

    def setUp(self):
        stop_app("com.gameholic.drawsomethingbyspider")
        clear_app("com.gameholic.drawsomethingbyspider")
        wake()
        home()
        start_app("com.gameholic.drawsomethingbyspider")
        sleep(7)
        self.poco = UnityPoco()
        print("Basic level test start")
    
    def testBasicLevel(self):
    # init_device()
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10001", "z123456")
        self.waitLogin()
        sleep(5)
        
        # self.self.poco = Unityself.poco()
        self.poco(text="Basic Stage").click()
        sleep(1)
        if self.poco("Up").child("Text").get_text() == "Select Stage":
            assert("进入基础关卡成功")
        self.poco("Explain").click()
        sleep(1)
        if self.poco("zi").exists():
            assert("成功打开帮助")
        self.poco("confirm").click()
        sleep(1)
        if not self.poco("txt").exists():
            assert("成功关闭帮助界面")    
        for _ in range(4):
            self.poco.swipe([50.0/720, 400.0/1280], [670.0/720, 400.0/1280])
            sleep(3)
        self.poco("Content").offspring('Levelnum1').click()
        sleep(1)
        if self.poco("HPimage").exists():
            assert("成功进入具体关卡")
        sleep(1.0)
        self.poco("Return2").click()
        sleep(1)
        exitText = self.poco("lable").get_text()
        if exitText == "Are you sure you want to exit the game?":
            assert("成功打开退出弹框")
        self.poco(text="Cancel").click()

        sleep(1)
        if not self.poco("lable").exists() and self.poco("HPimage").exists():
            assert("成功关闭退出弹框")
        self.poco("Return2").click()
        sleep(1)
        if exitText == "Are you sure you want to exit the game?":
            assert("再次成功打开退出弹框")
        self.poco(text="OK").click()
        if self.poco("Up").child("Text").get_text() == "Select Stage":
            assert("成功退出具体关卡")
        for _ in range(4):
            self.poco.swipe([670.0/720, 400.0/1280], [50.0/720, 400.0/1280])
            sleep(3)
        if self.poco("WaitAfter").exists():
            assert("所有关卡都可以翻页")
        self.poco("Levelnum40").click()
        sleep(1)
        if not self.poco("HPimage").exists() and self.poco("Up").exists():
            assert("未解锁关闭无法进入")
        self.poco("Return").click()
        sleep(1)
        if self.poco("StartGame").exists():
            assert("返回主界面成功")

        stop_app("com.gameholic.drawsomethingbyspider")
        sleep(2.0)
        snapshot(msg="app stopped")
        print("basic level finish test")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(BasicLevelCase('testBasicLevel'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
# runTest()
#python运行去除注释，生成报告
# simple_report("logs")



