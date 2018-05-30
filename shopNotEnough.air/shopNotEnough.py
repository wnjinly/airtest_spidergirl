# -*- encoding=utf8 -*-
__author__ = "jingchuan.wei"
__title__ = "test shop"
__desc__ = """
this is a test script.
用来测试商店UI
"""
    
# start your script here
from airtest.core.api import sleep,clear_app,wake,home,start_app,stop_app,snapshot
from airtest.report.report import simple_report
import sys
sys.path.append("D:/test/spider/login.air")
sys.path.append("D:/test/spider/shop.air")
from login import init_device,autoUpdate,login,permissionClick,waitLogin
from shop import buy
from poco.drivers.unity3d import UnityPoco

def runTest():
    stop_app("com.gameholic.drawsomethingbyspider")
    clear_app("com.gameholic.drawsomethingbyspider")
    wake()
    home()
    start_app("com.gameholic.drawsomethingbyspider")
    sleep(7)
    permissionClick()
    autoUpdate()
    login("wn10003", "z123456")
    waitLogin()
    sleep(5)
    poco = UnityPoco()

    #进入商店
    poco("Shop").click()
    sleep(1)
    #惊喜关卡关闭
    if poco(text="What a surprise!").exists():
        poco(text="No").click()
    #关闭购买去广告提示弹框

    if poco("BitchPopup").child("Image").child("Image").exists():
        assert("弹出支付去广告成功")
        poco("Button").child("Text").click()
        sleep(1)
    poco(text="Monster").click() 
    sleep(1)
    if poco(text="Green Fluffy").get_text() == "Green Fluffy":
        print("切换到怪物标签成功")

    buy()
    poco(text="Gift").click()
    sleep(1)
    if poco("PropName").get_text() == "Marvellous Gift":
        print("切换礼物标签成功")
    sleep(1)
    buy()
    poco("Return").click()
    sleep(2)

    #完成测试
    stop_app("com.gameholic.drawsomethingbyspider")
    sleep(2.0)
    snapshot(msg="app stopped")
    print("shop finish test")
    
if __name__ == "__main__":
    runTest()
    
runTest()
