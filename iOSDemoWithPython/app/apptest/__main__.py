from __future__ import absolute_import, division, print_function, with_statement

import sys

from ctypes import cdll, c_int, c_void_p, util
from rubicon.objc import ObjCClass, objc_method
from rubicon.objc.core_foundation import from_value, to_value

__all__ = ('UIKit', 'ObjCClass', 'objc_method', 'NSObject',
           'UIScreen', 'UIView', 'UIViewController','UIResponder',
           'UIWindow', 'UIColor', 'UILabel')

UIKit = cdll.LoadLibrary(util.find_library('UIKit'))
UIKit.UIApplicationMain.restypes = (c_int, c_void_p, c_void_p,
                                    c_void_p)
UIKit.UIApplicationMain.restype = c_int

for item in __all__:
    if item not in globals():
        globals()[item] = ObjCClass(item)


class ObjCAppDelegate(NSObject):
    @objc_method('@B')
    def application_didFinishLaunchingWithOptions_(self, launchOptions):
        self.__dict__['delegate'] = PyAppDelegate()
        return 0


class PyAppDelegate(object):
    def __init__(self):
        self.window = UIWindow.alloc().initWithFrame_(UIScreen.mainScreen().bounds)
        
        view_controller = UIViewController.alloc().init()
        view_controller.view.setBackgroundColor_(UIColor.colorWithWhite_alpha_(0.5, 1))

        label = UILabel.alloc().initWithFrame_(view_controller.view.bounds)
        
        label.setText_("test, this is a label")
        label.setTextAlignment_(1)
        label.setTextColor_(UIColor.colorWithRed_green_blue_alpha_(30/255., 70/255., 137/255., 1))
        view_controller.view.addSubview_(label)

        self.window.rootViewController = view_controller
        self.window.makeKeyAndVisible()


if __name__ == '__main__':
    sys.exit(UIKit.UIApplicationMain(0, None, None, from_value('ObjCAppDelegate')))
