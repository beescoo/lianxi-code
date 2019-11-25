#!/usr/bin/env python3
'''
这个是学完继承之后的一个练习题
第一个类没有去写
直接就练习题的要求，
倒推NewUser怎样定义
用到了继承，
继承的基础上定义了新的属性
问题全出现在参数的理上
下午折腾了半个小时
然后，晚上回家...
不知道怎么弄的，
一下子，就好了
大概是 蒙对的....
现在，就当时的理解
一一注释下吧
'''

class UserDate(object):                 
    def __init__(self,num,name):  
        self.num = num            
        self.name = name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.num,self.name)

#以上和上一道练习题并没有区别

class Newuser(UserDate):
    def get_name(self):
        self.name = name

#名字就是对象的名称 
    def set_name(self,value):
        self.name = value

#设置函数，对象的名称是可以传入参数的
       
if __name__ == "__main__":       
    user1 = Newuser('101','Jack')
#这个继承了父类，但新的类NewUesr重新定义了名字方法，所以这就没毛用了。
    user1.set_name ('Jackie')
    ＃传入了参数
    user2 = Newuser(102,'Louplus')
    print(user1)
    print(user2)
