# -*- encoding=utf8 -*-
__author__ = "jingchuan.wei"
__title__ = "test ranking"
__desc__ = """
this is a test script.
Used to test leaderboards
"""

# start your script here
from airtest.core.api import sleep,clear_app,wake,home,start_app,stop_app,snapshot,assert_not_equal,exists,Template
import sys
sys.path.append("D:/test/spider/login.air")
from login import Login
import unittest
from poco.exceptions import PocoNoSuchNodeException
from poco.drivers.unity3d import UnityPoco

class RankingCase(Login):
    @classmethod
    def setUpClass(cls):
        super(RankingCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(RankingCase, cls).tearDownClass()

    def setUp(self):
        stop_app("com.gameholic.drawsomethingbyspider")
        clear_app("com.gameholic.drawsomethingbyspider")
        wake()
        home()
        start_app("com.gameholic.drawsomethingbyspider")
        sleep(7)
        self.poco = UnityPoco()
        print("rankding test start")

    def swipeRanking(self, rank, category):
        try:
            if self.poco("Content").child("RankingItem(Clone)")[0].exists():
                sleep(4)
                beforeSwipe = self.poco("Content").child("RankingItem(Clone)")[0].child("Img_Rank").get_position()
                self.poco("Scroll View").child("Content").child("RankingItem(Clone)").swipe("up")
                sleep(4)
                afterSwipe = self.poco("Content").child("RankingItem(Clone)")[0].child("Img_Rank").get_position()
                assert_not_equal(beforeSwipe, afterSwipe, "滑动成功")
        except PocoNoSuchNodeException:
            print("Ranking-(%s)%s is not exists"%(rank,category))

    def myReward(self):
        self.poco("Btn_MyReward").click()
        sleep(1)
        #有奖励
        if self.poco("TitleBg").child("Text_Title").exists():
            print("有可以领取的奖励")
            #关闭不领奖
            self.poco("Btn_Close").click()
            sleep(1)
            if not self.poco("TitleBg").child("Text_Title").exists():
                print("关闭我的奖励界面成功")
            self.poco("Btn_MyReward").click()
            sleep(1)
            if self.poco("TitleBg").child("Text_Title").get_text() == "My Rewards":
                print("关闭未领奖成功")
            self.poco(text="Get rewards").click()
            sleep(1)
            if self.poco("lable").get_text() == "Claimed successfully!":
                print("领取奖励成功")
            self.poco(text="OK").click()
            sleep(1)
            if not self.poco("lable").exists():
                print("领取成功弹框关闭成功")
            self.poco("Btn_MyReward").click()
            sleep(1)
            if "No rewards" in self.poco("lable").get_text():
                print("只能获得一次奖励正确")
                self.poco(text="OK").click()
                sleep(1)
        #无奖励        
        if self.poco("lable").exists():
            if "No rewards" in self.poco("lable").get_text():        
                print("没有可以领取的奖励")
                self.poco(text="OK").click()
                sleep(1)
                if not self.poco("lable").exists():
                    print("关闭无奖励领取弹框成功")

    def lookRanking(self,rank,category):
        #点击标签
        self.poco(text=rank).click()
        sleep(1)
        if exists(Template(r"tpl1524195197433.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.194, -0.837), resolution=(1080, 1920))):
            print("切换总榜成功")
        if exists(Template(r"tpl1524195245944.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.194, -0.843), resolution=(1080, 1920))):
            print("切换周榜成功")
        self.poco(text=category).click()
        sleep(1)
        if exists(Template(r"tpl1522639179495.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.129, -0.702), resolution=(1440, 2560))):
            print("切换到了猎人榜")
        if exists(Template(r"tpl1522639216724.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.19, -0.707), resolution=(1440, 2560))):
            print("切换到了工匠榜")
        if exists(Template(r"tpl1522639268505.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.151, -0.711), resolution=(1440, 2560))):
            print("切换到了巨星榜")    
        #滑动
        self.swipeRanking(rank,category)
        #查看奖励
        self.poco("Btn_RewardDetail").click()
        sleep(1)
        whatRanking = "Rewards-(%s)%s"%(rank,category)
        title = self.poco("TitleBg").child("Text_Title").get_text()
        if whatRanking == title:
            print("查看%s成功"%(whatRanking))
        self.poco("Btn_Close").click()
        sleep(1)
        if not self.poco("TitleBg").exists():
            print("关闭%s成功"%(whatRanking))

    def testRanking(self):
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10001", "z123456")
        self.waitLogin()
        sleep(5)
        #进入排行榜
        self.poco("Ranking").click()
        sleep(1)
        if self.poco(text="What a surprise!").exists():
            self.poco(text="No").click()
            sleep(1)
        if self.poco("Text_Title").get_text() == "Ranking":
            print("进入排行榜成功")
        #退出排行榜
        self.poco("Btn_Back").click()
        sleep(1)
        if not self.poco("Text_Title").exists():                       
            print("退出排行榜成功")
        #查看总榜
        self.poco("Ranking").click()
        sleep(1)
        if self.poco(text="What a surprise!").exists():
            self.poco(text="No").click()
            sleep(1)
        #查看巨星总榜
        self.lookRanking("Total","Superstar")
        #查看猎人总榜
        self.lookRanking("Total","Hunter")
        #查看工匠总榜
        self.lookRanking("Total","Craftsman")
        #查看巨星周榜
        self.lookRanking("Weekly","Superstar")
        #查看猎人周榜
        self.lookRanking("Weekly","Hunter")
        #查看工匠周榜
        self.lookRanking("Weekly","Craftsman")
        #领奖
        self.myReward()
        #退出排行榜
        self.poco("Btn_Back").click()
        #完成测试
        stop_app("com.gameholic.drawsomethingbyspider")
        # sleep(2.0)
        # snapshot(msg="app stopped")
        print("ranking finish test")

        # simple_report("logs")
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(RankingCase('testRanking'))    
    runner = unittest.TextTestRunner()
    runner.run(suite)
    


