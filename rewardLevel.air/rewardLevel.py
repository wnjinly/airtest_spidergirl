# -*- encoding=utf8 -*-
__author__ = "Administrator"
__title__ = "test script title"
__desc__ = """
this is a test script.
"""

# start your script here
from airtest.core.api import sleep,clear_app,wake,home,start_app,stop_app,snapshot,Template,exists,shell,assert_exists,using
# from airtest.report.report import simple_report
import sys
import time
from airtest.core.api import text,touch
sys.path.append("D:/test/spider/login.air")
using("D:/test/spider/rewardLevel.air")
from login import Login
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import unittest
from poco.drivers.unity3d import UnityPoco

class RewardLevelCase(Login):
    @classmethod
    def setUpClass(cls):
        super(RewardLevelCase, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(RewardLevelCase, cls).tearDownClass()
    
    def setUp(self):
        stop_app("com.gameholic.drawsomethingbyspider")
        clear_app("com.gameholic.drawsomethingbyspider")
        wake()
        home()
        start_app("com.gameholic.drawsomethingbyspider")
        sleep(7)
        self.poco = UnityPoco()
        assert("reward level test start")

    #进入悬赏关卡
    def enterReward(self):
        self.poco("RewardLV").click()
        sleep(2)
        if self.poco("Upup").child("Text").get_text() == "Reward Stage":
            assert("进入悬赏关卡成功")



    #悬赏关卡帮助        
    def rewardHelp(self):
        self.poco("Explain").click()
        sleep(1)
        if "You can find" in self.poco("txt").get_text():
            assert("打开悬赏关卡成功")
            self.poco("confirm").click()
            sleep(1)
            if not self.poco("txt").exists():
                assert("关闭帮助界面成功")

    def sorting(self, whatTabel):    
        items = self.poco("Tree").child()
        listReward = []
        listRate = []    
        if whatTabel == "Overall":
            for item in items:
                listReward.append(item.child("reward").get_text())
            if listReward[0] == max(listReward):
                assert("人气排序正确")            
        if whatTabel == "Popularity":
            for item in items:
                listReward.append(item.child("AllPlayerCount").get_text())
            if listReward[0] == max(listReward):
                assert("流行度排序正确")
                
        if whatTabel == "Difficulty":
            for item in items:
                challenge = item.child("AllPlayerCount").get_text()
                passStage = item.child("PassPlayerCount").get_text()
                if int(challenge) == 0:
                    listRate.append(1)
                else:
                    rate = float(passStage)/float(challenge)
                    listRate.append(rate)
            if listRate[0] == min(listRate): 
                assert("难度排序正确")
                
    #切换标签
    def changeLabel(self):
        self.poco(text="Popularity").click()    
        self.poco("Tree").child().child("LvName").wait_for_appearance()
        self.sorting("Popularity")
        self.poco(text="Difficulty").click()
        self.poco("Tree").child().child("LvName").wait_for_appearance()
        self.sorting("Difficulty")
        self.poco(text="Overall").click()
        self.poco("Tree").child().child("LvName").wait_for_appearance()
        self.sorting("Overall")

    #上下滑动列表   
    def swipeList(self):
        if len(self.poco("Tree").child().nodes) > 5:
            beforeSwipe = self.poco("Tree").child()[0].child("idtext").get_position()
            self.poco.swipe([500.0 / 1080, 1500.0 / 1920], [500.0 / 1080, 200.0 / 1920])
            sleep(3)
            afterSwipe = self.poco("Tree").child()[0].child("idtext").get_position()
            if beforeSwipe != afterSwipe:
                assert("swipe list successfully")
            else:
                assert("swipe list failed")
        
    #筛选弹框开启关闭
    def filterOpen(self):
        self.poco(text="Filters").click()
        sleep(1)
        if self.poco(text="mine").exists():
            assert("筛选界面成功打开")        
            self.poco("closed").click()
            sleep(1)
            #存在关闭弹框，但是未销毁弹框对象的bug，所以用get_position方式实现功能
            pos = self.poco("My").get_position()
            if pos == [0.5, 0.5]:
                assert("关闭筛选界面成功")
                self.poco("Return").click()
                sleep(1)
                self.poco("RewardLV").click()
                sleep(1)

    #进行筛选，去除所有人
    def switchFliters(self):
        self.poco(text="Filters").click()
        sleep(1)
        while exists(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.188, -0.208), resolution=(1440, 2560))):
            touch(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.188, -0.208), resolution=(1440, 2560)))
            sleep(1)
        self.poco("My").click()
        sleep(1)
        assert_exists(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(0.095, -0.21), resolution=(1440, 2560)), "去除mine勾选成功")
        self.poco("My").click()
        sleep(1)
        self.poco("other").click()
        sleep(1)
        assert_exists(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(0.095, -0.21), resolution=(1440, 2560)), "other可以除去勾选框")
        self.poco("other").click()
        sleep(1)
        self.poco("Played").click()
        sleep(1)
        assert_exists(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(0.095, -0.21), resolution=(1440, 2560)), "not hide played today可以除去勾选框")

    def cancelAll(self):
        #去除所有勾选
        while exists(Template(r"tpl1524898630127.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.096, -0.211), resolution=(720, 1280))):
            touch(Template(r"tpl1524898630127.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.096, -0.211), resolution=(720, 1280)))
            sleep(0.5)
        self.poco.click([360.0/720, 700.0/1280])
        sleep(1)
        assert("去掉所有人的关卡")
        if not self.poco("Tree").child().exists():
            assert("去掉所有人的关卡成功")
            
    #查看自己关卡
    def onlyMine(self, player):
        self.poco(text="Filters").click()
        sleep(1)
        while exists(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.188, -0.208), resolution=(1440, 2560))):
            touch(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.188, -0.208), resolution=(1440, 2560)))
            sleep(0.5)
        self.poco("other").click()
        sleep(1)
        self.poco("Played").click()
        sleep(1)
        self.poco.click([360.0/720, 700.0/1280])
        sleep(1)    
        self.poco(text="Popularity").click()
        sleep(1)
        myLevels = self.poco("Tree").child()
        marklist = []
        # player = self.poco("ToUserInfo").child("Text").get_text()
        for i in myLevels:
            if str(player) in i.child("LvMaker").get_text():
                marklist.append(1)
            else:
                marklist.append(0)
        assert(marklist)
        if max(marklist) == min(marklist) and max(marklist) == 1:
            assert("只保留自己的关卡成功")
        

    # 恢复关卡
    def recoveryFilters(self):
        self.poco(text="Filters").click()
        while exists(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.188, -0.208), resolution=(1440, 2560))):
            touch(Template(r"tpl1522138307590.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.188, -0.208), resolution=(1440, 2560)))
            sleep(1)
        self.poco.click([360.0/720, 700.0/1280])
        sleep(2)

    #进入关卡、退出关卡
    def enterOneReward(self):
        self.poco("Tree").child()[0].child("PlayThisLv").click()
        sleep(1)
        self.poco("lable").wait_for_appearance()
        popText = self.poco("Popup").child("BG").child("lable").get_text()
        print(popText)
        #not enough coins
        if "Not enough coins！" == popText:
            assert("金币不足无法进入成功")
            self.poco("Popup").child("BG").child("Button").click()
            if not self.poco("lable").exists():
                sleep(10)
                assert("金币不足弹框关闭成功")
        #coin enough
        if "You need to spend coins" in self.poco("lable").get_text():
            print("打开消耗金币弹框成功")
            self.poco(text="Cancel").click()
            sleep(1)
            if self.poco("lable").get_position() == [0.5, 0.5]:
                assert("取消关闭弹框成功")
                self.poco("Tree").child()[0].child("PlayThisLv").click()
                self.poco(text="OK").click()
                sleep(2)
            if self.poco("Hp").exists():
                assert("进入悬赏关卡成功")
                self.poco("Return2").click()
                sleep(1)
                if self.poco("lable").get_text() == "Are you sure you want to exit the game?":
                    assert("打开退出关卡弹框成功")
                self.poco(text="Cancel").click()
                sleep(1)
                if not self.poco("lable").exists():
                    assert("取消退出关卡成功")
                self.poco("Return2").click()
                sleep(1)
                self.poco(text="OK").click()
                sleep(1)
                if self.poco("Upup").exists():
                    assert("退出悬赏关卡成功")

        
        
    #点赞
    def like(self):
        for _ in range(2):
            self.poco.swipe([360.0 / 720, 93.0 / 1280], [360.0 / 720, 870.0 / 1280], duration=0.2)
            sleep(2)    
        self.poco("Center").offspring("Tree").child()[0].offspring("Btn_DisAgree").click()
        sleep(1)
        beforeAgree = self.poco("Center").offspring("Tree").child()[0].offspring("Btn_Agree").child("Text_AgreeNum").get_text()
        self.poco("Center").offspring("Tree").child()[0].offspring("Btn_Agree").click()
        sleep(1)
        afterAgree = self.poco("Center").offspring("Tree").child()[0].offspring("Btn_Agree").child("Text_AgreeNum").get_text()
        if int(beforeAgree) + 1 == int(afterAgree):
            assert("点赞成功")

    #点踩
    def hate(self):
        self.poco("Center").offspring("Tree").child()[0].offspring("Btn_Agree").click()
        sleep(1)
        beforeAgree = self.poco("Center").offspring("Tree").child()[0].offspring("Btn_DisAgree").child("Text_DisAgreeNum").get_text()
        self.poco("Center").offspring("Tree").child()[0].offspring("Btn_DisAgree").click()
        sleep(1)
        afterAgree = self.poco("Center").offspring("Tree").child()[0].offspring("Btn_DisAgree").child("Text_DisAgreeNum").get_text()
        if int(beforeAgree) + 1 == int(afterAgree):
            assert("点踩成功")

    #评论
    def comment(self):
        self.poco("Btn_Evaluate").click()
        sleep(1)
        popText = self.poco("lable").get_text()
        if popText == "Not enough coins !":
            assert("金币不足无法评论成功")
            self.poco(text="OK").click()
            sleep(1)
        if popText == "You need to give a score!":
            assert("评论星级不能为空成功")
            self.poco(text="OK").click()
            sleep(1)
        if popText == "Empty content!":
            assert("评论不能为空成功")
            self.poco(text="OK").click()
            sleep(1)
        if "1000 coins" in popText:
            assert("弹出花费金币成功")
            self.poco(text="Cancel").click()
            if not self.poco("lable").exists():
                assert("关闭花费金币弹框成功")
            self.poco("Btn_Evaluate").click()
            sleep(1)
            self.poco(text="Confirm").click()
            sleep(1)
            if popText == "Comment sent!":
                assert("评论成功")
                self.poco(text="OK").click()
                sleep(1)
        if "Failed to send comment." in self.poco("lable").get_text():
            assert("没玩过关卡无法评论成功")
            self.poco(text="OK").click()
            sleep(1)
        #有没费次数时
        if popText == "Comment sent!":
            assert("评论成功")
            self.poco(text="OK").click()
            sleep(1)
    #评星
    def startRating(self):
        self.poco("Bottom").child("Stars").child("Star3").click()
        sleep(1)
        assert_exists(Template(r"tpl1522211570186.png", record_pos=(-0.039, 0.443), resolution=(1440, 2560)), "评级成功")

    #输入评论文字
    def enterCommnet(self):
        self.poco("Placeholder").click()
        sleep(1)
        text("good!")
        self.poco1("android.widget.Button").click()
        sleep(1)

    #举报
    def reportLevel(self):
        self.poco(text="Report Stage").click()
        sleep(1)
        if self.poco("Toogle_EroticismOrPolitics").exists():
            assert("弹出举报弹框成功")
        self.poco(text="Cancel").click()
        sleep(1)
        if not self.poco("Toogle_EroticismOrPolitics").exists():
            assert("关闭举报弹框成功")
        self.poco(text="Report Stage").click()
        sleep(1)
        self.poco(text="Confirm").click()
        sleep(1)
        if self.poco("lable").get_text() == "You must choose an option!":
            assert("不选择理由无法举报成功")
            self.poco(text="OK").click()
            sleep(1)
        self.poco("Toogle_EroticismOrPolitics").click()
        sleep(1)
        assert_exists(Template(r"tpl1522225879391.png", record_pos=(-0.313, -0.301), resolution=(1440, 2560)),"选择色情/政治选项成功")
        self.poco("Toogle_Advertisement").click()
        sleep(1)
        assert_exists(Template(r"tpl1522225998289.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.138, -0.19), resolution=(1440, 2560)), "选择广告选项成功")
        self.poco("Toogle_Tort").click()
        sleep(1)
        assert_exists(Template(r"tpl1522226039045.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.159, -0.082), resolution=(1440, 2560)), "选择侵权选项成功")
        self.poco("Toogle_Other").click()
        sleep(1)
        assert_exists(Template(r"tpl1524907944782.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(-0.147, 0.032), resolution=(720, 1280)), "选择其它选项成")
        self.poco(text="Confirm").click()
        sleep(1)
        if self.poco("lable").get_text() == "Reason not specified!":
            assert("其他理由无文字不能举报")
            self.poco(text="OK").click()
            sleep(1)
        self.poco("InputField_OtherReason").child("Text").click()
        sleep(1)
        text("take")
        self.poco1("android.widget.Button").click()
        sleep(1)
        if self.poco("InputField_OtherReason").child("Text").get_text() == "take":
            assert("其它输入文字成功")
        self.poco("InputField_Desc").child("Text").click()
        sleep(1)
        text("bad")
        self.poco("InputField_OtherReason").child("Text").click()
        sleep(1)
        if self.poco("InputField_Desc").child("Text").get_text() == 'bad':
            assert("描述输入文字成功")
        self.poco(text="Confirm").click()
        sleep(1)
        if self.poco("lable").get_text() == "Reported":
            assert("举报成功")
            self.poco(text="OK").click()
            sleep(1)
        
    #长按弹出他人信息弹框
    def longPress(self):
        self.poco("Tree").child()[0].long_click()
        sleep(1)
        if self.poco("gotohomepage").exists():
            assert("弹出他人信息框成功")
            self.poco("share").sibling("Button").click()
            sleep(1)
            if not self.poco("gotohomepage").exists():
                assert("关闭他人信息框成功")
        self.poco("Tree").child()[0].child("thumbnail").click()
        sleep(1)
        self.poco(text="View author's homepage").click()
        self.poco("Text_Title").wait_for_appearance()
        sleep(1)
        if self.poco("Text_Title").exists():
            assert("查看他人信息成功")
            self.poco("Btn_Back").click()
            sleep(1)
            if not self.poco("Text_Title").exists():
                assert("退出他人信息界面成功")
        self.poco("Tree").child()[0].child("thumbnail").click()
        sleep(1)
        self.poco(text="Share this stage").click()
        sleep(1)
        if self.poco(text="Share this stage").get_text() == "Share this stage":
            assert("分享关卡弹出成功")
        #share功能
        if self.poco(text="Share").exists():
            self.poco(text="Share").click()
            sleep(1)
            if self.poco(text="Shared").get_text() == "Shared":
                assert("分享成功")
            #关闭分享
            self.poco("sharePopup(Clone)").child("BG").child("Button").click()
            sleep(1)
            if not self.poco(text="Share this stage").exists():
                assert("关闭分享关卡成功")
        else:
            self.poco.click([355.0/720, 924.0/1280])
            sleep(1)

    def getUserData(self):
        player = self.poco("ToUserInfo").child("Text").get_text()
        # mycoins = self.poco(texture="tongyong_jinbi").child("Text").get_text()
        return player



    def testRewardLevel(self):
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10001", "z123456")
        self.waitLogin()
        sleep(7)
        player = self.getUserData()
        #进入悬赏关卡
        self.enterReward()
        #查看帮助
        self.rewardHelp()
        #切换标签测试
        self.changeLabel()
        #列表滑动测试
        self.swipeList()
        #筛选测试
        #由于bug会复制filters，所以退出重进
        self.filterOpen()
        self.switchFliters()
        self.cancelAll()
        self.recoveryFilters()
        #由于bug会复制filters，所以退出重进
        self.poco("Return").click()
        sleep(1)
        self.poco("RewardLV").click()
        sleep(1)
        self.onlyMine(player)
        self.recoveryFilters()
        #具体关卡进入和退出
        self.enterOneReward()
        #进入评论
        self.poco("Tree").child()[0].child("Evaluate").click()
        sleep(1)
        #直接评论弹出星级不能为空
        self.comment()
        # #输入星级再评论弹出文字不能为空
        self.startRating()
        self.comment()
        # #输入文字再评论弹出评论成功
        self.enterCommnet()
        self.comment()
        #点赞和踩
        self.like()
        self.hate()
        #举报测试
        self.reportLevel()
        self.poco("Btn_Back").click()
        sleep(1)
        #长按测试
        self.longPress()



        stop_app("com.gameholic.drawsomethingbyspider")
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

        # simple_report("logs")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(RewardLevelCase("testRewardLevel"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
