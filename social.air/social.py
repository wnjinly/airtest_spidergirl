# -*- encoding=utf8 -*-
__author__ = "jingchuan.wei"
__title__ = "test social"
__desc__ = """
this is a test script.
用来测试社交模块
"""
from airtest.core.api import sleep,clear_app,wake,home,start_app,stop_app,snapshot,Template,exists,shell,assert_exists,using,text,touch,connect_device
# from airtest.report.report import simple_report
import sys
import time
sys.path.append("D:/test/spider/login.air")
using("D:/test/spider/rewardLevel.air")
from rewardLevel import RewardLevelCase
from login import Login
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import unittest
from poco.drivers.unity3d import UnityPoco
# from poco.drivers.unity3d import UnityPoco
# poco = UnityPoco()

class SocialCase(RewardLevelCase):
    # @classmethod
    # def setUpClass(cls):
    #     super(SocialCase, cls).setUpClass()

    # @classmethod
    # def tearDownClass(cls):
    #     super(SocialCase, cls).setUpClass()

    def enterSocial(self):
        self.poco("MSG").click()
        sleep(1)
        title = self.poco("Text_Title").get_text()
        if title == "Socail":
            print("enter social pass")


    def exitSocial(self):
        self.poco("Btn_Back").click()
        sleep(1)
        if not self.poco("Text_Title").exists():
            print("exit social pass")
        
    def socialHelp(self):
        self.poco("Explain").click()
        sleep(1)
        textHelp = self.poco("zi").child("txt").get_text()
        if "In Social you can" in textHelp:
            print("look help pass")
        self.poco("confirm").click()
        sleep(1)
        if not self.poco("zi").exists():
            print("close help pass")

    def swipeLebal(self):
        self.poco(text="Message").click()
        sleep(1)
        if self.poco(text="system").exists():
            print("swipe to message pass")
        self.poco(text="Friends").click()
        sleep(1)
        if self.poco("Page_Friend").exists():
            print("swipe to friends pass")
        else:
            print("swipe to friends failed")
        self.poco(text="Search").click()
        sleep(1)
        if self.poco("Btn_Search").exists():
            print("swipe to search pass")
        self.poco(text="Homepage").click()
        sleep(1)
        if self.poco("Page_HomePage").exists():
            print("swipe to homepage pass")

    def textOK(self):
        self.poco1 = AndroidUiautomationPoco()
        if self.poco1("android.widget.Button").exists():
            self.poco1("android.widget.Button").click()
            sleep(1)

    def clearText(self):
        self.poco("Btn_QuitSearch").click()
        sleep(1)
        self.poco("InputField").click()
        if self.poco("InputField").child("Text").get_text() == '':
            print("clear user ID pass")


    def textSearch(self, userId):
        self.poco("Toggle_Search").click()
        sleep(1)
        self.poco("InputField").click()
        sleep(1)
        text(userId)
        sleep(1)
        self.textOK()
        if self.poco("InputField").get_text() == userId:
            print("text user ID successfully")
        
    def search(self, userId):
        self.poco("Btn_Search").click()
        sleep(1)
        searchResult = self.poco("lable").get_text()
        if searchResult == "Can't find this player":
            print("can't find the userID pass")
            self.poco("BG").child("Button").child("Text").click()
            sleep(1)
        if self.poco("Text_PlayerId").exists():
            if self.poco("Text_PlayerId").get_text() == userId:
                print("search the user successfully")
            else:
                print("search result is wrong")
        else:
            print("search failed")
            
    def enterOtherHomePage(self):
        if self.poco("Player(Clone)").exists():
            self.poco("Player(Clone)").click()
            if self.poco("OtherHomePageUI(Clone)").exists():
                print("enter other home page successfully")
                
    def otherInfo(self):
        self.poco("Btn_InformPlayer").click()
        sleep(1)
        if self.poco("lable").get_text() == "Reported":
            print("report player pass")
        self.poco("BG").child("Button").click()
        sleep(1)
        if self.poco("lable").get_position() == [0.5, 0.5]:
            print("close the interface of report player successfully")
        
        if self.poco("Btn_AddFriend").exists():
            self.poco("Btn_AddFriend").click()
            if self.poco("lable").get_text() == "Invitation sent!":
                print("send invitation successfully")
                self.poco("BG").child("Button").click()
                sleep(1)
                if self.poco("lable").get_position() == [0.5, 0.5]:
                    print("close invitation successfully")
                    
    def exitOtherHomePage(self):
        self.poco("Bg").child("Top").child("Btn_Back").click()
        sleep(1)
        if not self.poco("Player(Clone)").exists():
            print("exit other home page successfully")
        

        
    def addFriend(self):
        self.poco("Toggle_Friend").click()
        sleep(3)
        if self.poco("Btn_Accept").exists():
            self.poco("Btn_Accept").click()
            sleep(1)
            if self.poco("Text_Friendid").get_text() == "1005339564":
                print("add friend successfully")

            
    def messagesList(self):
        sleep(5)
        items = self.poco("Bg").child("Scroll View").child("Content").child()
        contents = []
        for item in items:
            itemName = item.get_name()
            if itemName == "LeftMessage(Clone)":
                contents.append(item.child("Text_Content").get_text())
            if itemName == "RightMessage(Clone)":
                contents.append(item.child("Text_Content").get_text())
        return contents

    def receiveMessagesList(self):
        items = self.poco("Bg").child("Scroll View").child("Content").child()
        contents = []
        for item in items:
            if item.get_name() == "LeftMessage(Clone)":
                contents.append(item.child("Text_Content").get_text())
        # print(contents)
        return contents



    def sendMessage(self):
        if self.poco("Friend(Clone)").exists():
            self.poco("Friend(Clone)").click()
            sleep(3)
            if self.poco("Bg").child("Top").child("Text_Title").exists():
                print("open chat interface successfully")
            #输入英语
            self.poco("InputField").click()
            sleep(1)
            now = time.strftime('%H%M%S')
            englishInfo = "Hello" + now
            text(englishInfo)
            self.textOK()
            self.poco("Btn_Send").click()
            sleep(2)
            englishContents = self.messagesList()
            if englishContents[-1] == englishInfo:
                print("send english messages successfully")
            
            #输入中文
            self.poco("InputField").click()
            now1 = time.strftime('%H%M%S')
            chineseInfo = "你好" + now1
            text(chineseInfo)
            self.textOK()
            self.poco("Btn_Send").click()
            sleep(2)
            chineseContents = self.messagesList()
            if chineseContents[-1] == chineseInfo:
                print("send chinese successfully")
            return chineseInfo    
            
    def delFriend(self):
        sleep(1)
        self.poco("Btn_Delete").click()
        sleep(1)
        if "Are you sure" in self.poco("lable").get_text():
            print("open delete friend box successfully")
        self.poco("Cancel").click()
        sleep(1)
        if self.poco("lable").get_position() == [0.5, 0.5]:
            if self.poco("Text_Friendid").get_text() == "1007293172":
                print("cancel delete friend successfully")
        self.poco("Btn_Delete").click()
        sleep(1)
        self.poco("ConfirmBtn").click()
        sleep(1)
        if not self.poco("Text_Friendid").exists():
            print("delete friend successfully")

    def receiveMessages(self):
        self.poco("Toggle_Message").click()
        sleep(1)
        contents = []
        items = self.poco("Content").child()
        for item in items:
            if item.child("Text_FriendName").get_text() == "hj":
                item.click()
                sleep(3)
                contents = self.receiveMessagesList()
                return contents[-1]
                
                        


    def cannotSendMessage(self):
        self.poco("Toggle_Message").click()
        items = self.poco("Content").child()
        sleep(2)
        for item in items:
            if item.child("Text_FriendName").get_text() == "hj":
                item.click()
        sleep(3)
        if self.poco("Bg").child("Top").child("Text_Title").get_text() == "hj":
            print("enter friend's chat window successfully")
        self.poco("InputField").click()
        someWords = "Can not send" 
        text(someWords)
        sleep(1)
        self.textOK()
        self.poco("Btn_Send").click()
        sleep(1)
        contents = self.messagesList()
        if someWords not in contents:
            print("Can't send messages pass")

                        
    def receiveLevel(self):
        items = self.poco("Bg").child("Scroll View").child("Content").child()
        for item in items:
            if item.get_name() == "RightShare(Clone)":
                position = item.child("Btn_Accept").get_position()[1]
                while position < 0.1:
                    self.poco.swipe([270.0/540, 80.0/960], [270.0/540, 780.0/960])
                    sleep(2)
                    position = item.child("Btn_Accept").get_position()[1]   
                    
                item.child("Btn_Accept").click()
                sleep(3)
                if "You need to spend coins" in self.poco("lable").get_text():
                    print("pay window appears pass")
                    self.poco(text="Cancel").click()
                    sleep(1)
                    if not self.poco("lable").exists():
                        print("close pay window successfully")
                    self.poco("Bg").child("Scroll View").child("Content").child()[1].child("Btn_Accept").click()
                    sleep(3)
                    self.poco(text="OK").click()
                    sleep(2)
                    if self.poco("Hp").exists():
                        print("receive level invention successfully")
                        self.poco("Return2").click()
                        sleep(1)
                        if self.poco("lable").get_text() == "Are you sure you want to exit the game?":
                            print("exit level window appears pass")
                        self.poco(text="Cancel").click()
                        sleep(1)    
                        if not self.poco("lable").exists():
                            print("close exit level window pass")
                        self.poco("Return").click()
                        sleep(1)
                        self.poco(text="OK").click()
                        sleep(1)
                        if self.poco("InputField").exists():
                            print("exit level successfully")
                return
            else:
                print("no invite level")

    def ownLevel(self):
        #玩自己的关卡
        if self.poco("Btn_Play").exists():
            self.poco("Btn_Play").click()
        sleep(1)
        self.poco("ConfirmBtn").click()
        sleep(2)
        if self.poco("Hp").exists():
            print("enter your own level successfully")
            self.poco("Return").click()
            sleep(1)
            if self.poco("lable").get_text() == "Are you sure you want to exit the game?":
                print("exit level window appears pass")
            self.poco("Cancel").click()
            sleep(1)    
            if self.poco("lable").get_position() == [0.5, 0.5]:
                print("close exit level window pass")
            self.poco("Return").click()
            sleep(1)
            self.poco("ConfirmBtn").click()
            sleep(1)
            if self.poco("Text_Title").exists():
                print("exit level successfully")
        #查看评论
        
        if self.poco("Content").child("HisRewardLevel(Clone)")[0].child("Btn_Evaluate").exists():
            self.poco("Content").child("HisRewardLevel(Clone)")[0].child("Btn_Evaluate").click()
            sleep(1)
            if self.poco("Stars").exists():
                print("enter comments successfully")
            self.startRating()
            self.enterCommnet()
            self.comment()
            sleep(1)
            self.poco("Bg").child("Top").child("Btn_Back").click()
            sleep(1)
            if not self.poco("Stars").exists():
                    print("exit your level comments successfully") 

    def otherLevel(self):
        self.poco("Btn_ToFriendHomePage").click()
        sleep(2)
        if self.poco("OtherHomePageUI(Clone)").child("Bg").child("Top").child("Text_Title").get_text() == "hj's Homepage":
            print("open friend's info successfully")

        #玩别人的关卡
        if self.poco("Btn_Play").exists():
            self.poco("Btn_Play").click()
            sleep(2)
            self.poco("ConfirmBtn").click()
            sleep(2)
            if self.poco("HPimage").exists():
                print("enter friend's level successfullly")
            self.poco("Return").click()
            sleep(2)
            self.poco("ConfirmBtn").click()
            sleep(2)
            if not self.poco("HPimage").exists():
                print("exit friend's level successfully")
        #查看评论
        if self.poco("Btn_Evaluate").exists():
            self.poco("Btn_Evaluate").click()
            sleep(1)
            if self.poco("Stars").exists():
                print("enter comments successfully")
            self.startRating()
            self.enterCommnet()
            self.comment()
            self.poco("Bg").child("Top").child("Btn_Back").click()
            sleep(2)
            if not self.poco("Stars").exists():
                print("exit friend's comments successfully")
        self.poco("Bg").child("Top").child("Btn_Back").click()
        sleep(2)
                            


class Social(SocialCase): 

    # @classmethod
    # def setUpClass(cls):
    #     super(Social, cls).setUpClass()

    # @classmethod
    # def tearDownClass(cls):
    #     super(Social, cls).setUpClass()
    
    def setUp(self):

        # connect_device("android:///")
        # self.poco1 = AndroidUiautomationPoco(force_restart=False)
        stop_app("com.gameholic.drawsomethingbyspider")
        clear_app("com.gameholic.drawsomethingbyspider")
        wake()
        home()
        start_app("com.gameholic.drawsomethingbyspider")
        sleep(7)
        self.poco = UnityPoco()       


    def teardown(self): 
         stop_app("com.gameholic.drawsomethingbyspider")


    def testSocial(self):
        print("test social start")
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10001", "z123456")
        self.waitLogin()
        sleep(5)
        #进入社交,使用wn10001向10002申请好友
        self.enterSocial()
        #退出社交界面
        self.exitSocial()                         
        #查看帮助
        self.enterSocial()
        self.socialHelp()                        
        #切换标签
        self.swipeLebal()
        #查看自己发布的关卡                        
        self.ownLevel()
        #查找用户
        #输入错误信息，无法找到用户
        #输入错误信息，无法找到
        self.textSearch("32142")
        self.search("32142")
        self.clearText()
        #查找自己也无法找到信息
        self.textSearch("1005339564")
        self.search("1005339564")
        self.clearText()
        #输入wn10002的id，找到用户
        self.textSearch("1007293172")
        self.search("1007293172")
        #查看搜索到的用户信息
        self.enterOtherHomePage()
        self.otherInfo()
        #退出他人主页
        self.exitOtherHomePage()
        

    def testAddFriend(self): 
        print("test add friend start")
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10002", "z123456")
        self.waitLogin()
        sleep(5)
        #更换账号wn10002
        self.enterSocial()
        #添加好友
        self.addFriend()
        #聊天
        global message
        message = self.sendMessage()

    def testDelFriend(self):
        print("test del friend start")
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10001", "z123456")
        self.waitLogin()
        sleep(5)
        
        #更换账号wn10001
        self.enterSocial()
        receiveMessage = self.receiveMessages()
        if receiveMessage == message:
            print("receive message successfully")
        #查看他人信息
        self.otherLevel()
        self.poco("Bg").child("Top").child("Btn_Back").click()
        sleep(2)
        #删除好友
        self.poco("Toggle_Friend").click()
        sleep(3)
        self.delFriend()
        # #删除好友无法发送信息
        self.cannotSendMessage()
        #接收关卡邀请
        self.receiveLevel()
        #退出聊天
        self.poco("Bg").child("Top").child("Btn_Back").click()
        sleep(1)
        if self.poco("Toggle_Message").exists():
            print("exit chat window successfully")

        #退出社交界面
        self.exitSocial() 

        # stop_app("com.gameholic.drawsomethingbyspider")
        # sleep(2.0)
        # snapshot(msg="app stopped")
        print("social finish test")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    message = "start"
    suite.addTest(Social("testSocial"))
    suite.addTest(Social("testAddFriend"))
    suite.addTest(Social("testDelFriend"))
    runner = unittest.TextTestRunner()
    runner.run(suite)



