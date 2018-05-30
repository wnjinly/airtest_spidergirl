# -*- encoding=utf8 -*-
__author__ = "jingchuan.wei"
__title__ = "test Monster Handbook"
__desc__ = """
this is a test script.
用来测试怪物图鉴
"""


# start your script here
from airtest.core.api import sleep,stop_app,assert_not_equal,snapshot
from airtest.report.report import simple_report
import sys
sys.path.append("D:/test/spider/login.air")
from login import Login
import unittest

class MonsterBookCase(Login):
    @classmethod
    def setUpClass(cls):
        super(MonsterBookCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MonsterBookCase, cls).tearDownClass()


    def setUP(self):
        print("monster book test start")

    def testMonsterBook(self):
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10001", "z123456")
        self.waitLogin()
        sleep(5)
        #由于怪物图鉴重新安装游戏后会消失的bug存在，所以先进入一个关卡解锁一个怪物
        self.poco(text="Basic Stage").click()
        sleep(1)
        for _ in range(4):
            self.poco.swipe([16.0/576 ,400.0/1024] ,[560.0/576, 400.0/1024])
            sleep(3)
            
        if self.poco("Levelnum1").child("thumbnail").child("Image").exists():
            self.poco("Levelnum1").child("thumbnail").child("Image").click()
            sleep(1)
        self.poco("Return2").click()
        sleep(1)
        self.poco(text="OK").click()
        sleep(1)
        self.poco("Return").click()
        sleep(1)
        #进入图鉴
        self.poco("MonsterCompose").click()
        sleep(1)
        if self.poco("Tree").child("LvTemplate(Clone)").child("thumbnail").exists():
            print("进入图鉴成功")
        #测试帮助
        self.poco("Explain").click()
        sleep(1)
        helpText = self.poco("txt").get_text()
        if "Monsters illustrated" in helpText:
            print("打开帮助成功")
            self.poco("confirm").click()
            sleep(1)
            if not self.poco("zi").exists():
                print("关闭帮助成功")
        #测试单个怪物
        self.poco("Tree").child("LvTemplate(Clone)").child("thumbnail").click()
        sleep(1)
        if self.poco("MonsterInfo").exists():
            print("查看具体怪物详情成功")
        self.poco("Return").click()
        sleep(1)
        if not self.poco("MonsterInfo").exists():
            print("关闭具体怪物详情成功")
        #测试滑动
        beforeSwipe = self.poco("Tree").child("LvTemplate(Clone)")[0].child("thumbnail").get_position()

        self.poco("Viewport").swipe([0,-0.4])
        sleep(2)
        afterSwipe = self.poco("Tree").child("LvTemplate(Clone)")[0].child("thumbnail").get_position()

        assert_not_equal(beforeSwipe,afterSwipe, "滑动成功")

        #退出图鉴
        self.poco("Return").click()
        sleep(1)
        if  not self.poco("Tree").child("LvTemplate(Clone)").child("thumbnail").exists():
            print("退出怪物图鉴成功")
            
        #测试完成
        stop_app("com.gameholic.drawsomethingbyspider")
        sleep(2.0)
        snapshot(msg="app stopped")
        print("monster handbook finish test")

        # simple_report("logs")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MonsterBookCase('testMonsterBook'))    
    runner = unittest.TextTestRunner()
    runner.run(suite)

