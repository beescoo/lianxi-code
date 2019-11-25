'''
这是个关于类的练习
练习过程中——init——class的内置函数
——repr——内置函数，纠结了很长时间
原来内置函数有self这个参数，会非常方便
它能定义类的属性
其它的内置函数中，能够调用类的属性
总之，目前的情况，还是比较稀里糊涂的
2019.11.25
另外：文件后面有个～是什么意思呢？
'''


class UserDate():                 # 类的格式，第一个字母要大写。
    def __init__(self,num,name):  ＃__init__内置函数，定义了类的各种属性
        self.num = num            ＃ self 就是调用了类的属性
        self.name = name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.num,self.name)
        ＃ 这是一个内置的格式化输出的函数，注意self，这里其实作了很多实验，此前有个 疑问 ，既然有了内置函数，为什么还要在定义一次呢，函数是可以二次定义的吗。这个得问。 
if __name__ == "__main__":         ＃这里不解释了
    user1 = UserDate('101','Jack') ＃这里将对象实例化。
    user2 = UserDate('102','Louplus')
    print(user1)
    print(user2)
