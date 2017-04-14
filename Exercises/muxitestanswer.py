# -*- coding: utf-8 -*-

#=============================== Test 1 ======================================
class Message:
    def __init__(self, message, sender, receivers):
        self.sender = sender
        self.message = message
        self.receivers = receivers


class User:
    pass


class ChinaUser(User):
    tcountry = "China"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def create_room(roomno, users):
        return Room(roomno, users)

    @classmethod
    def country(cls):
        print("系统提示：你来自{}".format(cls.tcountry))

    def self_intro(self):
        return "我的名字是{},我的年龄是{}岁".format(self.name, self.age)

    def send_msg(self, msg, receivers, room):
        room.show_msg(Message(msg, self.name, receivers))


class Room:
    def __init__(self, roomno, users):
        self.roomno = roomno
        self.users = users
        print("系统提示：已创建房间：{}".format(self.roomno))

    def show_msg(self, msg):
        if msg.sender not in self.users:
            print("系统提示：你不在这个聊天室中！")
            return
        recs = []
        for i in msg.receivers:
            if i not in self.users:
                recs.append(i)
        if len(recs)!=0:
            print("系统提示：{}不在这个聊天室中！".format(recs))
            return
        print("{}-->{}:{}".format(msg.sender, msg.receivers, msg.message))


mary = ChinaUser("Mary", 16)
lily = ChinaUser("Lily", 15)
tom = ChinaUser("Tom", 18)
someone = ChinaUser("Someone", None)
someone2 = ChinaUser("Someone2", None)

room304 = mary.create_room(304, [mary.name, tom.name, lily.name])
mary.send_msg("你好, 世界！", [tom.name, lily.name], room304)
tom.country()
lily.send_msg(lily.self_intro(), ["Tom"], room304)
lily.send_msg(lily.self_intro(), ["Someone", "Someone2"], room304)
someone.send_msg("你好！", [tom.name], room304)


#=============================== Test 2 ======================================
"""
Compose three classes and run the test
Class User:
    * attributes:
      * ucountry:(default=None)
    * methods:
      * smethod() No arguments; print "Just a normal user"
      * cmethod(cls) arguments: cls; print "Nationality: <uncountry>"
      * hello(self) arguments: self; print "Hello, I'm User", no newline

Class ChineseUser, extends Class User
    * attributes:
      * uncountry:(default="China")
    * methods:
      * hello(self) arguments: self; extends User's hello() and print ", and I'm ChineseUser", no newline

Class RussianUser, extends Class User
    * attributes:
      * uncountry:(default="Russia")
    * methods:
      * hello(self) arguments: self; extends User's hello() print ", and I'm RussianUser", no newline

Class ChineseRussianUser, extends Class ChineseUser and Class RussianUser:
    * attributes:
      * ucountry:(default="China && Russia")
    * methods:
      * smethod(self) extends User's smethod()
      * cmethod(self) extends User's cmethod
      * hello(self) extends ChineseUser's and RussianUser's hello() and print ". So, I'm ChineseRussianUser"

Test:
    u = ChineseRussianUser()
    u.hello()
    u.smethod()
    u.cmethod()

Result:
    Hello, I'm User, and I'm RussianUser, and I'm ChineseUser. So, I'm ChineseRussianUser
    Just a normal User
    Nationality: China&&Russia
"""

class User:
    ucountry = None

    @staticmethod
    def smethod():
        print("Just a normal User")

    @classmethod
    def cmethod(cls):
        print("Nationality: {}".format(cls.ucountry))

    def hello(self):
        print("Hello, I'm User", end="")


class ChineseUser(User):
    ucountry = 'China'

    def hello(self):
        super().hello()
        print(", and I'm ChineseUser", end="")


class RussianUser(User):
    ucountry = 'Russia'

    def hello(self):
        super().hello()
        print(", and I'm RussianUser", end="")


class ChineseRussianUser(ChineseUser, RussianUser):
    ucountry = "China&&Russia"

    def smethod(self):
        super().smethod()

    def cmethod(self):
        super().cmethod()

    def hello(self):
        super().hello()
        print(". So, I'm ChineseRussianUser")


u = ChineseRussianUser()
u.hello()
u.smethod()
u.cmethod()
