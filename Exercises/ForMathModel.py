# -*- coding: utf-8 -*-

"""
例1 混合泳接力队的选拔
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              5名候选人的百米成绩
           甲       乙       丙       丁       戊
  蝶泳   1'06"8   57"2     1'18"    1'10"    1'07"4
  仰泳   1'15"6   1'06"    1'07"8   1'14"2   1'11"
  蛙泳   1'27"    1'06"4   1'24"6   1'09"6   1'23"8
 自由泳  58"6     53"      59"4     57"2     1'02"4

~~~~~~~~~~~~~~~~~~穷举所有的组队方案~~~~~~~~~~~~~~~~

选择语言: Python
"""

# 各种泳姿所有人的成绩列表，依次为甲、乙、丙、丁、戊(单位：秒)
Butterfly = [66.8, 57.2, 78, 70, 67.4]
Backstrock = [75.6, 66, 67.8, 74.2, 71]
Frog = [87, 66.4, 84.6, 69.6, 83.8]
Free = [58.6, 53, 59.4, 57.2, 62.4]

# 储存所有最终成绩的列表
Result = []

def func():
    print "甲记作1，乙记作2，丙记作3，丁记作4，戊记作5"
    flag = 1
    for a in Butterfly:
        for b in Backstrock:
            if Backstrock.index(b) == Butterfly.index(a):
                continue
            for c in Frog:
                if Frog.index(c) == Backstrock.index(b) \
                        or Frog.index(c)  == Butterfly.index(a):
                    continue
                for d in Free:
                    if Free.index(d) == Frog.index(c) \
                            or Free.index(d) == Backstrock.index(b) \
                            or Free.index(d)  == Butterfly.index(a):
                                continue
                    time = a + b + c + d
                    Result.append(time)
                    print "第", flag, "种", ".蝶泳第", Butterfly.index(a)+1, "个人",
                    print "仰泳第", Backstrock.index(b)+1, "个人",
                    print "蛙泳第", Frog.index(c)+1, "个人",
                    print "自由泳第", Free.index(d)+1, "个人",
                    print "总时间：",  time
                    flag = flag + 1

    # 所有可能的情况
    print "所有的情况共有：", len(Result), " 种"

    SortedResult = sorted(Result)
    # 用时最短
    print "最短时间: ", SortedResult[0], "秒"

    num = Result.index(SortedResult[0]) + 1
    print "该方法为第", num, "种"

if __name__ == '__main__':
    func()
