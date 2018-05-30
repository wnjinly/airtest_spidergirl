# -*- encoding=utf8 -*-
__author__ = "jingchuan.wei"
__title__ = "login"
__desc__ = """
this is a test login script.
"""

# start your script here
from airtest.core.api import sleep,text,shell,home,wake,clear_app,stop_app,start_app,connect_device
# from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.unity3d import UnityPoco

import unittest

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect_device("android:///")
        cls.poco1 = AndroidUiautomationPoco(force_restart=False)

    
    @classmethod
    def tearDownClass(cls):
        stop_app("com.gameholic.drawsomethingbyspider")

    
    def setUp(self):
        stop_app("com.gameholic.drawsomethingbyspider")
        clear_app("com.gameholic.drawsomethingbyspider")
        wake()
        home()
        start_app("com.gameholic.drawsomethingbyspider")
        sleep(7)
        self.poco = UnityPoco()
        print("test start")

    #自动更新函数
    def permissionClick(self):
        self.poco1 = AndroidUiautomationPoco()
        while self.poco1("com.android.packageinstaller:id/permission_message").exists():
            self.poco1("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(1)
        
    def autoUpdate(self):
        # self.poco = UnityPoco()
        sleep(2)
        loadingTime = 0
        try:
            while self.poco("tip1").exists():
                sleep(5)
                loadingTime += 5
                if loadingTime >= 300:
                    if "url" in self.poco("error").get_text():
                        print("更新失败")
                        stop_app("com.gameholic.drawsomethingbyspider")
                    else:
                        sleep(5)
        except RuntimeError as e:
            raise e
        
    #登录函数
    def login(self, username, password):
        self.poco1 = AndroidUiautomationPoco()
        if self.poco1(text="Sign in").exists():
            self.poco1(text="Sign in").click()
            sleep(1.0)
            self.poco1("android.widget.LinearLayout").offspring("android.widget.RelativeLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout").child("android.widget.ImageView").click()
            sleep(1)
            self.poco1(text="Username").click()
            sleep(1)
            text(username)
            sleep(1)
            self.poco1("android.widget.LinearLayout").offspring("android.widget.RelativeLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout")[2].child("android.widget.EditText").click()
            sleep(1)
            #有的手机text()方法不起作用
            shell("input keyboard text %s"%password)
            shell("input keyevent 4")
            sleep(1)
            self.poco1("android.widget.LinearLayout").offspring("android.widget.RelativeLayout").child("android.widget.LinearLayout").child("android.widget.LinearLayout")[3].child("android.widget.TextView").click()
            sleep(7)
        else:
            print("登录弹框未出现")
            start_app("com.gameholic.drawsomethingbyspider")
            
    def waitLogin(self):
        # self.poco = UnityPoco()
        while self.poco("Text_Percent").exists():
            sleep(5)
        if self.poco("FBIWorning(Clone)").exists():
            self.poco("FBIWorning(Clone)").click()  
        #检查是否存在离线金币，存在关闭
        if self.poco("CoinNum").exists():
            print("offline coin existed")
            self.poco.click([540.0/1080, 1210.0/1920])
        if self.poco("StartGame").child().get_text() == "基础关卡":
            self.poco("Setting").click()
            sleep(1)
            if self.poco("SurprisePopup").child("Image").exists():
                self.poco("SurprisePopup").child("Image").child("Cancel").click()
                sleep(1)
            self.poco("Arrow").click()
            sleep(1)
            self.poco("Item 0: English").child("Item Label").click()
            sleep(1)
            self.poco("option_top_x").click()
            sleep(1)
        if self.poco("StartGame").child().get_text() == "Basic Stage":
            print("login successfully!")
                    
    def testLogin(self):
        self.permissionClick()
        self.autoUpdate()
        self.login("wn10001", "z123456")
        self.waitLogin()
    
if __name__ == '__main__':
    unittest.main() 
  

