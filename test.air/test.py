#coding=utf-8
__author__ = "Administrator"



# from airtest.core.api import using
from poco.drivers.unity3d import UnityPoco
# import sys,os
# import locale,codecs
# using("D:/test/spider/test.air")




poco = UnityPoco()

if poco("Content").child("HisRewardLevel(Clone)")[0].child("Btn_Evaluate").exists():
    poco("Content").child("HisRewardLevel(Clone)")[0].child("Btn_Evaluate").click()