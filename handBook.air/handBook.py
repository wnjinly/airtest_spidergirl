# -*- encoding=utf8 -*-
__author__ = "Administrator"
__title__ = "test script title"
__desc__ = """
this is a test script.
"""

# start your script here
from airtest.core.api import sleep,clear_app,wake,home,start_app,stop_app,snapshot
from airtest.report.report import simple_report
import sys
sys.path.append("D:/test/spider/login.air")
from login import Login 
from poco.drivers.unity3d import UnityPoco
import unittest


class HandbookCase(Login):
    @classmethod
    def setUpClass(cls):
        super(HandbookCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HandbookCase, cls).tearDownClass()

    def setUp(self):
        print("handBook test start")


    def testHandBook(self):
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10001", "z123456")
        self.waitLogin()
        sleep(5)

        #进入图鉴
        # poco = UnityPoco()
        self.poco("Favorites").click()
        sleep(1)
        if self.poco(text="Handbook").get_text() == 'Handbook':
            print("进入图鉴成功")
        #查看帮助
        self.poco("Explain").click()
        sleep(1)
        if self.poco("txt").exists():
            print("打开帮助成功")
            self.poco("confirm").click()
            sleep(1)
            if not self.poco("txt").exists():
                print("关闭帮助成功")
        #切换标签
        self.poco("Text (1)").click()
        sleep(1)
        if self.poco("10102").exists():
            print("切换悬赏关卡标签成功")
        self.poco(text="Basic Stage").click()
        sleep(1)
        if self.poco("Levelnum2001").exists():
            print("切换基础关卡标签成功")
        #滑动列表
        beforeSwipe = self.poco("Levelnum2001").child("thumbnail").child("Image").get_position()
        self.poco("OursLevel").swipe([0,-0.2])
        sleep(2)
        afterSwipe = self.poco("Levelnum2001").child("thumbnail").child("Image").get_position()
        if beforeSwipe != afterSwipe:
            assert("滑动基础关卡图鉴成功")  
        self.poco("OursLevel").swipe([0,0.4])
        sleep(2)
        #查看具体图鉴
        self.poco("Levelnum1").click()
        sleep(1)
        if self.poco(texture="zhizuoguanka_kuang").exists():
            print("查看具体图鉴成功")
        #恢复图鉴状态
        for _ in range(2):
            self.poco("Left").click()
            sleep(1)
        #读取第1、3张图位置
        beforeSwipe1 = self.poco("Scroll View").child("Content").child("pic")[0].child("Panel").child("image").get_position()
        beforeSwipe3 = self.poco("Scroll View").child("Content").child("pic")[2].child("Panel").child("image").get_position()
        for _ in range(3):
            self.poco("BigPic").child("Middle").child("Scroll View").swipe([-0.4,0])   
            sleep(1)
        afterSwipe3 = self.poco("Scroll View").child("Content").child("pic")[2].child("Panel").child("image").get_position()
        if beforeSwipe3 != afterSwipe3:
            assert("向右滑动翻页成功")
        for _ in range(3):
            self.poco("BigPic").child("Middle").child("Scroll View").swipe([0.4,0])   
            sleep(1)
        afterSwipe1 = self.poco("Scroll View").child("Content").child("pic")[0].child("Panel").child("image").get_position()
        if beforeSwipe1 == afterSwipe1:
            assert("向左滑动翻页成功")

        for _ in range(2):
            self.poco("right").click()
            sleep(1)
        afterClick3 = self.poco("Scroll View").child("Content").child("pic")[2].child("Panel").child("image").get_position()
        if afterClick3 == afterSwipe3:
            assert("点击右翻页成功")

        for _ in range(2):
            self.poco("Left").click()
            sleep(1)
        afterClick1 = self.poco("Scroll View").child("Content").child("pic")[0].child("Panel").child("image").get_position()
        if afterClick1 == beforeSwipe1:
            assert("点击左翻页成功")

        self.poco("BigPic").child("Middle").child("Scroll View").click()
        if self.poco(text="Handbook").exists():
            assert("关闭具体图鉴成功")

        #退出图鉴
        self.poco("Return").click()
        sleep(1)
        if not self.poco(text="Handbook").exists():
            print("退出图鉴成功")
        print("handBook finish test")
        #完成测试
        stop_app("com.gameholic.drawsomethingbyspider")
        sleep(2.0)
        snapshot(msg="app stopped")
        print("finish test")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(HandbookCase('testHandBook'))
    runner = unittest.TextTestRunner()
    runner.run(suite)


