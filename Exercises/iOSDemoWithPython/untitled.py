#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ctypes import cdll
from ctypes import util
from rubicon.objc import ObjCClass, objc_method
# 载入Foundation框架
cdll.LoadLibrary(util.find_library('Foundation'))
# 获取NSArray类
NSArray = ObjCClass("NSArray")
# 等同于 
# NSArray *myArray = [NSArray arrayWithObjects:@"ok", @"ok1", @"ok2", nil]
myArray = NSArray.arrayWithObjects_("ok", "ok1", "ok2", None)

print myArray.count
print myArray.indexOfObject_("ok2")

