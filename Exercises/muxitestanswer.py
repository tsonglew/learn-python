# -*- coding: utf-8 -*-


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
