# -*- encoding=utf8 -*-
__author__ = "jingchuan.wei"
__title__ = "test shop"
__desc__ = """
this is a test script.
用来测试商店UI
"""
    
# start your script here
from airtest.core.api import sleep,clear_app,wake,home,start_app,stop_app,snapshot,Template,exists,shell,assert_exists
from airtest.report.report import simple_report
import sys
sys.path.append("D:/test/spider/login.air")
from login import init_device,autoUpdate,login,permissionClick,waitLogin
from poco.drivers.unity3d import UnityPoco




def buy():
    poco = UnityPoco()
    #确定购买
    poco("Tree").child("ShopProp(Clone)")[0].child("BuyIt").click()
    sleep(1)
    poco(text="OK").click()
    sleep(5)
    #弹出sdk界面
    if poco("lable").exists():
        if poco("lable").get_text() == "Top-up failed:3:Billing Unavailable":
            print("内网无法购买")
            poco(text="Confirm").click()
            sleep(1)
    if poco(text="You got").exists():
        print("购买成功")        
        while poco("xxxxxxxx").child("Text").exists():
            poco("xxxxxxxx").child("Text").click()
            sleep(1)
    if poco(text="Not enough diamonds!").exists():
        if poco(text="Not enough diamonds!").get_text() == "Not enough diamonds!":
            print("钻石不足无法购买")
            poco("copypop").child("BG").child("Button").child("Text").click()

    if poco(text="Not enough coins！").exists():
        if poco(text="Not enough coins！").get_text() == "Not enough coins！":
            print("金币不足无法购买")
            poco("copypop").child("BG").child("Button").child("Text").click()
            
    if exists(Template(r"tpl1522392116057.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.215, -0.074), resolution=(1440, 2560))):
        print("弹出购买sdk界面成功")
        #购买失败
        shell("input keyevent 4")
        assert_exists(Template(r"tpl1522392162168.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, 0.023), resolution=(1440, 2560)), "取消购买成功")
        print("购买成功请手动测试")
    if exists(Template(r"tpl1522399084096.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, 0.015), resolution=(1440, 2560))):
        print("内网钻石无法购买成功")





def runTest():
    stop_app("com.gameholic.drawsomethingbyspider")
    clear_app("com.gameholic.drawsomethingbyspider")
    wake()
    home()
    start_app("com.gameholic.drawsomethingbyspider")
    sleep(7)
    permissionClick()
    autoUpdate()
    login("wn10001", "z123456")
    waitLogin()
    sleep(5)
    poco = UnityPoco()


    #进入商店
    poco("Shop").click()
    sleep(1)
    #关闭购买去广告提示弹框

    if poco("BitchPopup").child("Image").child("Image").exists():
        print("弹出支付去广告成功")
        poco("Button").child("Text").click()
        if not poco("BitchPopup").child("Image").child("Image").exists():
            print("关闭弹框成功")
        sleep(1)
    #关闭商店
    poco("Return").click()
    sleep(1)
    if not poco(text="Limited").exists():
        print("退出商店成功")
    poco("Shop").click()
    sleep(1)
    #关闭购买去广告提示弹框
    if poco("BitchPopup").child("Image").child("Image").exists():
        print("弹出支付去广告成功")
        poco("Button").child("Text").click()
        sleep(1)
    #切换标签和购买
    #切换所有标签
    poco(text="Gift").click()
    sleep(1)
    if poco("PropName").get_text() == "Marvellous Gift":
        print("切换礼物标签成功")
    poco("Text (2)").click()
    sleep(1)
    if poco("PropName").get_text() == "Speed-up":
        print("切换到道具标签成功")
    poco(text="Diamonds").click()
    sleep(1)
    if poco(text="Super Gems Pack").get_text() == "Super Gems Pack":
        print("切换钻石标签成功")
    poco(text="Limited").click()
    sleep(1)
    if not poco("PropName").exists():
        print("切换到礼包标签成功")
    poco(text="Monster").click()    
    sleep(1)
    if poco(text="Green Fluffy").get_text() == "Green Fluffy":
        print("切换到怪物标签成功")
    #滑动列表
    poco(texture="monster_A1_1").wait_for_appearance()
    poco(texture="monster_A1_1").click()
    beforSwipe = poco(texture="monster_A1_1").get_position()
    
    poco.swipe([300.0/576, 850.0/1024],[300.0/576, 150.0/1024])
    sleep(2)
    afterSwipe = poco(texture="monster_A1_1").get_position()
    if beforSwipe != afterSwipe:
        print("滑动列表成功")
    else:
        print("滑动列表失败")
    #滑动回顶部
    poco.swipe([300.0/576, 150.0/1024],[300.0/576, 850.0/1024])
    sleep(2)
    #购买逻辑
    poco("Tree").child("ShopProp(Clone)")[0].child("BuyIt").child("Text").click()
    sleep(2)
    buyConfirm = poco("lable").get_text()
    if buyConfirm == "Confirm to purchase":
        print("打开确认购买弹框成功")
    #取消购买
    poco(text="Cancel").click()
    sleep(1)
    if not poco(text="Confirm to purchase").exists():
        print("取消购买成功")
    #wn10001购买怪物成功
    buy()
    #切换到钻石标签查看sdk调出
    poco(text="Diamonds").click()
    sleep(1)
    if poco(text="Super Gems Pack").get_text() == "Super Gems Pack":
        print("切换钻石标签成功")
    buy()

    #完成测试
    stop_app("com.gameholic.drawsomethingbyspider")
    sleep(2.0)
    snapshot(msg="app stopped")
    print("shop finish test")

    # simple_report("logs")
if __name__ == "__main__":
    runTest()
    
# runTest()
# buy()

