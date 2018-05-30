# -*- encoding=utf8 -*-
__author__ = "jinghcuan.wei"
__title__ = "test make level"
__desc__ = """
this is a test script.
用来测试制作关卡
"""

# start your script here
from airtest.core.api import sleep,clear_app,wake,home,start_app,stop_app,snapshot,Template,exists,shell,assert_exists
from airtest.report.report import simple_report
import sys
import time
from airtest.core.api import text,touch
sys.path.append("D:/test/spider/login.air")
from login import init_device,autoUpdate,login,permissionClick,waitLogin
from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from pocounit.case import PocoTestCase

class MakeLvCase(PocoTestCase):
    @classmethod
    def setUpClass(cls):
        init_device()
        cls.poco = UnityPoco()

    def enterMakelevel(self):
        # self.poco = UnityPoco()
        self.poco("MakeLV").click()
        sleep(1)
        if self.poco("Up").child("Text").exists():
            print("enter make level successfully")

    def lookHelp(self):
        # self.poco = UnityPoco()
        self.poco("Explain").click()
        sleep(1)
        if self.poco("txt").exists():
            print("look help interface successfully")
            self.poco(text="OK").click()
            if not self.poco("txt").exists():
                print("exit help interface successfully")

    def exitMylevel(self):
        # self.poco = UnityPoco()
        self.poco("Return").click()
        sleep(2)
        if not self.poco(text="My level").exists():
            print("exit my level interface successfully")

    def swipeMylevel(self):
        # self.poco = UnityPoco()
        if len(self.poco("Tree").child().nodes) >= 5:
            self.poco("Tree").child()[0].child("idtext").get_position()

            beforeSwipe = self.poco("Tree").child()[0].child("idtext").get_position()
            self.poco.swipe([100.0 / 1920, 100.0 / 1080], [100.0 / 1920, -200.0 / 1080])
            sleep(2)
            afterSwipe = self.poco("Tree").child()[0].child("idtext").get_position()
            if beforeSwipe != afterSwipe:
                print("swipe successfully")
            else:
                print("swipe failed")


    def addLevel(self):
        # self.poco = UnityPoco()
        self.poco("PlayerMakeLevel").click()
        if self.poco(text="Disclaimer").exists():
            print("open disclaimer interface successfully")

    def closeDisclaimer(self):
        # self.poco = UnityPoco()
        self.poco(text="Cancel").click()
        sleep(1)
        if not self.poco(text="Disclaimer").exists():
            print("close disclaimer successfully")


    def agreeDisclaimer(self):
        # self.poco = UnityPoco()
        self.poco(text="I Agree").click()
        sleep(1)
        if self.poco(text="Choose from album").exists():
            print("enter make level interface successfully")

    def switchLebel(self):
        # self.poco = UnityPoco()
        self.poco(text="Monster").click()
        sleep(1)
        if self.poco("SetMonster_D").exists():
            print("switch to monster interface successfully")
        self.poco(text="Publish").click()
        sleep(1)
        if self.poco("Save_Releaseit").exists():
            print("switch to publish interface successfully")
        self.poco(text="Background").click()
        sleep(1)
        if self.poco(text="Choose from album").exists():
            print("switch to background interface successfully")

    def closeMakeLevel(self):
        # self.poco = UnityPoco()
        self.poco("Return").click()
        sleep(2)
        if not self.poco(text="Background").exists():
            print("close make level interface successfully")


    def chooseAlbum(self):
        self.poco(text="Choose from album").click()
        sleep(5)
        self.poco1 = AndroidUiautomationPoco(force_restart=False)
        if self.poco1("android.widget.TextView").exists():
            print("open album successfully")
        shell("input keyevent 4")   #关闭选择图片
        if not self.poco1("android.widget.TextView").exists():
            print("close album successfully")

    def takePhotos(self):
        self.poco(text="Take a photo").click()
        sleep(5)
        self.poco1 = AndroidUiautomationPoco(force_restart=False)
        if self.poco1("com.google.android.GoogleCamera:id/shutter_button").exists():
            print("open camera successfully")
            shell("input keyevent 4") 
        if not self.poco1("com.google.android.GoogleCamera:id/shutter_button").exists():
            print("close camera successfully")

    def addSuccessfully(self):
        #红米note2
        self.poco(text="Take a photo").click()
        sleep(5)
        self.poco1 = AndroidUiautomationPoco(force_restart=False)
        if self.poco1("com.android.camera:id/v6_shutter_button_internal").exists():
            self.poco1("com.android.camera:id/v6_shutter_button_internal").click()
            sleep(1)
            self.poco1("com.android.camera:id/v6_btn_done").wait_for_appearance()
            if self.poco1("com.android.camera:id/v6_btn_done").exists():
                self.poco1("com.android.camera:id/v6_btn_done").click()
                sleep(5)
            if self.poco1("com.miui.gallery:id/wallpaper_apply").exists():
                self.poco1("com.miui.gallery:id/wallpaper_apply").click()
                sleep(1)
    @classmethod
    def addMonster(self):
        # self.poco = UnityPoco()
        self.poco(text="Monster").click()
        sleep(1)
        #添加怪物预览
        if self.poco("Tree").child().exists():
            self.poco("Tree").child()[0].click()
            sleep(1)
        if self.poco("usedlingdaoli").get_text() != 0:
            print("add monster successfully")
        self.poco(text="Preview").click()
        sleep(2)
        if self.poco("Mask").exists():
            print("preview successfully")
            self.poco.click([0.1,0.1])
            sleep(2)
            if not self.poco("Mask").exists():
                print("exit preview successfully")
        #滑动怪物选择，添加超出统率力情况
        if self.poco("Monster_1122").exists():
            self.swipeMonster()
        self.poco(text="Reset monster").click()
        sleep(1)
        if self.poco("usedlingdaoli").get_text() == 0:
            print("reset ok")
        self.poco("Monster_1001").click()


    @classmethod
    def swipeMonster(self):
        # self.poco = UnityPoco()
        self.poco.swipe([1000.0 / 1080, 1660.0 / 1920], [10.0 / 1080, 1660.0 / 1920], duration=0.2)
        sleep(2)
        pos = self.poco("Monster_1122").get_position()
        if min(pos) > 0:
            for _ in range(3):
                self.poco("Monster_1122").click()
                sleep(1)
            if "Your leadership is not" in self.poco("lable").get_text():
                print("leadership not enough ok")
                self.poco(text="OK").click()
                sleep(1)
                if not self.poco("lable").exists():
                    print("close leadership not enough interface successfully")
            self.poco(text="Reset monster").click()
            self.poco.swipe([10.0 / 1080, 1660.0 / 1920],[1000.0 / 1080, 1660.0 / 1920], duration=0.2)
            
            
    def switchPrivacy(self):
        # self.poco = UnityPoco()
        self.poco(text="Public").click()
        sleep(1)
        assert_exists(Template(r"D:/test/spider/makeLevel.air/tpl1526632435537.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.384, -0.207), resolution=(576, 1024)), "switch to Open pass")
        self.poco("OnlyFriend").click()
        sleep(1)
        assert_exists(Template(r"D:/test/spider/makeLevel.air/ttpl1526632538433.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.295, -0.127), resolution=(576, 1024)), "switch to Just pass")
        self.poco("OnlyMe").click()
        sleep(1)
        assert_exists(exists(Template(r"D:/test/spider/makeLevel.air/ttpl1526632587864.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.267, -0.042), resolution=(576, 1024))), "switch to Publicity pass")

    def textLevelInfo(self):
        # self.poco = UnityPoco()
        self.poco("LvNameInput").click()
        sleep(1)
        now = time.strftime('%H%M%S')
        global title
        title = "test" + now
        text(title)
        self.poco1 = AndroidUiautomationPoco(force_restart=False)
        if self.poco1("android.widget.Button").exists():
            self.poco1("android.widget.Button").click()
        self.poco("DesInput").click()
        des = "make at " + now
        text(des)
        if self.poco1("android.widget.Button").exists():
            self.poco1("android.widget.Button").click()
        self.poco("Save_Releaseit").click()

                
    def publish(self):
        # self.poco = UnityPoco()
        self.poco(text="Publish").click()
        sleep(1)
        self.poco("Save_Releaseit").click()
        sleep(1)
        popupText = self.poco("lable").get_text()
        #提交成功
        if  "Your stage has" in popupText:
            print("make a level successfully")
            self.poco(text="OK").click()
            sleep(2)
            if self.poco(text="My level").exists():
                print("return to my level ok")
        #缺少怪物
        if popupText == "The stage must contain a monster":
            print("no monster can't make a level ok")
            self.poco("BG").child("Button").click()
            sleep(1)
            self.addMonster()
        #缺少背景图
        if popupText == "The stage must contain a background image":
            print("no backgroud can't make a level")
            self.poco("BG").child("Button").click()
            sleep(1)
            #切换background标签
            self.poco(text="Background").click()
            sleep(1)
            #添加背景
            #使用相册
            self.chooseAlbum()
            #使用相机
            self.takePhotos()
            #成功添加背景
            self.addSuccessfully()
        #缺少名字
        if popupText == "The stage must have a name":
            print("no name can't make a level pass")
            self.poco("BG").child("Button").click()
            #添加名称
            self.textLevelInfo()


    def modifyLevel(self):
        # self.poco = UnityPoco()
        if self.poco("Tree").child()[0].exists():
            self.poco("Tree").child()[0].child("Lvupdate").child("Text").click()

            sleep(1)
            if self.poco(text="Background").exists():
                print("enter modify interface successfully")
            self.poco(text="Publish").click()
            sleep(1)
            self.poco("Save_Releaseit").click()
            sleep(1)
            popupText = self.poco("lable").get_text()
            if "You have successfully modified" in popupText:
                print("modified level successfully")
                self.poco(text="OK").click()
                sleep(1)

    def updatePrivacy(self):
        # self.poco = UnityPoco()
        self.poco("Tree").child()[0].child("Lvmode").child("Label").click() 
        sleep(1)
        self.poco("Item 1: Friends only ").click()
        sleep(1)
        if self.poco("lable").get_text() == "Stage changed successfully":
            print("update to friends only ok")
            self.poco(text="OK").click()
        self.poco(text="Friends only ").click()
        sleep(1)
        self.poco("Item 2: Only yourself").click()
        sleep(1)
        if self.poco("lable").get_text() == "Stage changed successfully":
            print("update to only yourself ok")
            self.poco(text="OK").click()
        self.poco(text="Only yourself").click()
        sleep(1)
        self.poco("Item 0: Public").click()
        sleep(1)
        if self.poco("lable").get_text() == "Stage changed successfully":
            print("update to public ok")
            self.poco(text="OK").click()

    def deleteLevel(self):
        # self.poco = UnityPoco()
        self.poco("Tree").child()[0].child("Lvdelete").child("Text").click()
        sleep(1)
        if self.poco("lable").get_text() == "Please confirm to delete this stage":
            print("open delete interface successfully")
            self.poco(text="Cancel").click()
            sleep(1)
            if not self.poco("lable").exists():
                print("close delete interface successfully")
        beforeDelete = len(self.poco("Tree").child().nodes)
        self.poco("Tree").child()[0].child("Lvdelete").child("Text").click()
        sleep(1)
        self.poco("ConfirmBtn").click()
        sleep(2)
        afterDelete = len(self.poco("Tree").child().nodes)
        if (afterDelete + 1) ==  beforeDelete:
            sleep(1)
            print("delete level pass")
        
    
#python运行去除注释，设置生成报告文件夹
# set_logdir("logs")




    def runTest(self):
        # init_device()
        permissionClick()
        autoUpdate()
        login("wn10001", "z123456")
        waitLogin()
        sleep(5)
        # self.poco = UnityPoco()
        # global self.poco
        #进入制作关卡
        self.enterMakelevel()
        #查看帮助
        self.lookHelp()
        #退出关卡
        self.exitMylevel()
        #再次进入制作关卡
        self.enterMakelevel()
        #内网可以测试滑动我的关卡
        self.swipeMylevel()
        #添加关卡
        self.addLevel()
        #关闭免责声明
        self.closeDisclaimer()
        self.addLevel()
        #同意免责声明
        self.agreeDisclaimer()
        #测试切换标签
        self.switchLebel()
        #关闭制作关卡
        self.closeMakeLevel()
        self.addLevel()
        self.agreeDisclaimer()
        #发布关卡缺少怪物失败,添加怪物
        self.publish()
        #发布关卡缺少背景失败，添加背景
        self.publish()
        #发布关卡缺少名称失败，添加名称
        self.publish()
        #发布成功
        self.publish()
        #测试关卡修改
        self.modifyLevel()
        self.updatePrivacy()
        self.swipeMylevel()
        self.deleteLevel()


        #结束测试
        stop_app("com.gameholic.drawsomethingbyspider")
        sleep(2.0)
        snapshot(msg="app stopped")
        print("finish test")

    #生成报告
    # simple_report("logs")
if __name__ == "__main__":
    import pocounit
    pocounit.main()
    
# self.poco = UnityPoco()
# runTest()

