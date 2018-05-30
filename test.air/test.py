#coding=utf-8
__author__ = "Administrator"



# from airtest.core.api import using
from poco.drivers.unity3d import UnityPoco
# import sys,os
# import locale,codecs
# using("D:/test/spider/test.air")
poco = UnityPoco()

def messagesList():
    items = poco("Bg").child("Scroll View").child("Content").child()
    for item in items:
        if item.get_name() == "RightShare(Clone)":
            position = item.child("Btn_Accept").get_position()[1]
            print(position)
            while position < 0.1:
                poco.swipe([270.0/540, 80.0/960], [270.0/540, 780.0/960])
                sleep(2)
                position = item.child("Btn_Accept").get_position()[1]   
            item.child("Btn_Accept").click()
            return
        else:
            print("no invite level")
messagesList()